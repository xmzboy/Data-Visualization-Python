import unittest
from python_rep import connection


class TestConnection(unittest.TestCase):
    def test_connection(self):
        self.assertEqual(connection('https://api.github.com/search/repositories?q=language:python&sort=stars').status_code, 200)


if __name__ == '__main__':
    unittest.main()