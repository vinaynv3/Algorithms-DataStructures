"""
Hash Table
  -> it is a container, where each item is stored in hash table slot. The slot is allocated to an
     item through hash function.
  -> The following uses collision technique called chaning

"""

import sys
import os

sys.path.insert(1,os.getcwd().split('/S')[0]+"/DataStructures/")

from linkedlist import UnorderedLinkedList as chain

class HashTable:

    def __init__(self, size):
        self.table = [None] * size

    def hash_function(self, item):

        if type(item) == int:
            slot = item % len(self.table)
            return slot

        elif type(item) == str:
            ord_list = [ ord(char) for char in item]

            slot = sum(ord_list) % len(self.table)
            return slot
        
        else:
            return None

    def __contains__(self,item):
        hash_value = self.hash_function(item)
        slot = self.table[hash_value]
        
        if item in slot:
            return True
        else:
            return False


    def put(self, item):

        if not all(self.table):
            hash_value = self.hash_function(item)

            if self.table[hash_value] != None:
                slot = self.table[hash_value]
                slot.addNode(item)
                self.table[hash_value] = slot

            else:
                slot = chain()
                slot.addNode(item)
                self.table[hash_value] = slot
        else:
            return "HashTable is FULL!"

    def __len__(self):
        return len(self.table)

    def __getitem__(self,position):
        return self.table[position]

    def total_values_in_position(self):
        #print(len(self))
        val_pos_list = [len(value) for value in self.table if value is not None]
        return val_pos_list




def main():
    hash_table = HashTable(11)
    alist = [77, 44, 55, 20, 26, 93, 17, 31, 54]
    for num in alist:
        hash_table.put(num)

    
    print("List: ",alist)
    print("size ",hash_table.total_values_in_position())

    
    
if __name__ == "__main__":
    main()

