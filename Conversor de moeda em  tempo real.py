from forex_python.converter import CurrencyRates
c = CurrencyRates()
amount = int(input('Entre com o amount:'))
from_currency = input('From Currency:').upper()
to_currency = input('To Currency:').upper()
print(from_currency, 'To', to_currency, amount)
resultado = c.convert(from_currency, to_currency, amount)
print(resultado)
