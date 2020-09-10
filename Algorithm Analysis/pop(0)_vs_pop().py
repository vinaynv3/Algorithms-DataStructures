"""

Below functions remove data item from an array at the end & beggining in a given list.
The pop() operation in each function takes variable time to perform a given tas.k
f(alist) = lamda x:alist.pop()  #constant time o(1)
f(alist) = lamda x:alist.pop(0) #linear time o(n)

"""

from timeit import Timer
#o(n)
def func_pop_start(alist_length):
    l = list(range(alist_length))
    l.pop(0)

#o(1)
def func_pop_end(alist_length):
    l = list(range(alist_length))
    l.pop()



for value in range(1000000,10000001,100000):

    #pop(0) time analysis
    f1 = func_pop_start(value)
    pop_start = Timer("f1","from __main__ import f1")
    print("o(n): ",pop_start.timeit(number = 100), " mili_sec")

    #pop() time analysis
    f2 = func_pop_end(value)
    pop_end = Timer("f2","from __main__ import f2")
    print("o(1): ",pop_end.timeit(number = 100), " mili_sec\n")
