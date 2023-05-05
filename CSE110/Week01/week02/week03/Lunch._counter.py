childs_price=float(input('What is the price of the Kids Meal?:'))
adult_price=float(input('What is the price of the Adults Meal?:'))
#Meal Prices
num_children=int(input('How many childern are in youre group?:'))
num_adults=int(input('How many adults are in youre group?:'))
#Number Of Guests
Sales_tax_rate=float(input('What is the sales tax rate?:'))
subtotal = childs_price * num_children + adult_price * num_adults
sales_tax = subtotal * (Sales_tax_rate / 100)

print(f'Subtotal: {subtotal:.2f}')
print(f'Sales Tax: {sales_tax:.2f}')
print(f'Total: {subtotal+sales_tax}')
total= subtotal+sales_tax
#sales taxrate/Total
pay_amount=float(input('What is the payment amount?:'))
print(f'youre change is: {pay_amount-total:.2f}')
