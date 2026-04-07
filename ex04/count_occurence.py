# pylint: disable=missing-module-docstring

items = [11, 45, 8, 11, 23, 45, 23, 45, 89]
res = {}

for item in items:
    if item  not in res:
        res[item] = items.count(item)

print(res)
