import sys
import subprocess
import pkg_resources

def update():

    required = {'fastapi[standard]', 'psutil'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        python = sys.executable
        subprocess.call(['pip', 'install', *missing])