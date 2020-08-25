import math as mt
import datetime as dt
import random as rd
import time as tm

#math
print(mt.sqrt(9))
print("seno: %.3f, cosseno: %.3f" %(mt.sin(1), mt.cos(0)))
print("{}".format(mt.pi))

#datetime
print()
print("date: ", dt.date.today())
print("datetime: ", dt.datetime.now())
day = 11
month = 11
year = 2000
date = dt.date(year, month, day)
print(date.day)
print(date.month)
print(date.year)
hour = 13
minute = 29
horario = dt.datetime(year, month, day, hour, minute)
print(horario.hour)
print(horario.minute)
print(horario.second)

#random
print()
print(rd.random())
print(rd.randint(1, 10))
lista = ["maria", "1", "3.14", "3 + j"]
print(rd.choice(lista))

#time
print()
print(tm.time())

antes = tm.time()
lista = []
for i in range(0, 1000):
    lista.append(i)

depois = tm.time()
intervalo = antes - depois
print("tempo: {}".format(intervalo))
print("Trabalhando nas atualizações")
tm.sleep(3)
print("...")
tm.sleep(3)
print("Finalizando o programa")
















