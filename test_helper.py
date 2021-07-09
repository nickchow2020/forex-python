from helper import calculating_currency,currency_symbal
from forex_python.converter import RatesNotAvailableError
from unittest import TestCase

class Helper_test(TestCase):
    def test_calculating_currency(self):
        self.assertEqual(calculating_currency("USD","CNY",1),6.49)
        self.assertEqual(calculating_currency("CNY","USD",1),0.15)
        self.assertRaises(RatesNotAvailableError,calculating_currency,"WEWW","CNY",1)
        self.assertRaises(ValueError,calculating_currency,"USD","CNY","hes")
    
    def test_currency_symbal(self):
        self.assertEqual(currency_symbal("USD"),"US$")
        self.assertIsNone(currency_symbal("CNYs"))