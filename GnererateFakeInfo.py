import pandas as pd
from datetime import date
from faker import Faker
from random import randint

f = Faker()

date_range = [d for d in pd.date_range(
    start=date(2023, 5, 1),
    end=date(2023, 6, 1))
]
dict_data ={
    'date': date_range,
    'name': [f.name() for _ in range(len(date_range))],
    'email': [f.email() for _ in range(len(date_range))],
    'money': [randint(1, 100) * 0.99 for _  in range(len(date_range))]
}

df = pd.DataFrame.from_dict(dict_data)
df.to_csv('out.csv', index =False)
