import requests as rq
import pandas as pd
import time
import datetime as dt

response = rq.get('http://opendata.trudvsem.ru/api/v1/vacancies')
data = response.json()

df_data = pd.DataFrame(response)

print(data)
