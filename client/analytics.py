import requests
import pandas as pd
from bson.json_util import loads
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

url = 'http://127.0.0.1:8000/sales/'
headers = {'Authorization': 'Token 35c4a03a86e2719bd89108a87a0c3f765bd2bc97'}
r = requests.get(url, headers=headers)
data = loads(r.content)
df = pd.json_normalize(data)

sns.set()
plt.figure()
df.groupby('customer.age').size().plot(xlabel='Customer Age', kind='bar', figsize=(20,5), title='Number of customers by age')
plt.show()

items = pd.DataFrame(columns=['name', 'tags', 'price', 'quantity'])
itemLst = []

for index, row in df.iterrows():
    rowDf = pd.DataFrame(row['items'])
    rowDf['order_id'] = row['_id']
    itemLst.append(rowDf)
    
items = pd.concat(itemLst)
items.head(15).groupby(['order_id', 'name']).sum()