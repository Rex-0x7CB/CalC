import time
import os
import sys

def calc(command):
    init_sys = time.perf_counter();
    init_proc = time.process_time();
    os.system(command)
    end_sys = time.perf_counter();
    end_proc = time.process_time();

    #print("\n\ninit = ", init)
    #print("end = ", end)
    sys_time = end_sys - init_sys
    proc_time = end_proc - init_proc
    exec_time = (sys_time, proc_time)
    #print("System time = end - init : ", exec_time)
    return exec_time

def main():
    count = -1
    param = 0
    path = ""
    arguments = ""
    std_input_file = ""
    for arg in sys.argv:
        count = count + 1
        print("sys.argv[", count,"] =", arg)
        if arg == "--path" :
            param = 1
            continue
        elif arg == "--arg" :
            param = 2
            continue
        elif arg == "--file" :
            param = 3
            continue
        elif arg == "--loop" :
            param = 4
            continue

        if param == 1 :
            print("Count = ",count, "Saving to path : ", str(sys.argv[count]))
            path = path + str(sys.argv[count])
        if param == 2 :
            arguments = arguments + " " + str(sys.argv[count])
        if param == 3 :
            std_input_file = std_input_file + str(sys.argv[count])
        if param == 4 :
            loop = int(sys.argv[count])

    print("Path :", path)
    print("Command Line Arguments :", arguments)
    print("Standard Input File :", std_input_file)
    print("Number Of Iterations :",loop)

    command = "'" + path + "'" + arguments + " < " + "'" +  std_input_file + "'"
    print("\nCommand to be executed :", command)

    timings = []
    for i in range(0,loop):
        print("\n\nInitiating Execution {}...\n".format(i+1))
        time2execute = calc(command)
        print("\nSystem time taken to execute  : ", time2execute[0], "seconds")
        print("Process time taken to execute : ", time2execute[1], "seconds")
        timings.append(time2execute)

    sys_total = 0
    proc_total = 0
    for timing in timings:
        sys_total = sys_total + timing[0]
        proc_total = proc_total + timing[1]

    sys_average = sys_total/loop
    proc_average = proc_total/loop

    print("\n\nAverage system time for {} executions  :".format(loop), sys_average, "seconds")
    print("Average process time for {} executions :".format(loop), proc_average, "seconds")

if __name__ == "__main__":
    main()
