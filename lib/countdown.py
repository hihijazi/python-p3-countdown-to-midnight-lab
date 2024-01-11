# your code goes here!
# import ipdb
import time


def countdown(int):
    while int >= 1:
        print(f"{int} SECOND(S)!")
        int -= 1
        # countdown_with_sleep(1)
    print('HAPPY NEW YEAR!')

countdown(4)


def countdown_with_sleep(int):
    while int >= 1:
        print(f"{int} SECOND(S)!")
        int -= 1
        time.sleep(1)
    print('HAPPY NEW YEAR!')
countdown_with_sleep(5)