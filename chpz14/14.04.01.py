"""The os module provides a function called walk that is similar to
this one but more versatile. Read the documentation and use it to
print the names of the files in a given directory and its subdirectories."""

import os

def walk_through(dirname):
    for root, dirs, files in os.walk(dirname):
        for name in files:
            print (os.path.join(root, name))
        for name in dirs:
            print (os.path.join(root, name))


walk_through("C:/Users/admin/PycharmProjects/Think_Python")

path = "C:/Users/admin/PycharmProjects/Think_Python"

for path, dirs, files in os.walk(path):
    print files

def walk2(dirname):
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print os.path.join(root, filename)

walk2("C:/Users/admin/PycharmProjects/Think_Python")


