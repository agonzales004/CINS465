#!/usr/bin/env python
from collections import defaultdict
import collections
import re

#Part 1 of assignment
#adapted from example found on https://www.quora.com/How-do-I-convert-a-list-into-a-dictionary-in-python
#and https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
def stringCount(list):
    set = collections.Counter(list)
    for key in sorted(set.iterkeys()):
        print "%s: %s" % (key, set[key])

#Part 2 of assignment
def isFloat(value):
    if re.match(r"^[+]?[-]?\d*[.]\d+$", value):
        return True
    else:
        return False

#Part 3 of assignment
#Code adapted from https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, nData):
        new_node = Node(nData)
        new_node.set_next(self.head)
        self.head = new_node

    def delete(self, nData):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == nData:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Value ",nData," not found")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def printLL(self):
        sData = ""
        current = self.head
        while current:
            sData+=str(current.get_data())
            sData+=" "
            current = current.get_next()
        print(sData)

    def search(self, nData):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == nData:
                found = True
                return found
            else:
                current = current.get_next()
        if current is None:
            return found

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

#Node class adapted from https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
