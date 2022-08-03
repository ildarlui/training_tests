class Stack():
    def __init__(self):
        self.stack = []

    def add_for_stack(self, item):
        self.stack.append(item)

    def get_from_stack(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def get_stack(self):
        return self.stack

    def get_len_stack(self):
        return len(self.stack)

    def pop_stack(self):
        if self.stack:
            removed = self.stack.pop()
            return removed
        else:
            return None

s = Stack()
s.add_for_stack("Add")
s.add_for_stack("Delete")
print(s.get_from_stack())
print(s.get_stack())
print(s.get_len_stack())
print(s.pop_stack())
print(s.get_stack())




