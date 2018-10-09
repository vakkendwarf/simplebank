from person import *

class Account(object):

    interest = 0

    def __init__(self, owner: Person):
        self.__owner = owner
        self.__balance = 0.00
        self.__debit = 0.00

    def balanceCheck(self, amt):
        if amt > (self.__balance - self.__debit):
            return print("Nie mozna wykonac operacji! Niewystarczajace srodki.")
        else:
            return True

    def wplata(self, amt):
        self.__balance += amt

    def wyplata(self, amt):
        if(self.balanceCheck(amt)):
            self.__balance -= amt

    def przelew(self, target, amt):
        if(self.balanceCheck(amt)):
            self.__balance -= amt
            target.__balance += amt

    def dodajOdsetki(self):
        self.__balance = self.__balance * (1+Account.interest/100)

    def ustawDebet(self, amt):
        self.__debit -= amt

    def __str__(self):
        return "Stan Konta: " + str(self.__balance)


def ustawOdsteki(percent):
    Account.interest = percent