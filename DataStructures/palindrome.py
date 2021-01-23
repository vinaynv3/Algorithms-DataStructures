"""
Palindrome - It is word sequence, that reads same forward & backward

"""

from deque import Deque
import sys

def Palindrome_checker(aString):
    
    status = True
    container = Deque()
    for char in aString:
        container.addFront(char)

    #print(len(container))
    
    if len(aString)%2 == 1 and  status:
        pos = 1
        
        while pos <= len(container)//2:
            if container.removeFront() == container.removeRear():
                pos +=1
            else:
                status = False
        return status
        
        
    else:
        pos = 1 
        while pos <= len(container)//2:
            if container.removeFront() == container.removeRear():
                pos +=1
            else:
                status = False
        return status


def main():

    word = sys.argv[-1]
    print(Palindrome_checker(word))

if __name__ == "__main__":
    main()

    
