import unittest
from basic import the_generator, the_odd_even_gen, Mode


class MyTestCase(unittest.TestCase):
    MAX_VAL = 100

    def test_basic(self):
        expected = list(range(self.MAX_VAL))
        actual = list(the_generator(self.MAX_VAL))
        self.assertEqual(expected, actual)

    def test_even(self):
        expected = list(range(2, self.MAX_VAL, 2))
        actual = list(the_odd_even_gen(Mode.EVEN, self.MAX_VAL))
        self.assertEqual(expected, actual)

    def test_odd(self):
        expected = list(range(1, self.MAX_VAL))
        actual = list(the_odd_even_gen(Mode.ODD, self.MAX_VAL))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
