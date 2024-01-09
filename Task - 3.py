class PackOfMoney:
    def __init__(self, ):
        self.bills = {}

    def add_bill(self, n, c):
        if n in self.bills:
            self.bills[n] = self.bills[n] + c
        else:
            self.bills[n] = c

    def calculate_total(self):
        total = 0
        for n, c in self.bills.items():
            total += n * c
        return total

    def __str__(self):
        result = 'Pack of money: [ '
        for n in self.bills.keys():
            result += f'{n}$: {self.bills[n]}, '
        result += ']'
        return result

    def __add__(self, other):
        for n in other.bills.keys():
            c = other.bills[n]
            self.add_bill(n, c)


pack_1 = PackOfMoney()
pack_1.add_bill(50, 10)
pack_1.add_bill(100, 5)
pack_1.add_bill(10, 100)
print(pack_1)

pack_2 = PackOfMoney()
pack_2.add_bill(50, 10)
pack_2.add_bill(100, 5)
pack_2.add_bill(100, 14)
print(pack_2)

pack_1 + pack_2
print(f'Total sum: {pack_1.calculate_total()}')