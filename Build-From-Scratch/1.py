import os
import getpass
import socket


def main():
    # get the user's login name, the name of the machine they are on and their current working directory 
    USER = getpass.getuser()
    HOST = socket.gethostname()
    PWD = os.getcwd()

    # read a single line of input to be tokenized. 
    # place your custom prompt in the input parenthesis
    line = input("\n" + USER + " in " + HOST + " at " + PWD + " --> ").strip()

    # tokenize input by using split
    args = line.split()

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
if __name__ == "__main__":
    main()
