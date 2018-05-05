import unittest
import answer

class Test(unittest.TestCase):

    def test_foobar_examples(self):
        self.assertEqual(answer.answer(0, 3), 2)
        self.assertEqual(answer.answer(17, 4), 14)

if __name__ == '__main__':
    unittest.main()