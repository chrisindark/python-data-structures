class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        # self.items.append(item)
        self.items.insert(0, item)

    def dequeue(self):
        # item = self.items[:1][0]
        # self.items = self.items[1:len(self.items)]
        # return item
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
print(q.is_empty())

q.enqueue(1)
q.enqueue('two')
q.enqueue(True)

print(q.size())
print(q.is_empty())

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

print(q.is_empty())
