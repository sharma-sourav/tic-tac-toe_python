import random

array = [' '] * 9
win = False
curr = " "


def chkDiag():
    if array[0] == array[4] and array[4] == array[8] and array[0] != ' ':
        global win
        win = True
        return
    elif array[2] == array[4] and array[4] == array[6] and array[2] != ' ':
        # global win
        win = True
        return


def chkVer():
    for i in range(0, 2, 1):
        if array[i] == array[i + 3] and array[i + 3] == array[i + 6] and array[i] != ' ':
            global win
            win = True
            return


def chkHor():
    for i in range(0, 8, 3):
        if array[i] == array[i + 1] and array[i + 1] == array[i + 2] and array[i] != ' ':
            global win
            win = True
            return


def ChkIfWin():
    chkHor()
    # global win
    if not win:
        chkVer()
    if not win:
        chkDiag()


def chk_input(pos):
    if array[int(pos)] == ' ':
        return True
    else:
        return False


def user_input():
    inp = input("enter a position: ")
    res = chk_input(inp)
    if not res:
        print("wrong input")
        user_input()
    return inp


def get_turn():
    global curr
    if curr == ' ':
        curr = random.choice(['O', 'X'])
    elif curr == 'O':
        curr = 'X'
    else:
        curr = 'O'


def print_board():
    print(array[0] + '|' + array[1] + '|' + array[2])
    print("-----")
    print(array[3] + '|' + array[4] + '|' + array[5])
    print("-----")
    print(array[6] + '|' + array[7] + '|' + array[8])
    print()
    global curr
    print('current user: ' + curr)


# main here
while not win:
    get_turn()
    print_board()
    x = int(user_input())
    array[x] = curr
    ChkIfWin()
    if win:
        # global curr
        print_board()
        print("winner: " + curr)
