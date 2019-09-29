import unittest
import fibboaaci

class TestLastDigitOfFibonacciNumber(unittest.TestCase):
    def test_small(self):
        for n in range(20):
            self.assertEqual(last_digit_of_fibonacci_number_naive(n),
                             last_digit_of_fibonacci_number(n))

    def test_large(self):
        for (n, last_digit) in [(100, 5), (139, 1), (91239, 6), (170, 5)]:
            self.assertEqual(last_digit_of_fibonacci_number(n), last_digit)


if __name__ == '__main__':
    unittest.main()