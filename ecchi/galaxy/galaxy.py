x = True
import os
def first_menu():
    print("""sing in
sing up
quit""")


def sing_in():
    print('welcome sing in')

def sing_up():
    print('welcome sing up')

def dark_menu():
    first_menu()
    i=input(":")
    if i == "sing in":
        sing_in()
    elif i == "sing up":
        sing_up()
    elif i == "quit":
        exit()
dark_menu()