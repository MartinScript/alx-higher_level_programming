#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False


def uppercase(str):
    for letter in str:
        print(
            "{:c}".format(ord(letter) - 32 if islower(letter) else ord(letter)), end=""
        )

    print()


for i in reversed(range(97, 123)):
    print("{:c}".format(i if i % 2 == 0 else i - 32), end="")
