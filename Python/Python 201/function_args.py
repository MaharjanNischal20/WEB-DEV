def add_num(*args):  #*args is a tuple.
    total = 0
    for num in args:
        total += num
    return total

total = add_num(1,2,3,4,5,6,7,8,9)
print(total)