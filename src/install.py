# Installation utility for the MPU-package manager, written by LC

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


from pathlib import Path
import os, errno, sys, glob
from Graph import Graph
import get_package

dep_graph = Graph([], True)
initial_vertex = ""

home = str(Path.home())
manifest_path = str(str(home)+"/.mpu/manifests/")
packages_repository = "https://gitlab.com/mpu-pkg-manager/mpu-packages"
dependency_list_path = str(str(home)+"/.mpu/")
dependency_list = []

# class PackagesInstallation:

def install_packages(user_input):
	global initial_vertex

	if os.path.exists(str(manifest_path)) == False:
		sys.exit("You should first update MPU - use 'main.py update'")

	if not (user_input):
		sys.exit("You should enter at least one package name - use 'main.py install YourPackageName'")

	for package in user_input:

		dependency_list_file = open(dependency_list_path+"dependency_list-"+str(package)+".txt", "w")
		dependency_list_file.write("")

		similarity = [os.path.basename(x) for x in glob.glob(manifest_path+package+'-[0-9]*')]

		if initial_vertex == "":
			initial_vertex = similarity[0]

		for match in similarity:
			dependency_checks(match, package, "")

	# get ordered install list using topological sort
	install_candidates = dep_graph.topological_sort(initial_vertex)

	# consult 'word' file to list installed packages
	with open(dependency_list_path+"world", "r") as file:
		installed_packages = file.read().splitlines()

		# remove already installed packages from 'install_candidates'
		for package in installed_packages:
			if package in install_candidates:
				install_candidates.remove(package)

	# download candidates from repository
	get_package.download(install_candidates)

	with open(dependency_list_path+"world", "w") as file:
		# update 'word' file with installed packages for future checks
		for package in install_candidates:
			file.write(package[:-4]+'.tbz2\n')


def dependency_checks(package, user_input, parent):

	if not package in dependency_list:
		dependency_list.append(package)
		with open(dependency_list_path+"dependency_list-"+str(user_input)+".txt", "a") as file:
			if not parent == "":
				file.write(parent+", "+str(package)+"\n")
				dep_graph.add(str(parent), str(package))

		# print()
		# print("Checking dependencies of > "+ str(package))

		if os.path.isfile(manifest_path+package) == True:
			# sys.exit("The manifest "+package+" doesn't exist.")

			with open(manifest_path+package) as file:
				line = file.readline()

				while line:
					dependency = line.strip()
					# print("- {}".format(dependency))
					dependency_checks(str(dependency+'.mpu'), user_input, package)
					line = file.readline()

				file.close()
