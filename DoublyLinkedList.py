from DLLNode import Node
from collections import Iterable
import copy

class DoublyLinkedList:
    def __init__(self, data=None, iterable=True):
        '''
        :param data: data to add to linked list (if it is an iterable it will loop through and add each
        piece of data unless you specify iterable = False, then it will just add the iterable to one node)
        :param iterable: only set this to False if initializing with an iterable and you want that iterable
        to be stored in one node and not multiple nodes
        '''
        self.head = self.tail = self.current = None
        self.size = 0
        if data:
            if isinstance(data, Iterable) and iterable:
                self.extend(data)
            else:
                self.add(data)




    def add(self, data, *args):
        if isinstance(data, Node): data = data.data
        self.size += 1
        node = Node(data, self.head)
        if self.head: self.head.previous = node
        else: self.tail = node
        self.head = node
        for arg in args:
            self.add(arg)


    def append(self, data, *args):
        if isinstance(data, Node): data = data.data
        self.size += 1
        node = Node(data, previous=self.tail)
        if self.tail: self.tail.next = node
        else: self.head = node
        self.tail = node
        for arg in args:
            self.append(arg)


    def insert(self, data, index):
        if isinstance(data, Node): data = data.data
        if index == 0:
            self.add(data); return
        if index == self.size:
            self.append(data); return
        node = self.get(index)
        prev = node.previous
        new = Node(data, node, prev)
        prev.next, node.previous = new, new
        self.size += 1


    def get(self, index):
        if index < 0:
            index = self.size + index
        if index == 0:
            return self.head
        if index == self.size-1:
            return self.tail
        if index > self.size - 1 or index < 0:
            raise IndexError('Invalid index given')
        if index > self.size / 2:
            itr, index = self.iterBackwards(), self.size - index - 1
        else:
            itr = self
        for i, node in enumerate(itr):
            if i == index:
                self.current = None
                return node


    def pop(self, index=None):
        if index is None or index == self.size-1:
            self.tail.previous.next = None
            self.tail = self.tail.previous
            self.size -= 1
            return
        if index < 0:
            index = self.size + index
        if index == 0:
            self.head.next.previous = None
            self.head = self.head.next
            self.size -= 1
            return
        if index < 0 or index >= self.size:
            raise IndexError('Invalid index given')
        node = self.get(index)
        prev, next = node.previous, node.next
        prev.next, next.previous = next, prev
        node.next, node.previous = None, None
        self.size -= 1
        return node


    def remove(self, item):
        if isinstance(item, Node): item = item.data
        for node in self:
            if node.data == item:
                prev, next = node.previous, node.next
                if prev != None:
                    prev.next = next
                if next != None:
                    next.previous = prev
                del node
                self.size -= 1
                break


    def copy(self):
        return self.__copy__()


    def reverse(self):
        current = self.head
        while current != None:
            current.next, current.previous = current.previous, current.next
            current = current.previous
        self.head, self.tail = self.tail, self.head


    def extend(self, iterable):
        if isinstance(iterable, DoublyLinkedList):
            if self.size > 0:
                self.tail.next = iterable.head
            else:
                self.head = iterable.head
            self.size += len(iterable)
        else:
            for item in iterable:
                self.append(item)


    def contentEquals(self, other):
        if self.size != len(other): return False
        for n1, n2 in zip(self, other):
            if n1 != n2:
                return False
        return True


    def dataEquals(self, other):
        if self.size != len(other) or not isinstance(other, DoublyLinkedList): return False
        for n1, n2 in zip(self, other):
            if n1.data != n2.data:
                return False
        return True


    def clear(self):
        self.head, self.tail, self.size = None, None, 0


    def iterBackwards(self):
        current = self.tail
        while current:
            yield current
            current = current.previous


    def sort(self):
        new = DoublyLinkedList(sorted(self))
        self.clear()
        self.extend(new)


    def __iter__(self):
        self.current = None
        return self


    def __next__(self):
        if not self.current:
            if not self.head:
                self.current = None
                raise StopIteration
            self.current = self.head
        else:
            if not self.current.next:
                self.current = None
                raise StopIteration
            self.current = self.current.next
        return self.current


    def __reversed__(self):
        dll = DoublyLinkedList()
        for node in self:
            dll.add(node.data)
        return dll


    def __copy__(self):
        dll = DoublyLinkedList()
        dll.extend(self)
        return dll


    def __deepcopy__(self, memodict={}):
        ll = DoublyLinkedList()
        for node in self:
            ll.append(copy.deepcopy(node.data))
        return ll


    def __repr__(self):
        return f"Linked List Object Containing: [{', '.join(str(i) for i in self)}]"


    def __str__(self):
        return f"[{', '.join(str(i) for i in self)}]"


    def __len__(self):
        return self.size


    def __mul__(self, other):
        assert other > 0
        for i in range(other - 1):
            self.extend(copy.deepcopy(self))
        return self


    def __getitem__(self, item):
        if isinstance(item, int):
            return self.get(item)
        elif isinstance(item, slice):
            start, stop, step = item.start or 0, item.stop or self.size, item.step or 1
            assert all(type(i) == int for i in (start, stop, step))
            if start < 0: start = self.size + start
            if stop < 0: stop = self.size + stop
            if step < 0: rev = True; step = -step
            else: rev = False
            ll = DoublyLinkedList()
            for i, x in enumerate(self):
                if start <= i < stop and (i + start) % step == 0:
                    ll.append(x)
            if rev:
                return reversed(ll)
            return ll
        else:
            raise TypeError('Invalid index type given (accepted indexes: int, slice)')


    def __setitem__(self, key, value):
        assert isinstance(key, int)
        self.get(key).data = value


    def __delitem__(self, key):
        assert isinstance(key, int)
        self.pop(key)


    def __contains__(self, item):
        for node in self:
            if node == item or node.data == item:
                return True
        return False




