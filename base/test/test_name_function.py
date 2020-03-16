import unittest

from .name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """
    测试 name_function.py
    运行 test_name_function.py时，所有以test打头的方法都将自动运行
    """

    def test_first_last_name(self):
        formatted_name = get_formatted_name('dwyane', 'wade')
        self.assertEqual(formatted_name, 'Dwyane Wade')


if __name__ == '__main__':
    unittest.main()
