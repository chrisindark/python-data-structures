import os

path = '/Users/christopherpaul'
files = []
# print(os.stat(path))
# print(os.listdir(path))


def list_directory(path):
    return os.listdir(path)


def is_big_image(path):
    """
    return True if file at the given path is png and is at least 5mb
    :param path:
    :return: True or False
    """
    if path.endswith('png') or path.endswith('jpg'):
        try:
            statinfo = os.stat(path)
            return statinfo.st_size > 5 * 1024 * 1024
        except OSError:
            return False
    return False


def recurse_directory(path):
    for i in list_directory(path):
        # print(i)
        # print(os.path.join(path, i))
        # os.path.isfile(os.path.join(path, i))
        if os.path.isfile(os.path.join(path, i)):
            if is_big_image(os.path.join(path, i)):
                files.append(os.path.join(path, i))
        elif os.path.isdir(os.path.join(path, i)):
            recurse_directory(os.path.join(path, i))
        else:
            print('dont know what this path contains: ', path)


recurse_directory(path)

print(files)
