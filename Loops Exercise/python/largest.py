# def find_largest(list_input):
#     largest = list_input[0]
#     for num in list_input:
#         if num < largest:
#             largest = num
#         return largest


# x = [4, 6, 8, 24, 12, 2]
# print(find_largest(x))


def find_largest(list_input):
    largest = list_input[0]

    for num in list_input:
        if num > largest:
            largest = num

    return largest


x = [4, 6, 8, 24, 12, 2]

print(find_largest(x))