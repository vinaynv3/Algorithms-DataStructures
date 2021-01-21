"""
Queue -  Linear Data structure

Above DS follows a principle called FIFO (First-in First-out), the oldest item in the queue 
will be processed first. Queue has two ends, one is at the rear, here item is added and another
end is at the front, where the item is removed.
Real-world cases: people standing in a queue to buy a movie ticket.
"""

#Implementation

class Queue:

    def __init__(self):
        self.alist = []

    def __len__(self):
        return len(self.alist)

    def __getitem__(self,position):
        return self.alist[position]

    def __setitem__(self,index,item):
        self.alist[index] = item

    def add(self, item):
        self.alist.append(item)

    def remove(self):
        return self.alist.pop(0)

    def __bool__(self):
        return self.alist == []


