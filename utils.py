def find_max(numbers):
    m = numbers[0]
    for n in numbers:
        if n>m:
            m = n
    return m
