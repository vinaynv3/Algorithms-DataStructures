"""
Shell Sort
"""

def shell_sort(alist):

    sub_list = len(alist)//2

    while sub_list > 0:

        for start in range(sub_list):
            gapInsertionSort(alist,start,sub_list)

            print("SIZE ",sub_list,"\n",alist)

        sub_list = sub_list//2

def gapInsertionSort(alist,start,gap):

    for index in range(start+gap,len(alist),gap):

        current_value = alist[index]
        position = index

        while position >= gap and alist[position-gap] > current_value:

            alist[position] = alist[position-gap]
            position -= gap

        alist[position] = current_value


def main():
    alist = [54,26,93,17,77,31,44,55,20]
    print(shell_sort(alist))

if __name__ == "__main__":
    main()
