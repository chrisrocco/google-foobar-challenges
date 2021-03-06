import unittest
from answer import answer


class Test(unittest.TestCase):

    def test_foobar_examples(self):

        self.assertEqual(
            answer([[True, False, True], [False, True, False], [True, False, True]]),
            4
        )

        self.assertEqual(
            answer([
                [True, True, False, True, False, True, False, True, True, False],
                [True, True, False, False, False, False, True, True, True, False],
                [True, True, False, False, False, False, False, False, False, True],
                [False, True, False, False, False, False, True, True, False, False]
            ]),
            11567
        )

        self.assertEqual(
            answer([
                [True, False, True, False, False, True, True, True],
                [True, False, True, False, False, False, True, False],
                [True, True, True, False, False, False, True, False],
                [True, False, True, False, False, False, True, False],
                [True, False, True, False, False, True, True, True]
            ]),
            254
        )

        # This is the maximum input size tested by Google Foobar
        self.assertEqual(
            answer([
                [True, True, False, True, False, True, False, True, True, False, True, True, False, True, False, True, False, True, True, False, True, True, False, True, False, True, False, True, True, False, True, True, False, True, False, True, False, True, True, False, True, True, False, True, False, True, False, True, True, False],
                [True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False],
                [True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False],
                [True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False],
                [True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False],
                [True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False],
                [True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, True, True, False],
                [True, True, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, False, False, True],
                [False, True, False, False, False, False, True, True, False, False, False, True, False, False, False, False, True, True, False, False, False, True, False, False, False, False, True, True, False, False, False, True, False, False, False, False, True, True, False, False, False, True, False, False, False, False, True, True, False, False]
            ]),
            737432225562708231147631690L
        )


if __name__ == '__main__':
    unittest.main()
