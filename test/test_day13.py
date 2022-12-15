import unittest

from day13 import is_in_the_right_order


class TestCases(unittest.TestCase):
    def test_is_in_right_order_1(self):
        self.assertTrue(is_in_the_right_order([1,1,3,1,1], [1,1,5,1,1])[1])

    def test_is_in_right_order_2(self):
        self.assertTrue(is_in_the_right_order([[1],[2,3,4]], [[1],4])[1])

    def test_is_in_right_order_3(self):
        self.assertFalse(is_in_the_right_order([9], [[8,7,6]])[1])

    def test_is_in_right_order_4(self):
        self.assertTrue(is_in_the_right_order([[4,4],4,4], [[4,4],4,4,4])[1])

    def test_is_in_right_order_5(self):
        self.assertFalse(is_in_the_right_order([7,7,7,7], [7,7,7])[1])

    def test_is_in_right_order_6(self):
        self.assertTrue(is_in_the_right_order([], [3])[1])

    def test_is_in_right_order_7(self):
        self.assertFalse(is_in_the_right_order([[[]]], [[]])[1])

    def test_is_in_right_order_8(self):
        self.assertFalse(is_in_the_right_order([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9])[1])

    def test_is_in_right_order_9(self):
        self.assertFalse(is_in_the_right_order([8,8,4,6], [8,8,4,6])[1])

    def test_is_in_right_order_10(self):
        self.assertTrue(is_in_the_right_order([[], [10, 3, 10, 9]], [[[7]], []])[1])

    def test_is_in_right_order_11(self):
        self.assertTrue(is_in_the_right_order([[3,1,2,10,1],[7,[[3,5,9]]],[5,[1],6,3],[3,[[],1,1,9,[4]]]], [[[[3,7,9,7]],[[],6,7,2],[],[[5],3,[2,4,5,9,7],[6]]],[[8,2,7,3,[]],5],[[3,7,[0],1,5],8],[[],[[6,6,3,1],6,[3],10,3],[[5],[2,2,7,1,5],0],0]])[1])

    def test_is_in_right_order_15(self):
        self.assertTrue(is_in_the_right_order([3], [[3, 7, 9, 7]])[1])


