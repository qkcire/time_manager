#!/home/eq/miniconda3/envs/time_manager/bin/python3.8

import time
from time import strftime
import datetime as dt
import os, sys, csv

work = {
    1: "c_programming",
    2: "arm_programming",
    3: "math_maturity",
    4: "fitness",
}

# program main menu
def menu():
    # os.system("clear")
    print("(1) C Programming Book")
    print("(2) ARM Programming")
    print("(3) Math Maturity")
    print("(4) Fitness")
    print("(0) EXIT")
    select = int(input("Enter work type number: "))
    if select < 0 or select > 4:
        print("Error: selection not recognized")
    else:
        print("You selected " + str(select) + " as your option.")
    return select

# output countdown timer according to MIN input
# where: 1 <= MIN <= infinity
def countdown_display(min, work_type):
    start_time = dt.datetime.now()
    target_time = start_time + dt.timedelta(minutes = min)
    time_remaining = target_time - start_time
    os.system("clear")
    print(start_time)
    print("Working on: " + work[work_type])
    # print("TIME LEFT")
    while str(time_remaining)[0:7] != '0:00:00':
        current_time = dt.datetime.now()
        time_remaining = target_time - current_time
        print(" TIME LEFT  "+str(time_remaining)[0:7], end="\r", flush=True)
        time.sleep(1)
    end_time = dt.datetime.now()
    print(flush=True)
    print("TIME COMPLETE")
    input("PRESS enter TO SAVE DATA AND CONTINUE")
    # start timestamp
    start_time_tuple = int(start_time.strftime("%Y%m%d")), int(start_time.strftime("%H%M%S"))
    start = int(str(start_time_tuple[0]) + str(start_time_tuple[1]))
    # end timestamp
    end_time_tuple = int(end_time.strftime("%Y%m%d")), int(end_time.strftime("%H%M%S"))
    end = int(str(end_time_tuple[0]) + str(end_time_tuple[1]))
    save_data(work_type, start, end)
    os.system("clear")

def alarm_clock():
    pass

def save_data(work_type, start_time, end_time):
    with open('time_manager_data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([end_time, start_time, work_type])
        # writer.writerow([work_type, start_time, end_time])
    input("DATA SAVED. PRESS enter to CONTINUE")

def break_time():
    print("BREAK TIME!")
    print("Go away, read some books!")
    input("Press Enter when ready to continue")

def main():
    option = 99
    while option > 0:
        option = menu()
        if option in work.keys():
            os.system("clear")
            print("You've chose to work on: " + work[option].upper())
            print("60 minutes has been set for this work.")
            input("Press ENTER to start time")
            countdown_display(1, option)
            break_time()


if __name__ == "__main__":
    # countdown_display(int(sys.argv[1]))
    main()
