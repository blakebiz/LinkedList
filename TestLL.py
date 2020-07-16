from LinkedList import LinkedList
import copy


ll = LinkedList()
# basic adding
ll.add(7)
ll.add(3)
ll.insert(5, 2)
ll.insert(9, 3)
ll.append(6)
print(ll)

ll2 = LinkedList()
ll2.add(12, 15)
ll.extend(ll2)
print(ll)
del ll2

# removing
ll.remove(3)
print(ll)
ll.pop()
ll.pop(2)
print(ll)
ll.clear()
print(ll)
ll.add(8)
ll.add(12)
print(ll)

# copying
ll2 = ll.copy()
print(ll == ll2)
print(ll.contentEquals(ll2))
print(ll.dataEquals(ll2))
del ll2
ll2 = copy.deepcopy(ll)
print(ll == ll2)
print(ll.contentEquals(ll2))
print(ll.dataEquals(ll2))
del ll2

# reverse
ll.add(3, 9)
print(ll)
print(reversed(ll))
ll.reverse()
print(ll)

# iterable by for loop
for node in ll:
    e = ', ' if node.next != None else ''
    print(node.__repr__(), end=e)
print()

# supports indexing and multiplication too
ll = ll * 3
print(ll)
print(ll[1:8])
print(ll[1:8:2])
print(ll[::-2])

# set and del items
print(ll)
ll[4] = 17
print(ll)
del ll[4]
print(ll)

# supports sorting and "in"
ll.sort()
print(ll)
ll[5] = 14
print(ll)
print(14 in ll)
print(13 in ll)








