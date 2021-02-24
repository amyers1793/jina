import subprocess
import time


for i in range(200):
    print(subprocess.run(['vmstat']))
    print(subprocess.run(['ps -eo pcpu,pid,user,args | sort -k 1 -r | head -10'], shell=True, check=True))
    time.sleep(2)
