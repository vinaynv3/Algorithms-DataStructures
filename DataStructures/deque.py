"""
Deque - Data structure

This container is a combination of stack & queue, the elements can be added both ends 
and can removed at both front & rear
"""

class Deque:

    def __init__(self):
        self.alist = []

    def __bool__(self):
        return self.alist == []
        

    def __str__(self):
        return self.alist

    def __len__(self):
        return len(self.alist)

    def __getitem__(self, position):
        return self.alist[position]

    def __setitem__(self,index,item):
        self.alist[index] = item

    def addFront(self,item):
        self.alist.insert(0,item)

    def addRear(self,item):
        self.alist.append(item)

    def removeFront(self):
        return self.alist.pop(0)

    def removeRear(self):
        return self.alist.pop()


