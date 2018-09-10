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
    if re.match(r"^\d*[.]\d+$", value):
        return True
    else:
        return False

alist = ["Hello", "Hello", "Bob"]
stringCount(alist)
numFloat = isFloat("2.30")
print(numFloat)
numFloat = isFloat("2")
print(numFloat)
