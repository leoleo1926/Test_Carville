import unittest
from functions import calc_prices

class TestCalcPrices(unittest.TestCase):
    def test_valid_input(self):
        # ��������� ���������� ������� ������
        self.assertEqual(calc_prices(1.81, 20), (1.81, 1.51))
        self.assertEqual(calc_prices(1.81, 18), (1.81, 1.53))
        self.assertEqual(calc_prices(5.05, 27), (5.05, 3.98))

    def test_invalid_nds(self):
        # ��������� ��������� ������������� �������� ���
        self.assertEqual(calc_prices(1.81, -5), "NDS value error. The value must be in the range from 0 to 99")
        self.assertEqual(calc_prices(1.81, 100), "NDS value error. The value must be in the range from 0 to 99")

    def test_rounding(self):
        # ���������, ��� ���� �������� �������� 2 ����� ����� �������
        self.assertEqual(calc_prices(5.055, 27), (5.05, 3.98))
        self.assertEqual(calc_prices(1.815, 18), (1.82, 1.54))

if __name__ == '__main__':
    unittest.main()

