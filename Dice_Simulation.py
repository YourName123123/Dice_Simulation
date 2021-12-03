#Command = 1-10 (the number you roll virtual dice)
#        = 'Exit' or 'exit'(to quit this program)
import random
import time

def main():
    Number = ["1","2","3","4","5","6","7","8","9","10"]
    Command = input("Command:")
    if Command in Number:
        n = int(Command)
        for i in range(0,n):
            num = random.randint(1,6)
            print(num)
            time.sleep(0.2)
        main()
    elif Command == "Exit" or "exit":
        exit()
    else:
        print("Unavailable command")
        main()


if __name__ == '__main__':
    main()