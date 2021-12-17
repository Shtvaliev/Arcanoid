import unittest
from arcanoid import rebound_player


class MyTestCase(unittest.TestCase):
    def test_right1(self):
        self.assertEqual(rebound_player(10, True, 10), -10)

    def test_right2(self):
        self.assertEqual(rebound_player(10, False, 10), 10)

    def test_right3(self):
        self.assertEqual(rebound_player(345657, True, 0), -345657)

    def test_right4(self):
        self.assertEqual(rebound_player(945876039485673, True, -3254267), -945876039485673)

    def test_wrong1(self):
        with self.assertRaises(TypeError):
            rebound_player(945876039485673, -3254267)

    def test_wrong2(self):
        with self.assertRaises(TypeError):
            rebound_player(345657, True)

    def test_wrong3(self):
        with self.assertRaises(TypeError):
            rebound_player(True, 0)


if __name__ == '__main__':
    unittest.main()
