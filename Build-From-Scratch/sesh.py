import readline
import os
import sys
import getpass
import socket
import pathlib

sesh_file = os.getcwd() + "/" + sys.argv[0]

def sesh(args):
    try:
        for line in open(args, "r"):
            execute(line.split())
    except Exception as e:
        print("sesh: cannot access " + args + ": No such file or directory")

def cd(args):
    try:
        if len(args) == 0:
            home_dir = str(pathlib.Path.home())
            os.chdir(home_dir)
        else:
            os.chdir(args)
    except Exception as e:
        print("cd: no such file or directory: " + args)


def dir(args):
    try:
        if len(args) == 0:
            args = "."
        print("  ".join(os.listdir(args)))
    except Exception as e:
        print("dir: cannot access " + args + ": No such file or directory") 

def pause():
    try:
        wait = input("\nThe shell is in the PAUSE state...\n")
        if not wait:
            raise ValueError("Execution has been resumed")
    except ValueError as e:
        print(e)


def color_yellow(word):
    return "\033[1;91m" + word +  "\033[00m"


def color_pink(word):
    return "\033[1;95m" + word +  "\033[00m"


def color_green(word):
    return "\033[1;92m" + word +  "\033[00m"


def launch(args): 
    pid = os.fork()
    if pid > 0:
        wpid = os.waitpid(pid, 0)
    else:
        try:
            os.execvp(args[0], args)
        except Exception as e:
            print("sesh: command not found: " + args[0])


def make_completer(vocabulary):
    def custom_complete(text, state):
        # None is returned for the end of the completion session.
        results = [x for x in vocabulary if x.startswith(text)] + [None]
        # A space is added to the completion since the Python readline doesn't
        # do this on its own. When a word is fully completed we want to mimic
        # the default readline library behavior of adding a space after it.
        return results[state] + " "
    return custom_complete


def read_line(USER, HOST, PWD):
    line = input("\n" + color_yellow(USER) + " in " + color_pink(HOST) + " at " + color_green(PWD) + " --> ").strip()
    return line

def tokenize(line):
    if "&&" in line:
        args = line.split("&&")
        for arg in args:
            execute(arg.split())
        sesh_loop()
    return line.split()


def execute(args):
    try:
        if len(args) == 0:
            pass
        elif "cd" == args[0]:
            cd("".join(args[1:]))
        elif "quit" == args[0]:
            sys.exit(0)
        elif "dir" == args[0]:
            dir("".join(args[1:]))
        elif "pause" == args[0]:
            pause()
        elif "sesh" == args[0]:
            sesh("".join(args[1:]))
        else:
            launch(args)
    except EOFError as e:
        print("")

def sesh_loop():
    USER = getpass.getuser()
    HOST = socket.gethostname()
    while True:
        PWD = os.path.dirname(os.path.realpath(__file__))
        readline.set_completer(make_completer(os.listdir(".")))
        line = read_line(USER, HOST, PWD)
        args = tokenize(line)
        execute(args)

def main():
    readline.parse_and_bind('tab: complete')
    sesh_file = os.getcwd() + "/" + sys.argv[0]
    sesh_loop()
        
if __name__ == '__main__':
    main()

