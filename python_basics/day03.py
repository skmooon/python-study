def filter_even(numbers):
    n = []
    for i in numbers:
        if i % 2 == 0:
            n.append(i)   
    return n
