import unittest


def calc_total_price(prices: list[int], discount: int):
    if not 0 <= discount <= 100:
        raise ValueError('Discount must be between 1% and 100%')
    total = sum(prices)

    return total * (1 - discount / 100)


class TestCalcTotalPrice(unittest.TestCase):
    # test regular discount
    def test_discount(self):
        self.assertEqual(calc_total_price([50, 50], 20), 80)

    # test no discount
    def test_no_discount(self):
        self.assertEqual(calc_total_price([50, 50, 50], 0), 150)

    # test full discount
    def test_full_discount(self):
        self.assertEqual(calc_total_price([50, 50], 100), 0)

    # test invalid discount < 100%
    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            calc_total_price([50, 50], 110)

    # test empty cart
    def test_empty_cart(self):
        self.assertEqual(calc_total_price([], 90), 0)




if __name__ == '__main__':
    unittest.main()