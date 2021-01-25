"""
Unordered linked list
"""

class Node:

    def __init__(self,item):
        self.Node = item
        self.Next = None

    def getNode(self):
        return self.Node

    def getNext(self):
        return self.Next

    def setNode(self,newItem):
        self.Node = newItem

    def setNext(self,newNext):
        self.Next = newNext


class UnorderedLinkedList:

    def __init__(self):
        self.head = None


    def __bool__(self):
        return self.head == None

    def addNode(self,item):

        if self.head is None:
            self.head = Node(item)

        else:
            current_nodes = self.head
            self.head = Node(item)
            self.head.setNext(current_nodes)

    def __len__(self):

        if bool(self):
            return 0

        else:
            current = self.head
            total_length = 0
            while current != None:
                total_length +=1
                current = current.getNext()
            return total_length

    def __contains__(self,item):

        current = self.head
        status = False
        position = 0

        while position < len(self) and not status:

            print(current.getNode(),item,position)
            if current.getNode() == item:
                status = True
            else:
                current = current.getNext()
            position +=1
        return status

    def remove(self,item):
        
        current = self.head
        previous = None
        position = 0
        found = False

        while not found and current != None:

            if current.getNode() == item:
                found = True

            else:
                previous = current
                current = current.getNext()    

        if previous is None:
            self.head = current.getNext()

        elif current == None:
            return None
        
        else:
            self.head = previous
            self.head.setNext(current.getNext())
    


class OrderedLinkedList(UnorderedLinkedList):

    def __init__(self):
        UnorderedLinkedList.__init__(self)

    def addNode(self,item):
        
        if self.head is None:
            self.head = Node(item)

        else:
            previous = None
            stop = False
            current = self.head

            while not stop and current != None:
                if item <= current.getNode():
                    stop = True
                else:
                    previous = current
                    current = current.getNext()
            
            if previous is None:
                self.head = Node(item)
                self.head.setNext(current)

            else:
                previous.setNext(Node(item))
                previous.getNext().setNext(current)
                
    















