"""
Dynamic programming : It is strategy used in algorithms by creating 
sub-solution to the problem of a state or in simpler terms breaking a
problem into smaller sub-problems, find a solution sub-problems

Ex: Fibnacci sequence, it status the a value in a sequence is sum of two
    previous numbers and the sequence begins with values 1,1 at positions
    0,1

"""
import sys
#Below function uses memoziation technique

class fib:

    def __init__(self):
        self.memo = {}

    def fib(self,n):

        if n in self.memo:
            return self.memo[n]

        elif n == 1 or n == 2:
            self.memo[n] = 1
            return 1

        else:
            print("recursion @ ",n)
            result = self.fib(n-1) + self.fib(n-2)
            self.memo[n] = result
            return result

def main():
    f = fib()
    print(f.fib(int(sys.argv[-1])))

if __name__ == "__main__":
    main()
