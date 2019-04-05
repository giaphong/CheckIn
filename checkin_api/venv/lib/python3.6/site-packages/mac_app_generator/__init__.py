#!/usr/bin/env python
# -*- coding: utf-8 -*-
import chmod
import control_characters
import mdfind
import os
import plistlib
import public
import subprocess
import sys
from writable_property import writable_property

"""
path/to/<name>.py                                 class Name(mac_app.App)

output:
~/Applications/.mac-app-generator/<name>.app                 (customizable)

app logs:
~/Library/Logs/Applications/<name>/out.log        (customizable)
~/Library/Logs/Applications/<name>/err.log        (customizable)

app files:
<name>.app/Contents/MacOS/executable              bash wrapper (hack to keep app visible)
<name>.app/Contents/MacOS/launchd.plist           launchd.plist
<name>.app/Contents/MacOS/script                  (your class file)
"""

LOGS = os.path.join(os.environ["HOME"], "Library/Logs/Applications")
CODE = """#!/usr/bin/env bash

# LaunchAgent required to keep app visible in Dock
set "${0%/*}"/launchd.plist
trap "launchctl unload '$1'" EXIT
PlistBuddy() { /usr/libexec/PlistBuddy "$@"; }
PlistBuddy -c "Delete WorkingDirectory" -c "Add WorkingDirectory string ${0%/*}" "$1"
PlistBuddy -c "Delete Program" -c "Add Program string ${0%/*}"/script "$1"

Label="$(PlistBuddy -c "Print Label" "$1")"
# logs must exists or launchd will create logs with root permissions
logs="$(PlistBuddy -c "Print StandardErrorPath" -c "Print StandardOutPath" "$1")"
dirs="$(echo "$logs" | grep / | sed 's#/[^/]*$##' | uniq)"
( IFS=$'\\n'; set -- $dirs; [ $# != 0 ] && mkdir -p "$@" )

launchctl unload "$1" 2> /dev/null; launchctl load -w "$1"
while :; do sleep 0.3 && launchctl list "$Label" | grep -q PID || exit 0; done
"""


def dirname(path):
    return os.path.dirname(path)


def write(path, data):
    """write a dictionary to a plist file"""
    path = os.path.abspath(os.path.expanduser(path))
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    data = {k: v for k, v in data.items() if v is not None}
    if hasattr(plistlib, "dump"):
        plistlib.dump(data, open(path, 'wb'))
    else:
        plistlib.writePlist(data, path)


@public.add
class App:
    """Mac app generator. writable properties: `app_folder`, `app_name`, `app_path`, `app_code`, `app_script`, `app_image`, `app_stderr`, `app_stdout`, `app_env`. methods: `create_app()`"""
    app_env = dict((k, control_characters.remove(str(v))) for k, v in os.environ.items())

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if v is not None:
                setattr(self, k, v)

    @writable_property
    def app_name(self):
        """app name. default is class name
app name concepts:
1)   custom name self._app_name with @app_name.setter
2)   class name self.__class__.__name__.lower().replace("_", "-")
3)   module name (os.path.splitext(os.path.basename(self.app_script))[0].replace("_", "-"))
        """
        return self.__class__.__name__.lower().replace("_", "-")

    @writable_property
    def app_folder(self):
        """app folder. default is `~/Applications/.appify/`"""
        return os.path.expanduser("~/Applications/.mac-app-generator")

    @writable_property
    def app_script(self):
        """source script path. default is class module file"""
        return sys.modules[self.__class__.__module__].__file__

    @writable_property
    def app_code(self):
        """source code string"""
        return open(self.app_script).read()

    @writable_property
    def app_path(self):
        """app path. `app_folder`+`app_name`"""
        path = os.path.join(self.app_folder, self.app_name)
        return "%s.app" % path if os.path.splitext(path)[1] != ".app" else path

    @writable_property
    def app_image(self):
        """app image. default is `mdfind kMDItemFSName=<app_name>.png` result"""
        filename = "%s.png" % self.app_name
        matches = mdfind.mdfind(["kMDItemFSName=%s" % filename]).splitlines()
        if matches and os.path.exists(matches[0]) and os.path.isfile(matches[0]):
            return matches[0]

    @writable_property
    def app_stdout(self):
        """stdout path. default is `~/Library/Logs/Applications/<name>/out.log`"""
        return os.path.join(LOGS, self.app_name, "out.log")

    @writable_property
    def app_stderr(self):
        """stderr path. default is `~/Library/Logs/Applications/<name>/err.log`"""
        return os.path.join(LOGS, self.app_name, "err.log")

    def create_app(self):
        """create Mac app"""
        if ".app/" not in os.getcwd():
            self.create_app_executable()
            self.create_app_script()
            if self.app_image:
                self.create_app_icon()
            self.create_app_info()
            self.create_app_launchd()
            self.refresh_app()
        return self

    def create_app_launchd(self):
        Label = "%s.app" % self.app_name
        """<Program> and <WorkingDirectory> are created at runtime"""
        data = dict(
            Label=Label,
            RunAtLoad=True,
            EnvironmentVariables=self.app_env,
            StandardOutPath=os.path.expanduser(self.app_stdout),
            StandardErrorPath=os.path.expanduser(self.app_stderr)
        )
        path = os.path.join(self.app_path, "Contents", "MacOS", "launchd.plist")
        write(path, data)

    def create_app_executable(self):
        """create app executable file"""
        path = os.path.join(self.app_path, "Contents", "MacOS", "executable")
        dirname = os.path.dirname(path)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        open(path, "w").write(CODE)
        chmod.make.executable(path)

    def create_app_script(self):
        """create app script file"""
        path = os.path.join(self.app_path, "Contents", "MacOS", "script")
        dirname = os.path.dirname(path)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        open(path, "w").write(self.app_code)
        chmod.make.executable(path)

    def create_app_icon(self):
        """create app icon"""
        if not self.app_image:
            raise OSError('app_image unknown')
        if not os.path.exists(self.app_image):
            raise OSError('%s NOT EXISTS' % self.app_image)
        path = os.path.join(self.app_path, "Contents", "Resources", "Icon.icns")
        dirname = os.path.dirname(path)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        args = ["/usr/bin/sips", "-s", "format", "icns", self.app_image, "--out", path]
        subprocess.check_call(args, stdout=subprocess.PIPE)

    def create_app_info(self):
        path = os.path.join(self.app_path, "Contents", "Info.plist")
        dirname = os.path.dirname(path)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        data = dict(CFBundleExecutable="executable")
        if self.app_image:
            data.update(CFBundleIconFile="Icon.icns")
        write(path, data)

    def refresh_app(self):
        """remove .DS_Store and touch folder"""
        for folder in [self.app_path, os.path.dirname(self.app_path)]:
            try:
                f = os.path.join(folder, ".DS_Store")
                if os.path.exists(f):
                    os.unlink(f)
                os.utime(folder, None)
            except PermissionError:
                pass
        return self

    def __str__(self):
        return '<App "%s">' % self.app_path

    def __repr__(self):
        return self.__str__()
