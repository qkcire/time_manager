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
    os.system("clear")
    print("(1) C Programming Book")
    print("(2) ARM Programming")
    print("(3) Math Maturity")
    print("(4) Fitness")
    print("(0) EXIT")
    select = int(input("Enter work type number: "))
    if select < 0 or select > 4:
        print("Selection not recognized. Try again.")
    else:
        print("You selected " + str(select) + " as your work_num.")
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
    try:
        while str(time_remaining)[0:7] != '0:00:00':
            current_time = dt.datetime.now()
            time_remaining = target_time - current_time
            print(" TIME LEFT  "+str(time_remaining)[0:7], end="\r", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Keyboard pause initiated.")
        print("Ending clock.")
        return

    end_time = dt.datetime.now()
    print(flush=True)
    print("TIME COMPLETE")
    start_page, end_page = map(int, input("Enter the start page, end page: ").split(", "))
    input("PRESS enter to SAVE DATA AND CONTINUE")
    # start timestamp
    start_time_tuple = int(start_time.strftime("%Y%m%d")), int(start_time.strftime("%H%M%S"))
    start = int(str(start_time_tuple[0]) + str(start_time_tuple[1]))
    # end timestamp
    end_time_tuple = int(end_time.strftime("%Y%m%d")), int(end_time.strftime("%H%M%S"))
    end = int(str(end_time_tuple[0]) + str(end_time_tuple[1]))
    save_data(work_type, start, end, end_page, start_page)
    os.system("clear")

def alarm_clock():
    pass

def save_data(work_type, start_time, end_time):
    start, end = convert_time_format(start_time, end_time)
    with open('data_time_manager.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([start, end, work_type])
        # writer.writerow([work_type, start_time, end_time])

def break_time():
    print("BREAK TIME!")
    print("BOOK TIME!")
    input("Press Enter when ready to continue")
    os.system("clear")

def convert_time_format(start_time, end_time):
    start_time_tuple = int(start_time.strftime("%Y%m%d")), int(start_time.strftime("%H%M%S"))
    start = int(str(start_time_tuple[0]) + str(start_time_tuple[1]))
    end_time_tuple = int(end_time.strftime("%Y%m%d")), int(end_time.strftime("%H%M%S"))
    end = int(str(end_time_tuple[0]) + str(end_time_tuple[1]))
    return start, end

def timer(work_num):
    ON = True
    OFF = False
    init_start_time = dt.datetime.now()
    cntd_time = 0
    os.system("clear")
    while ON:
        try:
            current_time = dt.datetime.now()
            # if cntd_time:
            #     delta = current_time - init_start_time + cntd_time
            # else:
            #     delta = current_time - init_start_time
            delta = current_time - init_start_time
            print("TIME INVESTED "+str(delta)[0:7], end="\r", flush=True)
            time.sleep(1)            
        except KeyboardInterrupt:
            os.system("clear")
            print("TIME PAUSED @ " + str(delta)[0:7])
            pause = int(input("press 1 to continue or 0 to end timer: "))
            if pause == 1:
                if cntd_time:
                    save_data(work_num, cntd_time, current_time)
                else:
                    save_data(work_num, init_start_time, current_time)
                    cntd_time = dt.datetime.now()
                continue
                # cntd_time = dt.timedelta(seconds=(current_time - init_start_time).seconds)
                # continue
            else:
                ON = OFF
    return
    # try:
    #     while True:
    #         current_time = dt.datetime.now()
    #         delta = current_time - start_time
    #         print("TIME INVESTED "+str(delta)[0:7], end="\r", flush=True)
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     os.system("clear")

    #     print("TIME PAUSED @ " + str(delta)[0:7])
    #     input("press ENTER to continue")
    #     return

def main():
    work_num = 99
    while work_num > 0:
        work_num = menu()
        if work_num in work.keys():
            os.system("clear")
            print("You've chose to work on: " + work[work_num].upper())
            input("Press ENTER to start time")
            timer(work_num)
            # countdown_display(5, work_num)
            # break_time()


if __name__ == "__main__":
    # countdown_display(int(sys.argv[1]))
    main()
