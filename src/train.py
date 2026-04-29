import os, pandas as pd, joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt, seaborn as sns

os.makedirs('models', exist_ok=True)
os.makedirs('outputs', exist_ok=True)

df=pd.read_csv('data/creditcard.csv')
X=df.drop('Class',axis=1); y=df['Class']
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

sc=StandardScaler()
Xtr=sc.fit_transform(Xtr)
Xte=sc.transform(Xte)

Xtr,ytr=SMOTE(random_state=42).fit_resample(Xtr,ytr)

model=RandomForestClassifier(n_estimators=350,random_state=42)
model.fit(Xtr,ytr)

pred=model.predict(Xte)
print(classification_report(yte,pred))

cm=confusion_matrix(yte,pred)
plt.figure(figsize=(7,5))
sns.heatmap(cm,annot=True,fmt='d',cmap='Blues')
plt.title('Confusion Matrix')
plt.savefig('outputs/confusion_matrix.png',bbox_inches='tight')

joblib.dump({'model':model,'scaler':sc},'models/model.pkl')
print('Model saved')
