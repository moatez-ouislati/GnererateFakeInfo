from faker import Faker
from random import randint, choice

f = Faker()
payment_methodes = ['paypal', 'bitcoin']

for _ in range(20):
    money = randint(1, 100) * 0.99
    payment_methode = choice(payment_methodes)
    user_email = "*****" + f.email()[6:]
    print(f'{money}$ --- {user_email} --- {payment_methode}')
