#!/usr/bin/env python
import inspect
import os
import plistlib
import public


"""
https://www.real-world-systems.com/docs/launchd.plist.5.html
"""

KEYS = [
    "Label",
    "Disabled",
    "UserName",
    "GroupName",
    "inetdCompatibility",
    "LimitLoadToHosts",
    "LimitLoadFromHosts",
    "LimitLoadToSessionType",
    "Program",
    "ProgramArguments",
    "EnableGlobbing",
    "EnableTransactions",
    "OnDemand",
    "KeepAlive",
    "RunAtLoad",
    "RootDirectory",
    "WorkingDirectory",
    "EnvironmentVariables",
    "Umask",
    "TimeOut",
    "ExitTimeOut",
    "ThrottleInterval",
    "InitGroups",
    "WatchPaths",
    "QueueDirectories",
    "StartOnMount",
    "StartInterval",
    "StartCalendarInterval",
    "StandardInPath",
    "StandardOutPath",
    "StandardErrorPath",
    "Debug",
    "WaitForDebugger",
    "SoftResourceLimits",
    "HardResourceLimits",
    "Nice",
    "ProcessType",
    "AbandonProcessGroup",
    "LowPriorityIO",
    "LaunchOnlyOnce",
    "MachServices",
    "Sockets"
]


@public.add
def read(path):
    """return a dictionary with a plist file data"""
    if hasattr(plistlib, "load"):
        return plistlib.load(open(path, 'rb'))
    return plistlib.readPlist(path)


@public.add
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
def update(path, **kwargs):
    """update a plist file"""
    new = {}
    if os.path.exists(path):
        old = dict(read(path))
        new = dict(old)
    new.update(kwargs)
    write(path, new)


def isproperty(obj):
    return isinstance(obj, property)


def iscapitalized(string):
    return string[0] != "_" and string[0] == string[0].upper() and string != string.upper()


@public.add
class Plist:
    """launchd.plist class"""

    def __init__(self, **kwargs):
        self.update(kwargs)

    def keys(self):
        """return a list of object launchd.plist keys"""
        attr_keys = list(self.__dict__.keys()) + list(self.__class__.__dict__.keys())
        prop_keys = []
        for name, member in inspect.getmembers(self.__class__):
            if isinstance(member, property):
                prop_keys.append(name)
        return list(filter(iscapitalized, attr_keys + prop_keys))

    def update(self, *args, **kwargs):
        """Update the dictionary with the key/value pairs from other, overwriting existing keys"""
        inputdict = dict(*args, **kwargs)
        for k, v in inputdict.items():
            setattr(self, k, v)

    def get(self, key, default=None):
        """return the value for key if key is in the dictionary, else default"""
        return getattr(self, key, default)

    @property
    def data(self):
        """return dictionary with launchd plist keys only"""
        result = dict()
        for key in self.keys():
            value = getattr(self, key)
            if value is not None and value != [] and value != "":
                result[key] = value
        return result

    def load(self, path):
        """load data from .plist file"""
        data = read(path)
        self.update(data)
        return self

    def create(self, path):
        """create .plist file"""
        write(path, self.data)
        for key in ["StandardErrorPath", "StandardOutPath"]:
            dirname = os.path.dirname(getattr(self, key, ""))
            if dirname and not os.path.exists(dirname):
                os.makedirs(dirname)

    def __contains__(self, key):
        """return hasattr(self,key)"""
        return hasattr(self, key) and getattr(self, key, None) is not None

    def __getitem__(self, key):
        """return getattr(self,key)"""
        return getattr(self, key)

    def __setitem__(self, key, value):
        """setattr(self,key, value)"""
        return setattr(self, key, value)

    def __str__(self):
        return "<%s Label='%s'>" % (self.__class__.__name__, self.get("Label", "UNKNOWN"))

    def __repr__(self):
        return self.__str__()


class MyPlist(Plist):
    Label = "MyPlist"
    StartInterval = 1
    Custom_key = "works for Capitalized keys!"

    @property
    def StandardErrorPath(self):
        return os.path.expanduser("~/Logs/LaunchAgents/%s/err.log" % self.Label)
