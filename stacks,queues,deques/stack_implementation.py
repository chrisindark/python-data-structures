class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


s = Stack()
print(s.is_empty())

s.push(1)
s.push('two')
s.push(True)

print(s.size())
print(s.is_empty())

print(s.pop())
print(s.pop())
print(s.pop())

print(s.is_empty())
