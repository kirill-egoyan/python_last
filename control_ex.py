import random 
import pandas as pd
import numpy as np
lst = ['robot']  *  10
lst += ['human']  *  10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
unique_values = list(set(data['whoAmI']))
one_hot_encoded = pd.DataFrame(index=data.index, columns=unique_values)
for i, value in enumerate(data['whoAmI']):
    one_hot_encoded.iloc[i, unique_values.index(value)] = 1
data = data.join(one_hot_encoded)
data = data.drop('whoAmI', axis=1)
data = data.fillna(0)
print(data.head())