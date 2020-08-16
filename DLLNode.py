class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


    def __repr__(self):
        return f'Node object containing < {self.data} >'


    def __str__(self):
        return str(self.data)


    def __lt__(self, other):
        assert isinstance(other, Node)
        return self.data < other.data


    def __le__(self, other):
        assert isinstance(other, Node)
        return self.data <= other.data