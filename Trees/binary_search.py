"""
Binary Search implementation
"""

class BinarySearch:

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self,key,value):
        self.put(key,value)

    def put(self,key,val):

        if self.root is None:
            self.root = TreeNode(key,val)
        else:
            self._put(key,val,self.root)
        self.size +=1

    #Duplicate key bug
    def _put(self,current_node,key,val):

        if key < current_node.key:

            if current_node.hasLeftChild():
                self._put(key,val,current_node.leftC)
            else:
                current_node.leftC = TreeNode(key,val)
        else:
            if current_node.hasRightChild():
                self._put(key,val,current_node.rightC)
            else:
                current_node.rightC = TreeNode(key,val)

class TreeNode:

    def __init__(self,key,val,parent=None,left=None,right=None):
        self.key = key
        self.val = val
        self.parent = parent
        self.leftC = left
        self.rightC = right

    def hasLeftChild(self):
        return self.leftC

    def hasRightChild(self):
        return self.rightC

    def isLeftChild(self):
        return self.parent and self.parent.leftC == self

    def isRightChild(self):
        return self.parent and self.parent.rightC == self

    def isRoot(self):
        return not self.parent

    def isLeafNode(self):
        return not (self.leftC or self.rightC)

    def replaceNodeData(self,key,val,leftC=None,rightC=None):
        self.key = key
        self.val = val
        self.leftC = leftC
        self.rightC = rightC
        
        if self.hasLeftChild():
            self.leftC.parent == self
        else:
            self.rightC.parent == self

