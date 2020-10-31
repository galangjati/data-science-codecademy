import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

vandc = pd.merge(visits, cart, how = 'left')

nnull = vandc[vandc.cart_time.isnull()]


percent_not_cart = float(len(nnull)) / len(vandc) 

candc = pd.merge(cart, checkout, how = 'left')
n_null_cc = candc[candc.checkout_time.isnull()]

percent_not_checkout = float(len(n_null_cc)) / len(candc)

all_data = visits.merge(cart, how = 'left').merge(checkout, how = 'left').merge(purchase, how = 'left')

candp = pd.merge(checkout, purchase, how = 'left')

n_co = len(candp)
n_no_purchase = len(candp[candp.purchase_time.isnull()])

percent_not_purchase = float(n_no_purchase) / n_co

'''
print(percent_not_cart)
print(percent_not_checkout)
print(percent_not_purchase)
'''

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

avg_purchase_time = all_data.time_to_purchase.mean()

print(avg_purchase_time)



