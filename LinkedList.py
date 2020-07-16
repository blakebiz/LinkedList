from Node import Node
import copy
from collections.abc import Iterable

class LinkedList:
    def __init__(self, data=None, iterable=True):
        '''
        :param data: data to add to linked list (if it is an iterable it will loop through and add each
        piece of data unless you specify iterable = False, then it will just add the iterable to one node)
        :param iterable: only set this to False if initializing with an iterable and you want that iterable
        to be stored in one node and not multiple nodes
        '''
        self.head = None
        self.size = 0
        self.current = None
        if data:
            if isinstance(data, Iterable) and iterable:
                self.extend(data)
            else:
                self.add(data)


    def add(self, data, *args):
        self.size += 1
        if self.head:
            self.head = Node(data, self.head)
        else:
            self.head = Node(data)
        for arg in args:
            self.add(arg)


    def insert(self, data, index):
        if index < 0:
            index = self.size + index
        if index == 0:
            self.add(data); return
        elif index > self.size or index < 0:
            raise IndexError('Invalid index given')
        elif index == self.size:
            self.get(index-1).next = Node(data)
        else:
            current = self.get(index-1)
            old = current.next
            current.next = Node(data, old)
        self.size += 1


    def get(self, index):
        if index < 0:
            index = self.size + index
        if index == 0:
            return self.head
        elif index > self.size - 1 or index < 0:
            raise IndexError('Invalid index given')
        else:
            current, ind = self.head, 0
            while current:
                if index == ind:
                    return current
                ind += 1
                current = current.next


    def append(self, data, *args):
        self.insert(data, self.size)
        for arg in args:
            self.append(arg)


    def copy(self):
        return self.__copy__()


    def __copy__(self):
        ll = LinkedList()
        ll.extend(self)
        return ll

    def deepcopy(self):
        return self.__deepcopy__()

    def __deepcopy__(self, memodict={}):
        ll = LinkedList()
        for node in self:
            ll.append(copy.deepcopy(node.data))
        return ll


    def remove(self, item):
        if self.head.data == item:
            self.head = self.head.next; return
        last = self.head
        for node in self[1:]:
            if node.data == item:
                last.next = item.next
                break
        else:
            raise IndexError('Item not found')


    def pop(self, index=None):
        if index is None:
            index = self.size - 2
        if index < 0:
            index = self.size + index
        if index == 0:
            rv = self.head
            self.head = self.head.next
        elif index > self.size - 1 or index < 0:
            raise IndexError('Invalid index given')
        else:
            prev = self.get(index-1)
            rv = prev.next
            prev.next = prev.next.next
        self.size -= 1
        return rv.data

    def extend(self, iterable):
        if isinstance(iterable, LinkedList):
            if self.size > 0:
                self.get(self.size-1).next = iterable.head
            else:
                self.head = iterable.head
            self.size += len(iterable)
        else:
            for item in iterable:
                self.append(item)


    def reverse(self):
        ll = LinkedList()
        while self.head:
            ll.add(self.pop(0))
        self.extend(ll)
        del ll


    def contentEquals(self, other):
        if self.size != len(other): return False
        for n1, n2 in zip(self, other):
            if n1 != n2:
                return False
        return True


    def dataEquals(self, other):
        if self.size != len(other) or not isinstance(other, LinkedList): return False
        for n1, n2 in zip(self, other):
            if n1.data != n2.data:
                return False
        return True


    def clear(self):
        self.head, self.size = None, 0


    def __reversed__(self, reversing=False):
        ll = LinkedList()
        for node in self:
            ll.add(node)
        return ll


    def __iter__(self):
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


    def __repr__(self):
        return f"Linked List Object Containing: [{', '.join(str(i) for i in self)}]"


    def __str__(self):
        return f"[{', '.join(str(i) for i in self)}]"


    def __len__(self):
        return self.size


    def __mul__(self, other):
        assert other > 0
        for i in range(other-1):
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
            ll = LinkedList()
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
    
    
    def sort(self):
        new = LinkedList(sorted(self))
        self.clear()
        self.extend(new)














