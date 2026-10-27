class Node: 
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        self.top = Node(x, self.top)

    def pop(self):
        if self.top is None:
            return None
        x = self.top.data
        self.top = self.top.next
        return x

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        n = 0
        node = self.top
        while node is not None:
            n += 1
            node = node.next
        return n

    def tampil(self):
        out = []
        node = self.top
        while node is not None:
            out.append(node.data)
            node = node.next
        return out

if __name__ == "__main__":
    s = Stack()
    s.push(10)
    print(s.peek())  