import update
update.update()

import os
import psutil

# Get the system root directory
system_root = os.path.abspath(os.sep)
print("System Root Directory:", system_root)

# Get all hard drive letters
drive_letters = [disk.device for disk in psutil.disk_partitions()]
print("Hard Drive Letters:", drive_letters)
