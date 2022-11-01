#!/usr/bin/env python3
def guess_number(n):
    while(1):
        guess = int(input("What is your guess?\n>> "))
        if guess == n:
            print("WIN")
            break    
        elif guess > n:
            print("too high")
        elif guess < n:
            print("too low")
        pass
guess_number(23)
