#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) == "e" or chr(i) == "p":
        continue
    print("{:c}".format(i), end="")
