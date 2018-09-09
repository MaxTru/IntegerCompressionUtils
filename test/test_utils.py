import unittest
import utils

class UtilsTest(unittest.TestCase):
    def test_unaryEncode(self):
        self.assertEqual(utils.unary_encode(2), '0b10')
        self.assertEqual(utils.unary_encode(10), '0b1111111110')
        self.assertNotEqual(utils.unary_encode(9), '0b1111111110')
        self.assertRaises(ValueError, utils.unary_encode, -55)

    def test_unaryDecode(self):
        self.assertEqual(utils.unary_decode('0b10'), 2)
        self.assertEqual(utils.unary_decode('0b11110'), 5)
        self.assertRaises(ValueError, utils.unary_decode, '0b10101010')
        self.assertRaises(ValueError, utils.unary_decode, '10101010')

    def test_gammaEncode(self):
        self.assertEqual(utils.gamma_encode(3), '0b101')
        self.assertEqual(utils.gamma_encode(5), '0b11001')
        self.assertNotEqual(utils.gamma_encode(5), '0b110011')
        self.assertRaises(ValueError, utils.gamma_encode, -55)

    def test_gammaDecode(self):
        self.assertEqual(utils.gamma_decode('0b101'), 3)
        self.assertEqual(utils.gamma_decode('0b11001'), 5)
        self.assertRaises(ValueError, utils.gamma_decode, '10101010')
        self.assertRaises(ValueError, utils.gamma_decode, '55')
