import unittest
from Extra_Credit import isSorted, bogoSort, brickSort

class TestExtraCredit(unittest.TestCase):
    
    def test_isSorted(self):
        self.assertTrue(isSorted([1, 2, 3, 4, 5]))
        self.assertFalse(isSorted([5, 1, 2, 3, 4]))
        
    def test_bogoSort(self):
        lst = [1, 2, 3]  # Very small list to ensure quick sorting
        bogoSort(lst)
        self.assertTrue(isSorted(lst))
        
        lst = [3, 2, 1]  # Reverse sorted small list
        bogoSort(lst)
        self.assertTrue(isSorted(lst))

    def test_brickSort(self):
        lst = [5, 1, 4, 2, 8]
        brickSort(lst)
        self.assertTrue(isSorted(lst))

        lst = [10, 22, 5, 75, 65, 80]
        brickSort(lst)
        self.assertTrue(isSorted(lst))

        lst = [1, 2, 3, 4, 5]  # Already sorted
        brickSort(lst)
        self.assertTrue(isSorted(lst))

        lst = [5, 4, 3, 2, 1]  # Reverse order
        brickSort(lst)
        self.assertTrue(isSorted(lst))

if __name__ == '__main__':
    unittest.main()
