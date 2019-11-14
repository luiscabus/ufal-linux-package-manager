# mpu (minimal package utility)- A simple package manager written in python

# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
from update import *
from install import *


def main(args=None,packages=None):
    if args is None and packages is None:
        args = sys.argv[1:2]
        packages = sys.argv[2:]
        
    if "install" in args:
        # TODO: Install and Resolver modules, and pass "packages" list as
        # an argument to install.
        # TODO: An upgrade warning for older local-key.
        install_packages(packages)
        print("Install a package!")
    elif "delete" in args:
        # TODO: Package and local-package removing function.
        print("Safe removal")
    elif "clear" in args:
        # TODO: Implement an algorithm to build the local-package graph and
        # search for orphan packages.
        print("Clean")
    elif "update" in args:
        sync()
        print("Update manifests")
    elif "upgrade" in args:
        # TODO: A module to map the system packages oudated and upgrade them
        # to newer version
        print("Upgrade packages")
    else:
        sys.exit(1)
        
main()
