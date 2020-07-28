#!/home/eq/miniconda3/envs/time_manager/bin/python3.8

import time
from time import strftime
import datetime as dt
import os, sys, csv

work = {
    1: "c programming",
    2: "arm programming",
    3: "math maturity",
    4: "fitness",
    5: "wasting time",
    6: "sleep",
    7: "music",
    8: "family"
}

# program main menu
def menu():
    os.system("clear")
    for key, value in work.items():
        print('({0}) {1}'.format(key, value).upper())
    print("(0) EXIT")
    select = int(input("ENTER WORK TYPE: "))
    if select < 0 or select > 4:
        print("Selection not recognized. Try again.")
    else:
        print("You selected " + str(select) + " as your work_num.")
    return select

def alarm_clock():
    pass

def save_data(work_type, start_time, end_time):
    start, end = convert_time_format(start_time, end_time)
    with open('data_time_manager.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([start, end, work_type])

def break_time():
    print("BREAK TIME!")
    print("BOOK TIME!")
    input("Press Enter when ready to continue")
    os.system("clear")

def convert_time_format(start_time, end_time):
    # date and time concatonated into a string
    # example 2020/07/25 12:11:31 - > 2020-07-25 12:11:31
    start = start_time.strftime("%Y-%m-%d %H:%M:%S")
    end = end_time.strftime("%Y-%m-%d %H:%M:%S")
    return start, end
    # a long int (concatonated date + time)
    # example 2020/07/25 12:11:31 -> 20200725121131
    # start_time_tuple = int(start_time.strftime("%Y%m%d")), int(start_time.strftime("%H%M%S"))
    # start = int(str(start_time_tuple[0]) + str(start_time_tuple[1]))
    # end_time_tuple = int(end_time.strftime("%Y%m%d")), int(end_time.strftime("%H%M%S"))
    # end = int(str(end_time_tuple[0]) + str(end_time_tuple[1]))
    # return start, end

def timer(work_num):
    ON = True
    OFF = False
    init_start_time = dt.datetime.now()
    delta = 0
    resumed_time = 0
    os.system("clear")
    while ON:
        try:
            current_time = dt.datetime.now()
            if resumed_time:
                delta_prime = current_time - resumed_time + delta
                print(" TIME INVESTED ON "+work[work_num].upper()+" +"+str(delta_prime)[0:7], end="\r", flush=True)
            else:
                delta = current_time - init_start_time
                print(" TIME INVESTED ON "+work[work_num].upper()+" +"+str(delta)[0:7], end="\r", flush=True)
            time.sleep(1)            
        except KeyboardInterrupt:
            os.system("clear")
            if resumed_time:
                print(" TIME PAUSED @ " + str(delta_prime)[0:7])
            else:
                print(" TIME PAUSED @ " + str(delta)[0:7])
            resume = int(input(" PRESS (1) TO CONTINUE OR (0) TO END: "))
            os.system("clear")
            if resume:
                if resumed_time:
                    save_data(work_num, resumed_time, current_time)
                    delta = delta_prime
                else:
                    save_data(work_num, init_start_time, current_time)
                resumed_time = dt.datetime.now()
                continue
            else:
                ON = OFF
                if resumed_time:
                    save_data(work_num, resumed_time, current_time)
                    delta = delta_prime
                else:
                    save_data(work_num, init_start_time, current_time)
    return

def main():
    work_num = 99
    while work_num > 0:
        work_num = menu()
        if work_num in work.keys():
            os.system("clear")
            print(" YOU'VE CHOSEN TO WORK ON: " + work[work_num].upper())
            input(" PRESS (ENTER) TO START. . . ")
            timer(work_num)
    os.system("clear")

if __name__ == "__main__":
    main()
