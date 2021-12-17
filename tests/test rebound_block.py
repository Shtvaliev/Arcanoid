import unittest
from arcanoid import rebound_block


class MyTestCase(unittest.TestCase):
    def test_right1(self):
        self.assertEqual(rebound_block(5, 0, 5, 0, 6, 36, 6, 36, True, 2, 2), (2, 2))

    def test_right2(self):
        self.assertEqual(rebound_block(5, 0, 5, 0, 6, 36, 6, 36, True, 2, -2), (2, -2))

    def test_right3(self):
        self.assertEqual(rebound_block(25, 5, 10, 20, 5, 46, 11, 40, True, 10, -10), (-10, -10))

    def test_right4(self):
        self.assertEqual(rebound_block(105, 214, 219, 100, 106, 230, 200, 136, True, 100, 200), (100, -200))

    def test_right5(self):
        self.assertEqual(rebound_block(2015, 1031, 1036, 2010, 2000, 1030, 1000, 2030, True, 99, -9823), (-99, -9823))

    def test_right6(self):
        self.assertEqual(rebound_block(-66, -985, -980, -71, -100, -970, -1000, -70, True, 100, 100), (100, -100))

    def test_right7(self):
        self.assertEqual(rebound_block(-66, -985, -980, -71, -100, -970, -1000, -70, False, 100, 100), (100, 100))

    def test_wrong1(self):
        with self.assertRaises(TypeError):
            rebound_block(-66, -985, -980, -71, -100, -970, -1000, -70, 100, 100)

    def test_wrong2(self):
        with self.assertRaises(TypeError):
            rebound_block()

    def test_wrong3(self):
        with self.assertRaises(TypeError):
            rebound_block(2015, 1031, 1036, 2010, 2000, 1030, 1000, 2030, True, 99)


if __name__ == '__main__':
    unittest.main()
