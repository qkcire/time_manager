#!/home/eq/miniconda3/envs/time_manager/bin/python3.8

import time
from time import strftime
import datetime as dt
import os, sys

# output countdown timer according to MIN input
# where: 1 <= MIN <= infinity
def countdown_display(min):
    start_time = dt.datetime.now()
    target_time = start_time + dt.timedelta(minutes = min)
    time_remaining = target_time - start_time
    os.system("clear")
    print("\t\t\t\t        TIME LEFT")
    while str(time_remaining)[0:7] != '0:00:00':
        current_time = dt.datetime.now()
        time_remaining = target_time - current_time
        print("\t\t\t\t\t "+str(time_remaining)[0:7], end="\r", flush=True)
        time.sleep(1)
    print(flush=True)
    print("\t\t\t\t      TIME COMPLETE")
    input("\t\t\t\t   PRESS enter TO EXIT")
    os.system("clear")

if __name__ == "__main__":
    countdown_display(int(sys.argv[1]))

