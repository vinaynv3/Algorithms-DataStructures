'''
Basic Algorithm

'''

def bubble_sort(alist):
    for i in range(len(alist)):
        for j in range(len(alist)):
            if alist[i] <= alist[j]:
                temp = alist[i]
                alist[i] = alist[j]
                alist[j] = temp
    return alist


print(bubble_sort([56,41,1,6,11]))
