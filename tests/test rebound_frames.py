# -*- coding: utf-8 -*-
import unittest
from arcanoid import rebound_frames

default_parameters = {
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
    }


class MyTestCase(unittest.TestCase):
    def test_right1(self):
        self.assertEqual(rebound_frames(10, 10, 45, 432, 12, 1, default_parameters), (45, 432, 1))

    def test_right2(self):
        self.assertEqual(rebound_frames(800, 10, 45, 432, 12, 1, default_parameters), (-12, 432, 1))

    def test_right3(self):
        self.assertEqual(rebound_frames(800, -1, 45, 432, 12, 1, default_parameters), (-12, 12, 1))

    def test_right4(self):
        self.assertEqual(rebound_frames(800, 800, 45, 432, 12, 1, default_parameters), (0, 0, 0))

    def test_right5(self):
        self.assertEqual(rebound_frames(-10, -1, 45, 432, 12, 1, default_parameters), (12, 12, 1))

    def test_wrong1(self):
        with self.assertRaises(TypeError):
            rebound_frames(800, 800, 45, 432, 12, 1)

    def test_wrong2(self):
        with self.assertRaises(TypeError):
            rebound_frames(800, 10, 45, 432, 1, default_parameters)

    def test_wrong3(self):
        with self.assertRaises(TypeError):
            rebound_frames(10, 45, 432, 12, 1, default_parameters)


if __name__ == '__main__':
    unittest.main()
