import subprocess
import time


for i in range(200):
    print(subprocess.run(['vmstat']))
    time.sleep(2)
