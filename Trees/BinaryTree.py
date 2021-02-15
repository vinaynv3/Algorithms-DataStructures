"""

Binary tree implementation

"""

class binary_tree:

    def __init__(self,root):
        self.root = root
        self.left  = None
        self.right = None

    def addLeft(self,val):

        if self.left is None:
            self.left = binary_tree(val)

        else:
            temp = binary_tree(val)
            temp.left = self.left
            self.left = temp
     

    def addRight(self,val):

        if self.right is None:
            self.right = binary_tree(val)

        else:
            temp = binary_tree(val)
            temp.right = self.right
            self.right = temp
     

    def getRoot(self):
        return self.root

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setRoot(self,val):
        self.root = val
