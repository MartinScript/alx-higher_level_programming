#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = tuple(map(lambda x, y: x + y if x !=
                      None or y != None else x == 0, tuple_a, tuple_b))
    return new_tuple


tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
