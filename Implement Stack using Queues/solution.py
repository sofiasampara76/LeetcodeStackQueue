class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def push(self, element):
        cur = self.head
        if cur is None:
            self.head = Node(element)
            self.tail = self.head
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(element)
            self.tail = cur.next

    def pop(self):
        if self.head is None:
            return None
        if self.head.next is None:
            popped = self.head
            self.head = None
            self.tail = None
            return popped.item
        head = self.head
        self.head = self.head.next
        return head.item

    def __len__(self):
        length = 0
        cur = self.head
        while cur is not None:
            cur = cur.next
            length += 1
        return length

    def is_empty(self):
        return self.head is None

    def peek(self):
        return self.head.item if self.head else None


class MyStack:

    def __init__(self):
        self.queue = Queue()
        self.temporary_queue = Queue()

    def push(self, x: int) -> None:
        self.queue.push(x)

    def pop(self) -> int:
        while len(self.queue) > 1:
            self.temporary_queue.push(self.queue.pop())
        popped = self.queue.pop()
        self.temporary_queue, self.queue = self.queue, self.temporary_queue
        return popped

    def top(self) -> int:
        while len(self.queue) > 1:
            self.temporary_queue.push(self.queue.pop())
        top = self.queue.peek()
        self.temporary_queue.push(self.queue.pop())
        self.temporary_queue, self.queue = self.queue, self.temporary_queue
        return top

    def empty(self) -> bool:
        return self.queue.is_empty()


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
print(param_2)
print(obj.top())

print(obj.empty())