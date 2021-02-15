"""
Merge Sort
"""

def merge_sort(alist):

    if len(alist) > 1:
        """
        Recursion implementaion
        """
        mid_point = len(alist)//2
        left = alist[:mid_point]
        right = alist[mid_point:]

        merge_sort(left)
        merge_sort(right)

        i,j,k = (0,0,0)

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                alist[k] = right[j]
                j += 1
            else:
                alist[k] = left[i]
                i +=1
            k +=1

        while i < len(left):
            alist[k] = left[i]
            i += 1
            k +=1

        
        while j < len(right):
            alist[k] = right[j]
            j += 1
            k +=1

        print("Merging...", alist)
    
    return alist

def main():
    alist = [54,26,93,17,77,31,44,55,20]
    print(merge_sort(alist))

if __name__ == "__main__":
    main()


