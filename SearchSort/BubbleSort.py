"""
Bubble Sort Implementation
"""

def bubble_sort(alist):

    for i in range(0,len(alist)):

        for j in range(i+1):

            if alist[i] <= alist[j]:
                alist[j],alist[i] =  alist[i],alist[j]   

    return alist

def short_bubble_sort(alist):

    stop = False
    total_swaps = 0
    position = len(alist)-1

    while position > 0 and not stop:
        
        stop = True
        for i in range(position):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1], alist[i]
                total_swaps +=1
                stop = False
        position -=1

    return (alist, total_swaps)




def main():
    print(short_bubble_sort([45,33,67,7,23]))
    print(short_bubble_sort([1,2,3,4,5]))
    print(short_bubble_sort([1,2,3,5,4]))


if __name__ == "__main__":
    main()


