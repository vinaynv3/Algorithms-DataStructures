"""

Tree Traversal
1.Pre-order
2.In-order
3.Post-order
"""
import random
from BinaryTree import binary_tree

def pre_order(btree):

    if btree != None:
        print(btree.getRoot())
        pre_order(btree.left)
        pre_order(btree.right)


def post_order(btree):

    if btree != None:
        pre_order(btree.left)
        pre_order(btree.right)
        print(btree.getRoot())


def in_order(btree):

    if btree != None:
        pre_order(btree.left)
        print(btree.getRoot())
        pre_order(btree.right)


def main():

    btree = binary_tree(1)

    left = btree.addLeft
    right = btree.addRight

    side = 0

    for i in range(2,8):

        if side is 0:
            left(i)
            side = 1
        else:
            right(i)
            side = 0
    
    print("PRE-ORDER")
    pre_order(btree)
    print("IN-ORDER")
    in_order(btree)
    print("POST-ORDER")
    post_order(btree)


if __name__ == "__main__":
    main()






