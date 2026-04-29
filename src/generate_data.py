import pandas as pd, numpy as np, os
os.makedirs('data', exist_ok=True)
np.random.seed(42)
n=7000
amount=np.random.exponential(100,n)
hour=np.random.randint(0,24,n)
tx_1h=np.random.poisson(1.8,n)
intl=np.random.binomial(1,0.1,n)
night=((hour<6)|(hour>22)).astype(int)
risk=(amount>280).astype(int)+(tx_1h>4).astype(int)+intl+night
fraud=((risk>=3)|((risk>=2)&(np.random.rand(n)<0.35))).astype(int)
pd.DataFrame({
'amount':amount.round(2),
'hour':hour,
'tx_1h':tx_1h,
'is_international':intl,
'is_night':night,
'Class':fraud
}).to_csv('data/creditcard.csv',index=False)
print('Dataset generated')
