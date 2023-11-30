'''Задача 44: 
В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. 
Сможете ли вы это сделать без get_dummies?
'''

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

headers= data['whoAmI'].unique()
result = pd.DataFrame()
for i in headers:
  result[i] = (data['whoAmI'] == i).astype(int)
result.head(20)