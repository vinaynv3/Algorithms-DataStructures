"""
The program visiluzes data item look-up analyzes performace between dictonary & List datastructure

"""

import random
import matplotlib.pyplot as plt
from timeit import Timer

list_data = []
dict_data = []
x_axis = [i for i in range(1,11)]

for val in range(10000,100001,10000):

    alist = list(range(val))
    dict = {i:None for i in range(val+1)}

    #Timer objects
    t1 = Timer("random.randrange({0}) in alist".format(val), "from __main__ import random, alist" )
    list_data.append(t1.timeit(number = 1000))

    t2 = Timer("dict[random.randrange({0})]".format(val), "from __main__ import random, dict" )
    dict_data.append(t2.timeit(number = 1000))


#Data visualization

fig, axs = plt.subplots()

axs.set(ylabel = 'millisec',
        xlabel = 'Index',
        title = 'List & Dict look-up speed')

axs.plot(x_axis,list_data,
        x_axis,list_data,"oy",
        x_axis,dict_data,
        x_axis,dict_data,"or")

plt.show()
