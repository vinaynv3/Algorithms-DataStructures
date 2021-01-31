
import unittest 

def sequential_search(alist,item):

    if item in alist:
        return True
    else:
        return False

class SequenceTest(unittest.TestCase):

    def test_find_item_in_sequence(self):
        self.assertTrue(sequential_search([1,2,3,4],4),True)


    def test_find_item_NotFound_in_sequence(self):
        self.assertFalse(sequential_search([1,2,3,4],5),False)

if __name__ == "__main__":
    unittest.main()

