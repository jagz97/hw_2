def sort_list(array):
    n = len(array)
    i = 0

    while i < n:
        j = 0
        while j < n - i - 1:
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            j += 1
        i += 1
    return array


my_array = [6, 8, 2, -1, 0]
print(sort_list(my_array))



