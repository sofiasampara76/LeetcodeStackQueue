from collections import deque

class FreqStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        self.stack.appendleft(val)

    def pop(self) -> int:
        if self.stack:
            set_of_elements = set()
            counter = 0
            val = None
            for el in self.stack:
                if el not in set_of_elements:
                    number = self.stack.count(el)
                    set_of_elements.add(el)
                    if number > counter:
                        counter, val = number, el
            self.stack.remove(val)
            return val
        return None