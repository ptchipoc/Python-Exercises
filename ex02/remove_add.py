# pylint: disable=missing-module-docstring

items = [34, 54, 67, 89, 11, 43, 94]
print("Print original list:", items)

print("Original list:", items)
element = items.pop(4)
print("List after removing element at 4 position:", items)

items.insert(2, element)
print("List after adding element at 2 position:", items)

items.append(element)
print("List after adding element at last position:", items)
