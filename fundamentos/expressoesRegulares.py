import re

#search
frase = "meu número de telefone é (41)0000-0000"

f = re.search("\(\d{2}\)\d{4,5}-\d{4}", frase)
print(f)

email = "Entre em contato, meu e-mail é roberto@company.com"
e = re.search("\w+@\w+\.\w+", email)
print(e)

placa = "a placa do carro era FGA-2020"
p = re.search("[A-Za-z]{3}-\d{4}", placa)
print(p)

#match
print()
placa = "a placa do carro era FGA-2020"
print(re.match("[A-Za-z]{3}-\d{4}", placa))
placa = "FGA-2020 era a placa do carro"
print(re.match("[A-Za-z]{3}-\d{4}", placa))

#findall
print()




















