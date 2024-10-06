import unittest


def convert_temperature(temp: float, scale: str):
    if scale == 'C':
        return (temp - 32) * (5 / 9)
    elif scale == 'F':
        return temp * 9 / 5 + 32
    else:
        raise ValueError('Unknown scale: use "C" or "F"')


print(convert_temperature(-40.0, 'F'))


class TestConvertTemp(unittest.TestCase):
    # conv C to F
    def test_c_to_f(self):
        self.assertEqual(convert_temperature(40.0, 'F'), 104.0)

    # conv F to C
    def test_f_to_c(self):
        self.assertEqual(convert_temperature(32.0, 'C'), 0.0)

    # test invalid scale
    def test_invalid_scale(self):
        with self.assertRaises(ValueError):
            convert_temperature(32.0, 'B')

    # edge case -40C
    def test_c_to_f_edge(self):
        self.assertEqual(convert_temperature(-40.0, 'F'), -40.0)

    # def test_f_to_c_edge(self):
    #     self.assertEqual(convert_temperature(-40.0, 'C'), -40.0)


if __name__ == '__main__':
    unittest.main()
