import unittest
from arcanoid import activating


class MyTestCase(unittest.TestCase):
    def test_right1(self):
        self.assertEqual(activating(True, True, 0, 99, 0, 0), (99, -99, 0))

    def test_right2(self):
        self.assertEqual(activating(True, True, 1, 99, 0, 0), (0, 0, 0))

    def test_right3(self):
        self.assertEqual(activating(True, False, 0, 99, 0, 0), (99, -99, 1))

    def test_right4(self):
        self.assertEqual(activating(False, False, 1, 99, 4958, 2564), (4958, 2564, 1))

    def test_wrong1(self):
        with self.assertRaises(TypeError):
            activating(False, 1, 99, 4958, 2564)

    def test_wrong2(self):
        with self.assertRaises(TypeError):
            activating(True, True, 0, 99, 0)

    def test_wrong3(self):
        with self.assertRaises(TypeError):
            activating(True, True, 1, 0, 0)


if __name__ == '__main__':
    unittest.main()
