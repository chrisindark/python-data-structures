class Deque(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)


d = Deque()

d.add_front('hello')
d.add_rear('world')
print(d.size())
print(d.remove_front(), ' ', d.remove_rear())

print(d.size())
print(d.is_empty())
