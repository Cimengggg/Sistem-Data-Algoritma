class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        node = Node(data)
        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue kosong (underflow)")
        node = self.front
        self.front = node.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue kosong")
        return self.front.data

    def display(self):
        cur = self.front
        items = []
        while cur:
            items.append(cur.data)
            cur = cur.next
        print(items if items else "Queue kosong")
