# CalC
CalC (Pronounced Cal - See) is a python script that executes a program and calculates the time taken for it's execution. This can be used to benchmark the time complexity of a program.

Platform:
--------
Linux

Prerequisite:
-------------
Python3

Options Available:
------------------

* --path
This is the path of the executable you want to benchmark.

* --file
This is the path of a file that contains the inputs that are to be given to the executable as  standard input(stdin) i.e all the input that the executable expects to receive from keyboard. The content must be listed in the exact same sequence as is expected by the program. See "Examples" at the end of documentation for more clarification.

* --arg
These are the parameters which will be passed to the executable as command line arguments.

* --loop
Number of time the executable will be executed.


Output:
--------
The debug mode is turned on in the initial commit. It will be made optional later. This is the reason it displays all the received parameters, the command constructed by the script that will be passed to os.system() and only then does the real execution of the executable starts.

After each execution, CalC reports the time taken to execute on system clock and also on the process clock. The process clock is the time that the executable took to execute itself. It does not include the time when your OS kept the executable to sleep and thus it is the actual time taken by the executable to execute itself.
On the other hand, system clock does include the time during which the executable was asleep. So if you were to watch the time of execution on your wall clock or on your wrist clock, this would be it.

After all the executions (number mentioned in --loop parameter), the script displays the average of all system clock timings recorded and all process clock timings recorded.



Usage:
------

```
python3 CalC.py --path ~/My\ Files/My\ Programs/Learning/C++/time.out --arg 5 20 --file ~/My\ Files/My\ Programs/Learning/C++/time.argv --loop 5
```

This will execute "time.out" in "~/My Files/My Programs/Learning/C++/" directory(as mentioned in --path) and pass '5' and '20' as command line arguments to it(as mentioned in --arg). The executable expects an integer as input from keyboard (standard input). Instead of providing an input from the keyboard, I've written the integer in a file "time.argv" which resides in "~/My Files/My Programs/Learning/C++/" directory (as mentioned in --file). The executable "time.out" will be executed '5' times (as mentioned in --loop).

The file "time.out", it's source code and it's standard input file "time.argv" are also available in the 'Example' folder of CalC's Github repository.
