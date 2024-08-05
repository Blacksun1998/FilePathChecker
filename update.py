import sys
import subprocess
import pkg_resources

def update():

    # Get a list of all installed packages
    installed_packages = [dist.project_name for dist in pkg_resources.working_set]
    for package in installed_packages:
        subprocess.call(['pip', 'uninstall', package, '-y'])

    required = {'fastapi[standard]', 'psutil'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

if __name__ == "__main__":
    update()