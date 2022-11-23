def sum(arg):
    total = 0
    for val in arg:
        total += val
    print("Now I will return the total")
    return total

sum([1,2,3,4,5])