import unittest
from answer import answer


class Test(unittest.TestCase):

    def test_foobar_examples(self):
        self.assertEqual(answer('4'), 2)
        self.assertEqual(answer('15'), 5)
        self.assertEqual(answer('1' * 309), 5)


if __name__ == '__main__':

    unittest.main()