# pylint: disable=missing-module-docstring

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print("First set:", first_set)
print("Second set:", second_set)

intersection = first_set & second_set
print("Intersection:", intersection)

first_set -= intersection

print("first_set:", first_set)
