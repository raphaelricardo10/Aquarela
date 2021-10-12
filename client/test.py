import requests
import pandas as pd
from bson.json_util import loads
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = 'http://127.0.0.1:8000/sales/'
headers = {'Authorization': 'Token 35c4a03a86e2719bd89108a87a0c3f765bd2bc97'}
r = requests.get(url, headers=headers)
data = loads(r.content)
df = pd.json_normalize(data)
df.groupby('customer.age').size().plot(kind='bar')
plt.show()

print()