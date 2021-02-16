"""
Binary Heap implementation
"""

class binary_heap:

    def __init__(self):
        self.heap_list = [0]

    def __len__(self):
        return len(self.heap_list)

    def insert(self,item):
        self.heap_list.append(item)
        if len(self) > 2:
            self.prelocate_up()

    def prelocate_up(self):
        size = len(self)-1

        while size//2 > 0:

            if self.heap_list[size] < self.heap_list[size//2]:
                self.heap_list[size],self.heap_list[size//2] =  self.heap_list[size//2],self.heap_list[size]
            
            size = size//2

    def getHeapList(self):
        return self.heap_list

    def del_min(self):
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list.pop()
        print(self.heap_list)
        self.prelocate_down(1)
        return min_val

    def prelocate_down(self,index):
        
        size = len(self)-1
        pos = index

        while pos* 2 <= size:

            minChild = self.min_child(pos)
            #print(minChild)

            if self.heap_list[pos] > self.heap_list[minChild]:
                self.heap_list[pos], self.heap_list[minChild] = self.heap_list[minChild], self.heap_list[pos]

            pos = minChild
                

    def min_child(self, pos):

        if pos*2+1 > len(self)-1:
            return 2*pos

        if self.heap_list[2*pos] < self.heap_list[2*pos+1]:
            return 2*pos

        return 2*pos+1

    def addList(self,alist):
        
        if len(self) is 1:
            self.heap_list += alist

    def heap(self):

        mid_point = len(self)//2

        while mid_point > 0:
            self.prelocate_down(mid_point)
            mid_point = mid_point-1


def main():
    alist = [5,9,11,14,18,19,21,33,17,27]
    
    #p_q => priority queue
    p_q = binary_heap()

    for val in alist:
        p_q.insert(val)

    p_q.insert(7)


    print(p_q.del_min())
    print(p_q.getHeapList())
    p_q.heap()
    print(p_q.getHeapList())

def heap_tester():
    alist = [9, 6, 5, 2, 3] 

    p_q = binary_heap()
    p_q.addList(alist)
    p_q.heap()
    print(p_q.getHeapList())
if __name__ == "__main__":
    main()
    #heap_tester()



                
