"""
Selection sort 
"""

def selection_sort(alist):

    for val in range(len(alist)-1,0,-1):
        
        current_max = val
        for j in range(val):

            if alist[j] > alist[current_max]:
                current_max = j

        alist[val], alist[current_max] = alist[current_max], alist[val]

    return alist

def main():

    alist = [45,33,67,55,4,89,21]
    print(selection_sort(alist))

if __name__ == "__main__":
    main()


