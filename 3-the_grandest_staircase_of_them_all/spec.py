import unittest
from answer import answer


class Test(unittest.TestCase):

    def test_foobar_examples(self):

        self.assertEqual(answer(9), 7)
        self.assertEqual(answer(12), 14)
        self.assertEqual(answer(194), 338104629)


if __name__ == '__main__':

    unittest.main()