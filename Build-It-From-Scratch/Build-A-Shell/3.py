import os
import getpass
import socket
import pathlib
import sys


def read_line(USER, HOST, PWD):
    # read a single line of input to be tokenized. 
    # place your custom prompt in the input parenthesis
    line = input("\n" + USER + " in " + HOST + " at " + PWD + " --> ").strip()
    return line


def tokenize(line):
    # tokenize input by using split
    args = line.split()
    return args


def execute(args):
    # try execute one the change directory command
    # otherwise, generate EOF error  
    try:
        if len(args) == 0:
            pass
        elif "cd" == args[0]:
            cd("".join(args[1:]))
        elif "quit" == args[0]:
            quit()
        else:
            launch(args)
    except EOFError as e:
         print("")


def cd(args):
    # try to change directory based on args provided
    # otherwise, generate error message stating directory does not exist
    try:
        if len(args) == 0:
            home_dir = str(pathlib.Path.home())
            os.chdir(home_dir)
        else:
            os.chdir(args)
    except Exception as e:
        print("cd: no such file or directory: " + args) 


def quit():
    sys.exit(0)


def launch(args):
    # time to execute your input
    # use os.fork to get the process ID
    pid = os.fork()

    # if pid > 0 -> Parent process control
    # else -> Child process control
    if pid > 0:
        wpid = os.waitpid(pid, 0)
    else:
        # try to execeute in the form (command, command_args)
        # generate exception if command does not exist
        try:
            os.execvp(args[0], args)
        except Exception as e:
            print("sesh: command not found: " + args[0])

def main():
    while True:
        # get the user's login name, the name of the machine they are on and their current working directory 
        USER = getpass.getuser()
        HOST = socket.gethostname()
        PWD = os.getcwd()
        line = read_line(USER, HOST, PWD)
        args = tokenize(line)
        execute(args)

if __name__ == "__main__":
    main()
