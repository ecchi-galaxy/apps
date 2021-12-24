def first_manu(x = True):
    while x == True:
        print("""sing in
        sing up
        quit""")

def sing_in():
    print('welcome sing in')
def sing_up():
    print('welcome sing up')
def dark_menu():
    i=input(":")
    if i == "sing in":
        sing_in
    elif i == "sing up":
        sing_up
    elif i == "quit":
        exit()
dark_menu