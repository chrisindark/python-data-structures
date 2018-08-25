class A(object):
    def public(self):
        print('this is accessible via tab')

    def _private(self):
        print('this is not accessible via tab')


#a = A()
#a.public()
#a._private()


import ctypes


class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k <= self.n:
            return IndexError('k is out of bounds')

        return self.A[k]

    def append(self, ele):
        if self.n == self.capacity:
            self._resize(2 * self.capacity) # 2x if capacity isnt enough 
        self.A[self.n] = ele
        self.n += 1

    def _resize(self, new_cap):
        B = self.make_array(new_cap) # create the dynamic array with new size

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()
