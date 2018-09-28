def binary_tree(r):
    return [r, [], []]
    pass


def insert_left(root, new_node):
    a = root.pop(1)

    if len(a) > 1:
        root.insert(1, [new_node, a, []])
    else:
        root.insert(1, [new_node, [], []])

    return root


def insert_right(root, new_node):
    a = root.pop(2)

    if len(a) > 1:
        root.insert(2, [new_node, [], a])
    else:
        root.insert(2, [new_node, [], []])

    return root


def get_root(r):
    return r[0]


def set_root(r, val):
    r[0] = val


def get_left_node(r):
    return r[1]


def get_right_node(r):
    return r[2]


r = binary_tree(3)
print(r)
r = insert_left(r, 4)
print(r)
r = insert_left(r, 5)
print(r)
r = insert_right(r, 6)
print(r)
r = insert_right(r, 7)
print(r)
