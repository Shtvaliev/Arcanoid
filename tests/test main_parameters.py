import unittest
from arcanoid import main_parameters


class MyTestCase(unittest.TestCase):
    def test_right(self):
        self.assertEqual(main_parameters(), {
        'width': 700,
        'height': 700,
        'FPS': 60,
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'red': (255, 0, 0),
        'green': (10, 186, 181),
        'blue': (0, 0, 255),
        'speed': 3,
        'is_active': 0,
        'x': 0,
        'y': 0
        })

    def test_wrong1(self):
        with self.assertRaises(TypeError):
            main_parameters(2)

    def test_wrong2(self):
        with self.assertRaises(TypeError):
            main_parameters('')


if __name__ == '__main__':
    unittest.main()
