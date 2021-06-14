import os

def listup(path, depth = 0):
    indent = ' '*depth
    print(indent + 'Now in {}'.format(path))

    for entry in os.listdir(path):
        fullpath = os.path.join(path, entry)
        if os.path.isdir(fullpath):
            listup(fullpath, depth + 1)
        else:
            print(indent + 'Found{}'.format(fullpath))
    print(indent + 'Leave {}'.format(fullpath))

listup('.')

