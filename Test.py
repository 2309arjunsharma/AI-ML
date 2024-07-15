def reversed_array(array):
    rarray = array[::-1]
    print("Reversed array", end=" ")
    for i in rarray:
        print(i, end=" ")

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr)
reversed_array(arr)