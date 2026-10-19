def max_number(numbers):
    if numbers == []:
        return None
    else:
        largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
