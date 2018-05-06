import unittest
from answer import answer


class Test(unittest.TestCase):

    def test_foobar_examples(self):
        self.assertEqual(answer(5, 3), [[0, 1, 2, 3, 4, 5], [0, 1, 2, 6, 7, 8], [0, 3, 4, 6, 7, 9], [1, 3, 5, 6, 8, 9], [2, 4, 5, 7, 8, 9]])
        self.assertEqual(answer(4, 4), [[0], [1], [2], [3]])
        self.assertEqual(answer(2, 1), [[0], [0]])


if __name__ == '__main__':

    unittest.main()