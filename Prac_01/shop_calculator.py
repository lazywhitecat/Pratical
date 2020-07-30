item_number= int(input('Enter the number of items:'))
price=0
while item_number < 0:
    print('Invalid number of items.')
    item_number=int(input('Enter the number of items:))
for i in range (0,item_number):
    prices=float(input('Enter the price for each items:'))
    price=price+prices
if price > 100:
    totalprice=price*0.9
print('total price for {} items is'.format(item_number),totalprice)
