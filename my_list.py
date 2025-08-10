# Creating empty list
my_list = []

# Adding elements to list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"First List: {my_list}")

# Adding 15 at 2nd position
my_list.insert(1, 15)
print(f"List after insertion: {my_list}")

# Extending list with another list
my_list.extend([50, 60, 70])
print(f"List after extending: {my_list}")

# Removing last element
my_list.pop()
print(f"List after deletion: {my_list}")

# Sorting list in ascending order
my_list.sort()
print(f"List after sorting: {my_list}")

# Find index of 30
index_of_30 = my_list.index(30)
print(f"Index of value 30: {index_of_30}")