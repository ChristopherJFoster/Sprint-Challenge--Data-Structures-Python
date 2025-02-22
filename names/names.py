import time

from binary_search_tree import BinarySearchTree
from generic_heap import Heap

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

# f = open('names_1.txt', 'r')
# names_1 = Heap(lambda x, y: x < y)
# for row in f:
#     names_1.insert(str.strip(row))
# f.close()

# f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()

f = open('names_2.txt', 'r')
names_2 = BinarySearchTree()
for row in f:
    names_2.insert(str.strip(row))
f.close()

# Stretch: I know the answer is to use a heap, but I couldn't quite get it to work.
# f = open('names_2.txt', 'r')
# names_2 = Heap()
# for row in f:
#     names_2.insert(str.strip(row))
# f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

duplicates = []
for name_1 in names_1:
    if names_2.contains(name_1):
        duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# print(names_2.storage)
