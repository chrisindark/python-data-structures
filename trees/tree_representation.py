class BinaryTree(object):
    def __init__(self, root):
        self.root = root
        self.left_node = None
        self.right_node = None
        pass

    def insert_left(self, root):
        if self.left_node is None:
            self.left_node = BinaryTree(root)
        else:
            a = BinaryTree(root)
            a.left_node = self.left_node
            self.left_node = a

    def insert_right(self, root):
        if self.right_node is None:
            self.right_node = BinaryTree(root)
        else:
            a = BinaryTree(root)
            a.right_node = self.right_node
            self.right_node = a

    def get_left_node(self):
        return self.left_node

    def get_right_node(self):
        return self.right_node

    def get_root_node(self):
        return self.root

    def set_root_node(self, root):
        self.root = root


r = BinaryTree('a')
print(r)
a = r.get_root_node()
print(a)
r.insert_left('b')
a = r.get_left_node()
print(a)
