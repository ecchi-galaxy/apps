x = True
import os
def first_menu():
    print("""sing in
sing up
quit""")


def sing_in():
    print('welcome please wait ...')
    messageandnickname()

def messageandnickname(x  = True):
    n = input("nickname enter:")
    while x == True:
        m = input(':')
        f = ("{}: {}".format(n,m))
        p = print(f)
        if m == ".quit":
            exit()
        elif m == ".help":
            print("no helper sorry.")
        elif m == ".back":
            x = False
        elif m == ".report":
            report()
def sing_up():
    folder = open(" sing-up.md","a")
    n = input("name enter:")
    p = input("password:")
    folder.write(n)
    folder.write(p)
    folder.close
    sing_in()

while x == True:
    first_menu()
    i=input(":")
    if i == "sing in":
        sing_in()
    elif i == "sing up":
        sing_up()
    elif i == "quit":
        exit()
