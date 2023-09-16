#!/usr/bin/python3
def remove_char_at(str, n):
    string = str

    if len(str) <= n or n < 0:
        return string

    string = string[0:n:] + string[n + 1 :]

    return string


print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
