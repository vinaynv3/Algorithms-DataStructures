"""
Quick sort implementatiion
"""

def quick_sort(alist):
    quick_sort_helper(alist,0,len(alist)-1)
    return alist

def pivot_indexer(alist):
    print(alist)
    mid = len(alist)//2
    new_list = [alist[0],alist[mid],alist[len(alist)-1]]
    pivot_list =  sorted(new_list)
    return alist.index(pivot_list[1])


def quick_sort_helper(alist,first,last):

    if first < last:

        split_point = partition(alist,first,last)
        quick_sort_helper(alist,first,split_point-1)
        quick_sort_helper(alist,split_point+1,last)



def partition(alist,first,last):

    pivot_index = first
    #print(pivot_index, alist[pivot_index])
    left_mark = first+1
    right_mark = last

    while left_mark <= right_mark:

        if alist[left_mark] < alist[pivot_index] and  alist[right_mark] > alist[pivot_index]:
            left_mark +=1
            right_mark -=1

        elif alist[left_mark] > alist[pivot_index]:

            if alist[right_mark] < alist[pivot_index]:
                alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]
                left_mark +=1
                right_mark -=1
            else:
                right_mark -=1


        elif alist[right_mark] < alist[pivot_index] :

            if alist[left_mark] > alist[pivot_index]:
                alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]
                left_mark +=1
                right_mark -=1
            else:
                left_mark +=1
    

    if left_mark > right_mark:
        alist[pivot_index] ,alist[right_mark] = alist[right_mark], alist[pivot_index] 

    return right_mark


def main():
    alist = [54,26,93,17,77,31,44,55,20]
    #print(pivot_index(alist))
    print(quick_sort(alist))

if __name__ == "__main__":
    main()
