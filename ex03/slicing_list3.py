# pylint: disable=missing-module-docstring

items = [11, 45, 8, 23, 14, 12, 78, 45, 89]

l1 = items[0:3]
l2 = items[3:6]
l3 = items[6:]

print("Chunk 1",l1)
l1.reverse()
print("After reversing it", l1)

print("Chunk 2",l2)
l2.reverse()
print("After reversing it", l2)

print("Chunk 3",l3)
l3.reverse()
print("After reversing it", l1)
