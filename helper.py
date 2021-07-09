from forex_python.converter import CurrencyRates,CurrencyCodes

def calculating_currency(convert,to,amount):
    my_amount = int(amount)
    c = CurrencyRates().convert(convert,to,my_amount)
    return round(c,2)

def currency_symbal(cur):
    return CurrencyCodes().get_symbol(cur)