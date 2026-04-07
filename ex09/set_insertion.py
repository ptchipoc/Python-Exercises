# pylint: disable=missing-module-docstring, modified-iterating-list

speed = {
    'jan': 47,
    'feb': 52,
    'march': 47,
    'April': 44,
    'May': 52,
    'June': 53,
    'july': 54,
    'Aug': 44,
    'Sept': 54
}

sample_list = []

for item in speed.values():
    if item not in sample_list:
        sample_list.append(item)

print(sample_list)

# print(speed)
