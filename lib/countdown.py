# your code goes here!
import time

def countdown(int):
    x=int
    while x > 0:
        print(f"{x} SECOND(S)!")
        x -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(int):
    x=int
    while x > 0:
        print(f"{x} SECOND(S)!")
        x -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")