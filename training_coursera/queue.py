class Queue():
    def __init__(self):
        self.queue = []

    def add_for_queue(self, item):
        self.queue.append(item)

    def get_from_queue(self):
        if self.queue:
            return self.queue[-1]
        else:
            return None

    def get_queue(self):
        return self.queue

    def get_len_queue(self):
        return len(self.queue)

    def pop_queue(self):
        if self.queue:
            removed = self.queue.pop(0)
            return removed
        else:
            return None

s = Queue()
s.add_for_queue("Add")
s.add_for_queue("Delete")
print(s.get_from_queue())
print(s.get_queue())
print(s.get_len_queue())
print(s.pop_queue())
print(s.get_queue())