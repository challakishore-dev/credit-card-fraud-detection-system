from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib, pandas as pd

app=FastAPI(title='Fraud Detection Final')
templates=Jinja2Templates(directory='templates')
bundle=joblib.load('models/model.pkl')

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request,name='index.html',context={'request':request})

@app.post('/predict')
async def predict(request: Request):
    form=await request.form()
    vals={k:float(v) for k,v in form.items()}
    df=pd.DataFrame([vals])
    prob=float(bundle['model'].predict_proba(bundle['scaler'].transform(df))[0][1])
    return {'probability':round(prob,4),'decision':'REVIEW' if prob>0.5 else 'ALLOW'}
