import unittest
from led import led

class TestLed(unittest.TestCase):
    def test_1_needs_2_leds(self):
        self.assertEqual(2, led(1))

    def test_2_needs_5_leds(self):
        self.assertEqual(5, led(2))

    def test_3_needs_5_leds(self): 
        self.assertEqual(5, led(3))

    def test_4_needs_4_leds(self):
        self.assertEqual(4, led(4))

    def test_5_needs_5_leds(self):
        self.assertEqual(5, led(5))

    def test_6_needs_6_leds(self):
        self.assertEqual(6, led(6)) 

    def test_7_needs_3_leds(self):
        self.assertEqual(3, led(7))

    def test_8_needs_7_leds(self):
        self.assertEqual(7, led(8))

    def test_9_needs_6_leds(self):
        self.assertEqual(6, led(9))

    def test_0_needs_6_leds(self):
        self.assertEqual(6, led(0))   

    def test_11_needs_4_leds(self):
        self.assertEqual(4, led(11))

    def test_141_needs_8_leds(self):
        self.assertEqual(8, led(141))

unittest.main()
