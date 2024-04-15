from collections import deque

class FreqStack:

    def __init__(self):
        self.stack = deque()
        self.dict_of_values = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val in self.dict_of_values:
            self.dict_of_values[val] += 1
        else:
            self.dict_of_values[val] = 1

    def pop(self) -> int:
        max_freq = max(self.dict_of_values.values())
        popped_values = []
        popped = -1
        while self.stack:
            popped = self.stack.pop()
            if max_freq != self.dict_of_values[popped]:
                popped_values.append(popped)
            else:
                self.dict_of_values[popped] -=1
                break
        self.stack.extend(list(reversed(popped_values)))
        return popped
