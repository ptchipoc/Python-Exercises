# pylint: disable=missing-module-docstring, modified-iterating-list

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

sample_list = list(set(sample_list))
print("unique items",sample_list)

sample_tuple = tuple(sample_list)
print("tuple", sample_tuple)

print("min:", min(sample_tuple))
print("max:", max(sample_tuple))
