import numpy as np
import sys

def main():
    ask_num()
    ask_string()


def ask_num(ask, first_num, last_num, parts):
    while True:
        try:
            num = float(input(f"{ask}"))
            if num in np.linspace(first_num, last_num, parts):
                return num
            else:        
                print("Input seems a little unrealistic, please try again.")     
        except ValueError:
            print("The entered value is not a number. Please try again...")


def ask_string(ask):
    while True:
        string = input(f"{ask}")
        if string == "exit":
            sys.exit()
        elif string != "":
            return string
        else:
            print("Seems input asked was left empty. Please try again...")
            

if __name__ == "__main__":
    main()

