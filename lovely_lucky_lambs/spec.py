import unittest
import answer

class Test(unittest.TestCase):

    def test_foobar_examples(self):
        self.assertEqual(answer.answer(10), 1)
        self.assertEqual(answer.answer(143), 3)
        self.assertEqual(answer.answer(1), 0)

if __name__ == '__main__':
    unittest.main()