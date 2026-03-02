from .OSAdapters.BaseAdapter import BaseAdapter
from .OSAdapters.Windows import WindowsUtils
from .OSAdapters.MacOS import MacOSUtils
from .OSAdapters.Linux import LinuxUtils


OSUtils: BaseAdapter = WindowsUtils if BaseAdapter.isWindows() else LinuxUtils if BaseAdapter.isLinux() else MacOSUtils