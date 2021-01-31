

def BinarySearch(alist,item):
    
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:

        mid_point = (first+last)//2
        #print(mid_point, alist[mid_point])

        if alist[mid_point] == item:
            found = True

        else:
            if item < alist[mid_point]:
                last = mid_point-1
    
            else:
                first = mid_point+1
                

        print("List ",alist)

    return found

def BinarySearchRecur(alist,item):

    first = 0
    last = len(alist)-1
    mid = (first+last)//2

    #print(alist[mid], mid, len(alist))

    if len(alist) == 0:
        #print("DEBUG")
        return False

    else:
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                return BinarySearchRecur(alist[:mid],item)
            else:
                return BinarySearchRecur(alist[mid+1:],item)


def main():

    alist = [1,2,3,4,5]
    for i in range(1,7):
        print(i, BinarySearchRecur(alist,i))

if __name__ == "__main__":
    main()

