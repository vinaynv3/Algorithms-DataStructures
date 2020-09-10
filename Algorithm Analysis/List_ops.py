
"""
List - Non linear python data structure
Analysis of list operations execution time using timit module
"""


#class implements list operations

class list_operations(object):

    #constructor
    def __init__(self):
        self.alist = None

    #Below methods implement list operations
    #concatination
    def list_concat(self,num):

        self.alist = []
        for i in range(num):
            self.alist = self.alist + [i]

    #Append
    def list_append(self,num):

        self.alist = []
        for i in range(num):
            self.alist.append(i)

    #list_comphrension
    def list_comphrension(self,num):
        self.alist = [i for i in range(num)]

    #list class
    def list_constructor_with_range_func(self,num):
        self.alist = list(range(num))

    def list_size(self):
        return len(self.alist)

"""
timeit module analyzes execution time on each list_operations methods
"""

from timeit import Timer

if __name__ == "__main__":

    #class list_operations instantion
    num = 1000
    list_instance = list_operations()

    #class list_operations methods
    concat = list_instance.list_concat(num)
    append = list_instance.list_append(num)
    list_comphrension = list_instance.list_comphrension(num)
    list_range = list_instance.list_constructor_with_range_func(num)

    #timer objects
    t1 = Timer("concat","from __main__ import concat")
    print("Concat", t1.timeit(number = 10000), " mili_sec")

    t1 = Timer("append","from __main__ import append")
    print("Append", t1.timeit(number = 10000), " mili_sec")

    t1 = Timer("list_comphrension","from __main__ import list_comphrension")
    print("list_comphrension", t1.timeit(number = 10000), " mili_sec")

    t1 = Timer("list_range","from __main__ import list_range")
    print("list_range", t1.timeit(number = 10000), " mili_sec")
