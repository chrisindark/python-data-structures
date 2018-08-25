class Queue2Stacks(object):
    def __init__(self):
        self.stack1 = [] #  use for stacking enqueues
        self.stack2 = [] #  use for dequeues

    def enqueue(self, item):
        # for i in range(self.size(2)):
        #     self.push(1, self.pop(2))
        # self.push(1, item)
        #
        # for i in range(self.size(1)):
        #     self.push(2, self.pop(1))

        self.stack1.append(item)

    def dequeue(self):
        # return self.pop(2)
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def is_empty(self, i):
        if i == 1:
            return self.stack1 == []
        return self.stack2 == []

    def size(self, i):
        if i == 1:
            return len(self.stack1)
        return len(self.stack2)

    def push(self, i, item):
        if i == 1:
            return self.stack1.append(item)
        return self.stack2.append(item)

    def pop(self, i):
        if i == 1:
            return self.stack1.pop()
        return self.stack2.pop()

    def log_stack(self, i):
        if i == 1:
            return print(self.stack1)
        return print(self.stack2)


q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)

# q.log_stack(1)
# q.log_stack(2)

for i in range(3):
    print(q.dequeue())

# q.log_stack(1)
# q.log_stack(2)

for i in range(2,5):
    q.enqueue(i)

# q.log_stack(1)
# q.log_stack(2)

for i in range(5):
    print(q.dequeue())

# q.log_stack(1)
# q.log_stack(2)
