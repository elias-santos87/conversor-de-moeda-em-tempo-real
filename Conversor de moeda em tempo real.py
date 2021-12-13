from forex_python.converter import CurrencyRates
c = CurrencyRates()
montante = int(input("Enter the amount: "))
from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()
print(from_currency, " To ", to_currency, montante)
resultado = c.convert(from_currency, to_currency, montante)
print(resultado)

