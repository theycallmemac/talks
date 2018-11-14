    #################################
    # CALCULATOR FUNCTIONS
    ################################

    def add(x, y):
        pass

    def sub(x, y):
        pass

    def mul(x, y):
        pass

    def div(x, y):
        pass

    def mod(x, y):
        pass

    def exp(x, y):
        pass

    #################################
    # RUN CALCULATOR & MAIN FUNCTIONS
    #################################

    # DONT CHANGE THIS CODE

    def run_calculator(line):
        # set command as first word passed to the program
        command = line[0]

        # run until command is exit
        while command != "exit":
            
            # check that line is of format - `command x y`
            if len(line) > 3 or len(line) == 1:
                # tell user error occured and end program
                print("Error in number of arguments supplied!")
                break
            else:
                # set values of x and y
                x, y = int(line[1]), int(line[2])
            
            # get name of command passed by the user as a function
            func = globals()[command]

            # run command with x and y as parameters and print result
            print(func(x, y))

            # read in next lien of input and split on whitespace
            line = input().split(" ")

            # set new command
            command = line[0]

    def main():
        # split input on whitespace
        line = input().split(" ")

        # run calculator with split line
        run_calculator(line)

    if __name__ == "__main__":
        main()

