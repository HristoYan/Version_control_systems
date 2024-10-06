import unittest


# def add(a: int, b: int ):
#     return a + b
#
#
# class TestAdd(unittest.TestCase):
#     def test_add_positive_num(self):
#         result = add(2, 3)
#         self.assertEqual(result, 5)
#
#     def test_add_negative_num(self):
#         result = add(-1, -1)
#         self.assertEqual(result, -2)
#
#     def test_add_zero(self):
#         result = add(0, 0)
#         self.assertEqual(result, 0)


# def is_even(n):
#     return n % 2 == 0


# class TestEvenFunction(unittest.TestCase):
#     def test_even_num(self):
#         self.assertTrue(is_even(4))
#
#     def test_odd_num(self):
#         self.assertFalse(is_even(3))


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def revers_string(s: str):
    return s[::-1]


class TestReversString(unittest.TestCase):
    def test_str(self):
        self.assertEqual(revers_string('hello'), 'olleh')

    def test_empty_str(self):
        self.assertEqual(revers_string(''), '')

    def test_char(self):
        self.assertEqual(revers_string('c'), 'c')


# class TestPrimeFunction(unittest.TestCase):
#     def test_prime(self):
#         self.assertTrue(is_prime(13))
#
#     def test_not_prime(self):
#         self.assertFalse(is_prime(4))
#
#     def test_one_is_not_prime(self):
#         self.assertFalse(is_prime(1))
#
#     def test_two_is_prime(self):
#         self.assertTrue(is_prime(2))


if __name__ == '__main__':
    unittest.main()

