import os

def remove_orphans(path="."):
        # read all files in 'path'
        files = os.listdir(path)
        orphans = []

        # read all manifest files from folder
        for file in files:
                if(file.endswith(".manifest")):
                        orphans.append(file)


        for file in orphans:
                # read all dependencies in manifest file and remove them from 'orphans' list 
                # to ensure no package will lose functionality after orphan removal
                open_file = open(file, "r")
                deps = open_file.readlines()

                for dep in deps:
                        # remove '\n' from package name and add '.manifest' extension
                        dep = (dep.split('\n'))[0]
                        try:
                                orphans.remove(dep + ".manifest")
                        except:
                                pass

                # if file has dependencies, it is not an orphan.
                if(deps != []):
                        try:
                                orphans.remove(file)
                        except:
                                pass

        # resulting list contains only the packages that are not dependencies 
        # to other packages and that have no dependencies, which means: only orphan packages.

        return orphans
