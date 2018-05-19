import unittest
import answer as me

class Test(unittest.TestCase):

    def test_foobar_examples(self):
        self.assertEqual(me.answer(
            (3, 2),
            (1, 1),
            (2, 1),
            4
        ), 7)

        self.assertEqual(me.answer(
            (300, 275),
            (150, 150),
            (185, 100),
            500
        ), 9)

if __name__ == '__main__':
    unittest.main()