def max_nums(array:list) -> list:
    sub_array = list()
    for i in range(4):
        sub_array.append(max(array))
        del array[array.index(sub_array[i])]

    return sub_array

array = [11, -3, 20, -17, 25, 10, 9, -4, 5]
array = max_nums(array)

print(f"O array é {array} e a soma é: {sum(array)}")