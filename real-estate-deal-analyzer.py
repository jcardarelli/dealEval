#!/usr/bin/python


# README.md
#####################################################

# Analyzing commercial real estate quickly and easily
# https://www.youtube.com/watch?v = m8QIzxXRMGA

# Three things to know about the deal you're analyzing:
	#1. How much money does it make?
	#2. What is your return on investment
	#3. How does this investment compare to other investments?


# Five key terms:
#################

# 1. Income and Expenses
	# Definition:
	#	Income: rents, lease payments made, laundry income, late fees
	#	Expenses: Insurance, taxes, utilities, repairs/maintenance, management fees. (Mortgage payment is not a line item in expenses).

	# Rules:
	#	Income > Expenses


# 2. Net Operating Income (NOI)
	# Definition:
	#	Income - Expenses
	#	Your income after you subtract your expenses.
	#
	# NOI goes up, so does cash flow, and so does the property value
	# NOI goes down, so does cash flow, and so does the property value

	# Rules:
	#	NOI > Mortgage payment


# 3. Cash Flow
	# Definition:
	#	NOI - Your mortgage payment
	#	What your property returns after calculating income, expenses, and your annual mortgage payment.

	# Rules:
	#	Positive


# 4. Cash-on-cash Return
	# Definition:
	#	Annual cash flow / Your down payment
	#	How fast your money is moving. Your return on investment.
	#
	#	"How fast can I get back my 20,000?"
	#		1 Year  =  100%
	#		2 Years  =  50%
	#		3 Years  =  33%
	#		4 Years  =  25%

	# Rules:
	#	> =  10%

# 5. Capitalization Rate (cap rate)
	# Definition:
	#	NOI / Sales price
	#	If you paid all cash for an investment, what would your return on investment (ROI) be?
	#
	#	Each neighborhood has its own cap rate:
	#		High cap rate - Low/moderate income neighborhood - higher risk, higher potential return, price is lower
	#		Low cap rate - High income neighborhood - lower risk, lower potential return, price is higher
	#

	# Rules:
	#	> =  8%


# example.py
#####################################################
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


############################################################################


def newDeal(price, income, expenses, mortgage_payment, down_payment):
    """
    price: Sale price
    income = Annual Income
    expenses = Annual Expenditures
    mortgage_payment = Annual mortgage payment
    down_payment = Down payment
    """
    # Instantiate a DealEval object
    de = DealEval(price, income, expenses, mortgage_payment, down_payment)

    # Facts Display block
    de.printFactsBlock()

    # Calculations block
    de.printCalculationsBlock()

print 'New Deal 1'
newDeal(450000, 48000, 12000, 20000, 112500)

print

print 'New Deal 2'
newDeal(50000, 10000, 4000, 2000, 10000)
