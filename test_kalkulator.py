import unittest
from kalkulator import Kalkulator

class TestKalkulator(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(Kalkulator.tambah(5, 3), 8)
        self.assertEqual(Kalkulator.tambah(-2, 4), 2)
        self.assertEqual(Kalkulator.tambah(0, 0), 0)

    def test_kurangi(self):
        self.assertEqual(Kalkulator.kurangi(10, 4), 6)
        self.assertEqual(Kalkulator.kurangi(5, 10), -5)
        self.assertEqual(Kalkulator.kurangi(0, 0), 0)

    def test_kali(self):
        self.assertEqual(Kalkulator.kali(3, 4), 12)
        self.assertEqual(Kalkulator.kali(5, 0), 0)
        self.assertEqual(Kalkulator.kali(-2, 3), -6)

    def test_bagi(self):
        self.assertEqual(Kalkulator.bagi(10, 2), 5)
        with self.assertRaises(ValueError):
            Kalkulator.bagi(10, 0)

if __name__ == '__main__':
    unittest.main()