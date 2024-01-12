def menu():
    print("1: admin Добавить деньги в банкомат")
    print("2: admin Проверить состояние")
    print("3: user Добавить деньги на счет")
    print("4: user Снять деньги со счета")
    print("5: user Узнать баланс")
    print("0: Выход")


class Money:
    def __init__(self, slot = [0] * 7):
        self.cash = {"50 rub": slot[0], "100 rub": slot[1], "200 rub": slot[2], "500 rub": slot[3], "1000 rub": slot[4], "2000 rub": slot[5], "5000 rub": slot[6]}
    def __str__(self):
        return f'{self.cash}'
    def __add__(self, other):
        currentMoney = []
        for i in self.cash:
            currentMoney.append(self.cash[i])
        if len(other) > 2:
            for i in range(len(currentMoney)):
                currentMoney[i] += other[i]
        else:
            nominals = [50, 100, 200, 500, 1000, 2000, 5000]
            if other[0] not in nominals:
                raise IOError(f"Номинала {other[0]} нет, доступные номиналы: {nominals}")
            currentMoney[nominals.index(other[0])] += other[1]
        return Money(currentMoney)
    def reduce(self, query):
        pass


import itertools
class Bankomat:
    bankId = itertools.count()
    def __init__(self):
        self.id = next(Bankomat.bankId)
        self.rest = Money()
    def __str__(self):
        return f'Bankomat ID {self.id}: {self.rest}'
    def addMoney(self, *args):
        if len(args) == 1:
            self.rest += args[0]
        elif len(args) == 2:
            self.rest += [args[0], args[1]]
    def giveMoney(self, query):
        return self.rest.reduce(query)



class User:
    userId = itertools.count()
    def __init__(self):
        self.id = next(User.userId)
        self.balance = 0
    def __str__(self):
        return f'User ID {self.id}'
    def addMoney(self, nom, count):
        self.balance += nom * count

def adminAddMoney(bank):
    bank.addMoney([1, 2, 3, 4, 5, 6, 7])

def userAddMoney(user, bank):
    print("Введите номинал и количество")
    nom, count = int(input()), int(input())
    try:
        bank.addMoney(nom, count)
    except IOError as ex:
        print(f"{ex}")
    else:
        user.addMoney(nom, count)
        print(f'Успешно внесено {nom * count} рублей!')

def userGiveMoney(user, bank):
    print("Введите сумму")
    query = int(input())
    try:
        cash = bank.giveMoney(query)
    except:
        print("error")
    else:
        print('Успех')


def userBalance(user):
    print(f'Ваш баланс {user.balance} рублей')


sber1 = Bankomat()
user1 = User()
while True:
    menu()
    cmd = int(input())
    if cmd == 0:
        break
    elif cmd == 1:
        adminAddMoney(sber1)
    elif cmd == 2:
        print(sber1)
    elif cmd == 3:
        userAddMoney(user1, sber1)
    elif cmd == 4:
        userGiveMoney(user1, sber1)
    elif cmd == 5:
        userBalance(user1)

