#!/usr/bin/python

def calculateTax(price, tax_rate):
    total = price + (price * tax_rate)


    my_price=10000
    print 'my_price (inside function) = ', my_price
    return total	

my_price = float(raw_input ('Enter price: '))

totalPrice = calculateTax(my_price, 0.06)
print 'price = ', my_price, 'Total price = ', totalPrice
print 'my_price (out function) = ', my_price
