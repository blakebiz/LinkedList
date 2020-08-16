import copy
from DoublyLinkedList import DoublyLinkedList


ll = DoublyLinkedList()
# basic adding
ll.add(7)
ll.add(3)
ll.add(5)
ll.append(6)
ll.append(9)
print(ll)

ll.insert(12, 3)
ll.insert(15, 0)
ll.insert(17, 1)
print(ll)
print(ll.size)
ll.insert(19, 8)
ll.insert(18, 8)

print(ll)
ll2 = DoublyLinkedList()
ll2.add(1, 2, 3)
ll2.append(4, 5, 6)
print(ll2)
print(len(ll), len(ll2))
ll.extend(ll2)
print(ll)
print(ll2)
print(len(ll), len(ll2))
ll2.reverse()
print(ll2)

# ll.insert(5, 2)
# ll.insert(9, 3)
#
# print(ll)
# print(ll.get(0))
# print(ll.get(1))
# print(ll.get(2))
# print(ll.get(3))
# print(ll.get(4))
# print(ll.get(-1))
# print(ll.get(-2))
# print(ll.get(-3))
# print(ll.get(-4))
# print(ll.get(-5))




