import unittest
from Main import get_number, get_empty_list, get_index

class Test_2048(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_number(1, 2), 7)
    def test_2(self):
        self.assertEqual(get_number(3, 3), 16)
    def test_3(self):
        a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas=[
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
        self.assertEqual(get_empty_list(mas), a)
    def test_4(self):
        a=[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas=[
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
    def test_5(self):
        self.assertEqual(get_index(7), (1,2))
    def test_6(self):
        self.assertEqual(get_index(16), (3,3))  
    def test_7(self):
        self.assertEqual(get_index(1), (0,0))  
    def test_8(self):
        self.assertEqual(get_index(2), (0,1))  
if __name__ == '__main__':
    unittest.main()
