"""
based on http://grodola.blogspot.com/2016/02/how-to-always-execute-exit-functions-in-py.html
"""

import atexit
import os
import functools
import public
import signal
import sys


_registered_exit_funs = set()
_executed_exit_funs = set()

@public.add
def register(func=None, signals=[signal.SIGTERM]):
    """Register a function which will be executed on exit"""

    """or in case one of the `signals` is received
    by this process (differently from atexit.register()).
    Also, it makes sure to execute any other function which was
    previously registered via signal.signal(). If any, it will be
    executed after our own `fun`.

    Functions which were already registered or executed via this
    function will be ignored.

    Note: there's no way to escape SIGKILL, SIGSTOP or os._exit(0)
    so don't bother trying.

    You can use this either as a function or as a decorator:

        @register
        def cleanup():
            pass

        # ...or

        register(cleanup)

    Note about Windows: I tested this some time ago and didn't work
    exactly the same as on UNIX, then I didn't care about it
    anymore and didn't test since then so may not work on Windows.

    Parameters:

    - func: a callable
    - signals: a list of signals for which this function will be
      executed (default SIGTERM)
    """
    def stringify_sig(signum):
        if sys.version_info < (3, 5):
            smap = dict([(getattr(signal, x), x) for x in dir(signal)
                         if x.startswith('SIG')])
            return smap.get(signum, signum)
        else:
            return signum

    def fun_wrapper():
        if func not in _executed_exit_funs:
            try:
                func()
            finally:
                _executed_exit_funs.add(func)

    def signal_wrapper(signum=None, frame=None):
        fun_wrapper()
        # Only return the original signal this process was hit with
        # in case fun returns with no errors, otherwise process will
        # return with sig 1.
        if signum is not None:
            if signum == signal.SIGINT:
                raise KeyboardInterrupt
            # XXX - should we do the same for SIGTERM / SystemExit?
            sys.exit(signum)

    def register_fun(func, signals):
        if not callable(func):
            raise TypeError("{!r} is not callable".format(func))
        set([func])  # raise exc if obj is not hash-able

        signals = set(signals)
        for sig in signals:
            # Register function for this signal and pop() the previously
            # registered one (if any). This can either be a callable,
            # SIG_IGN (ignore signal) or SIG_DFL (perform default action
            # for signal).
            old_handler = signal.signal(sig, signal_wrapper)
            if old_handler not in (signal.SIG_DFL, signal.SIG_IGN):
                # ...just for extra safety.
                if not callable(old_handler):
                    continue
                # This is needed otherwise we'll get a KeyboardInterrupt
                # strace on interpreter exit, even if the process exited
                # with sig 0.
                if (sig == signal.SIGINT and
                        old_handler is signal.default_int_handler):
                    continue
                # There was a function which was already registered for this
                # signal. Register it again so it will get executed (after our
                # new fun).
                if old_handler not in _registered_exit_funs:
                    atexit.register(old_handler)
                    _registered_exit_funs.add(old_handler)

        # This further registration will be executed in case of clean
        # interpreter exit (no signals received).
        if func not in _registered_exit_funs or not signals:
            atexit.register(fun_wrapper)
            _registered_exit_funs.add(func)

    # This piece of machinery handles 3 usage cases. register_exit_fun()
    # used as:
    # - a function
    # - a decorator without parentheses
    # - a decorator with parentheses
    if func is None:
        @functools.wraps
        def outer(func):
            return register_fun(func, signals)
        return outer
    else:
        register_fun(func, signals)
        return func
