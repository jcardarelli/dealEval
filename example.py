#!/usr/bin/env python

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
