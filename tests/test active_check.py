# -*- coding: utf-8 -*-
import unittest
from arcanoid import activate_check


class MyTestCase(unittest.TestCase):
    def test_right1(self):
        self.assertEqual(activate_check(1, 2345, 3246, 4356, 1234), (4356, 1234))

    def test_right2(self):
        self.assertEqual(activate_check(0, 2345, 3246, 4356, 1234), (2345 + 49, 3246 - 10))

    def test_right3(self):
        self.assertEqual(activate_check(0, 0, 0, 4356, 1234), (49, -10))

    def test_right4(self):
        self.assertEqual(activate_check(1, 1000**100, 1000**100, 1000**100, 1000**100), (1000**100, 1000**100))

    def test_wrong1(self):
        with self.assertRaises(TypeError):
            activate_check(1, 2345, 3246, 4356)

    def test_wrong2(self):
        with self.assertRaises(TypeError):
            activate_check(0, 2345, 3246)

    def test_wrong3(self):
        with self.assertRaises(TypeError):
            activate_check(0)


if __name__ == '__main__':
    unittest.main()
