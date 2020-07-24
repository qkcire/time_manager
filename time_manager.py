#!/home/eq/miniconda3/envs/time_manager/bin/python3.8

import time
from time import strftime
import datetime as dt

# displays the amount of time remaining on screen
# according to the amount of time set in
# MINUTES, 1 <= min <= 60
def countdown(min):
    start_time = dt.datetime.now()
    target_time = start_time + dt.timedelta(minutes = min)
    time_remaining = target_time - start_time
    print("Begin countdown.")
    while str(time_remaining)[0:7] != '0:00:00':
        current_time = dt.datetime.now()
        time_remaining = target_time - current_time
        print(str(time_remaining)[0:7], end="\r", flush=True)
        time.sleep(1)
    print(flush=True)
    print("Time complete.")

countdown(1)
