import random


def main():
    splitter = "-" * 47
    print("Hi there!")
    print(splitter)
    print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
    print(splitter)
    game = True
    sec_num = unique_num()
    guesses = 0
    while game:
        players_num = input("Enter a number: ")
        print(splitter)
        guesses += 1
        if players_num == sec_num:
            print("Correct, you've guessed the right number\n in", guesses, "guesses!")
            break
        if not num_check(players_num) == players_num:
            continue
        else:
            print(bulls_cows(players_num, sec_num))


def unique_num():
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    sec_num = []
    while nums:
        i = random.choice(nums)
        if i in sec_num:
            continue
        else:
            sec_num.append(i)
        if sec_num[0] == "0":
            sec_num[0] = random.choice(nums)
        if len(sec_num) == 4:
            sec_num = "".join(sec_num)
            break
    return sec_num


def num_check(players_num):
    if players_num[0] == "0":
        return print("First character cant be 0.")
    elif not len(players_num) == 4:
        return print("Number have to be atleast 4 characters long.")
    elif not players_num.isdecimal():
        return print("All characters must be numbers!")
    else:
        return players_num


def bulls_cows(players_num, sec_num):
    sec_num = sec_num
    bull = "bull: "
    cow = ", cow: "
    bulls = 0
    cows = 0
    if len(players_num) == 4 and players_num[0] != "0":
        for enum, i in enumerate(sec_num):
            if players_num[enum] == sec_num[enum]:
                bulls += 1
            elif i in players_num:
                cows += 1
        if not bulls == 1:
            bull = "bulls: "
        if not cows == 1:
            cow = ", cows: "
        r = bull + str(bulls) + cow + str(cows)
        return r


main()
