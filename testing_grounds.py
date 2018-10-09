from person import *
from account import *

klient1 = Person("John", "Smith")
klient2 = Person("Jane", "Doe")
acc1 = Account(klient1)
acc2 = Account(klient2)

acc1.ustawDebet(0.00)
acc2.ustawDebet(-100.00)

acc1.wplata(500.00)
acc2.wplata(900.00)

acc2.wyplata(300.00)
acc1.przelew(acc2, 200.00)

print(str(acc1))
print(str(acc2))

acc2.przelew(acc1, 950.00)

ustawOdsteki(2)

acc1.dodajOdsetki()
acc2.dodajOdsetki()

print(str(acc1))
print(str(acc2))
