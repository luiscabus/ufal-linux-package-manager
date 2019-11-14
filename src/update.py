# Update utility for the MPU-package manager, written by Matheus Artur

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
import os, errno, sys


home = str(Path.home())
manifest_path = str(home)+"/.mpu/manifests/"
manifest_repository = "https://gitlab.com/mpu-pkg-manager/mpu-manifests"
log_path= str(home)+"/.mpu/log/"
log_file= str(log_path)+"update.log"

def sync():
    
    if os.path.exists(str(log_path)) == False:
        os.system("mkdir " +str(log_path))
        
    if os.path.exists( str(manifest_path)+".git") == False:
        sys.stdout.write('Initial repository sync, this might take a while...\n')
        os.system("git clone --quiet " +str(manifest_repository) + " " +str(manifest_path))
        sys.exit("Done! You can manually check repository integrity, news and info at ~/.mpu/manifests/news.org")
        
    else:
        os.system("cd "+str(manifest_path)+" && git pull > " +str(log_file))
    
        if os.stat(str(log_file)).st_size == 0:
            sys.exit("Fatal Error, couldn't update the main repository.\nCheck your network status and ~/.mpu/manifests/news.org for integrity :(")
        else:
            sys.exit("\nDone! MPU Update successfull :)")
