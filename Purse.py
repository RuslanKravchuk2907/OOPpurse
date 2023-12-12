class Purse:
    def __init__(self, currency, name='Unknown'):  # Object constructor
        if currency not in ('USD', 'EUR'):
            raise ValueError
        self.__money = 0.00
        self.currency = currency
        self.name = name

    def top_up_balance(self, howmany):     # Top up your account
        self.__money = self.__money + howmany
        return howmany

    def  top_down_balance(self, howmany):  # To debit from the account
        if self.__money - howmany < 0:
            print('Insufficient funds')
            raise ValueError ('Insufficient funds')
        self.__money = self.__money - howmany
        return howmany
    def info(self):
        print(self.__money)

    def __del__(self):
        print('Wallet deleted')


x = Purse('USD')
y = Purse('USD', 'Ruslan')
y.top_up_balance(1000)
x.top_up_balance(y.top_down_balance(35))
x.info()
y.info()