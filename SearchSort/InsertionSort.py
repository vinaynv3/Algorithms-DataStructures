"""
Insertion Sort
"""

def Insertion_Sort(alist):

    for index in range(1,len(alist)):

        current_value = alist[index]
        pos = index
        
        while pos > 0 and alist[pos-1] > current_value:
            alist[pos] = alist[pos-1]
            pos -= 1

        alist[pos] = current_value

    return alist




def main():

    alist = [45,33,67,55,4,89,21]
    print(Insertion_Sort(alist))

if __name__ == "__main__":
    main()


