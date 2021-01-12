"""
Linear data structure - stack
"""

class Stack:

    def __init__(self):
        self.alist = []

    
    def __repr__(self):
        return "Stack({0})".format(self.alist)
    
    def isEmpty(self):
        return len(self.alist) == 0

    def __len__(self):
        return len(self.alist)


    def __getitem__(self,position):
        return self.alist[position]

    def add(self,value):
        self.alist.append(value)


    def remove(self):
        self.alist.pop()


        
