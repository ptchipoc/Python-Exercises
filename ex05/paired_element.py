# pylint: disable=missing-module-docstring

first_list = [2, 3, 4, 5, 6, 7, 8]
print(first_list)

second_list = [4, 9, 16, 25, 36, 49, 64]
print(second_list)

result = zip(first_list, second_list)
result_set = set(result)
print(result_set)
