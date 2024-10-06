import re
import unittest


def is_valid_email(email: str):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None


class TestValidEmail(unittest.TestCase):
    # test valid
    def test_valid_email(self):
        self.assertTrue(is_valid_email('hristo@gmail.com'))

    # test invalid missing @
    def test_invalid_missing_at(self):
        self.assertFalse(is_valid_email('hristogmail.com'))

    # test invalid missing domain
    def test_invalid_missing_domain(self):
        self.assertFalse(is_valid_email('hristo@.com'))

    # test invalid missing username
    def test_invalid_missing_username(self):
        self.assertFalse(is_valid_email('@gmail.com'))

    # test empty str
    def test_invalid_empty_str(self):
        self.assertFalse(is_valid_email(''))


if __name__ == '__main__':
    unittest.main()
