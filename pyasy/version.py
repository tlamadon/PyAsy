"""PyAsy version information.

   To obtain the version of PyAsy::

     >>> import pyasy.version
     >>> pyasy.version.version()
     >>> pyasy.version.git_version()

   """

import imp
import os

def _version(name):
    version_file = os.path.join(os.path.dirname(__file__), name + '.py')
    version = imp.load_module('pyasy.pyasy.' + name,
                              open(version_file),
                              version_file,
                              ('.py', 'U', 1))
    return version.version

def version():
    """Return current version."""
    return _version('__version__')

def git_version():
    """Return current *git* version (if available)."""
    return _version('__git_version__')
