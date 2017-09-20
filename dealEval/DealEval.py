#!/usr/bin/python

def toDollar(number):
    """ Need a float as input (?) """
    reformatted = '${:,.2f}'.format(number)
    return reformatted

class DealEval:
    """ The __init__ method of this class will do the same calculations as the video.
        The get* methods will return only the calculated value. 
    """
    def __init__(self, price, income, expenses, mortgage_payment, down_payment):
        self.price = float(price)
        self.income = float(income)
        self.expenses = float(expenses)
        self.mortgage_payment = float(mortgage_payment)
        self.down_payment = float(down_payment)
        self.NOI = self.income - self.expenses
        self.cash_flow = self.NOI - self.mortgage_payment
        self.cash_on_cash_return = self.cash_flow / self.down_payment
        self.cap_rate = self.NOI / self.price

    def getNOI(self):
        """ Output is NOI/year """
        return self.NOI

    def getCashFlow(self):
        """ Output is CashFlow/year """
        return self.cash_flow

    def getCashOnCash(self):
        return self.cash_on_cash_return

    def getCapRate(self):
        return self.cap_rate

    def printFactsBlock(self):
        print 'Facts:'
        print ' - Sales Price:', toDollar(self.price)
        print ' - Down Payment:', toDollar(self.down_payment)
        print (' - Mortgage Payment: ' + toDollar(self.mortgage_payment) + '/year')
        print (' - Income: ' + toDollar(self.income) + '/year')
        print (' - Expenses: ' + toDollar(self.expenses) + '/year')

    def printCalculationsBlock(self):
        print 'Calculations:'
        print ' - NOI:', toDollar(self.NOI)
        print (' - Cash Flow: ' + str(self.cash_flow) + '/year')
        print (' - Cash-on-Cash Return: ' + str(self.cash_on_cash_return) + ' %')
        print (' - Cap Rate: ' + str(self.cap_rate) + ' %')
