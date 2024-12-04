import uvicorn
from fastapi import FastAPI
import pickle
import pandas as pd


app = FastAPI()
with open("./model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/test")
def get_home():
    return "Application is running..."

@app.get('/predict')
def predict():
    data = pd.read_csv("deploy_test.csv")
    pred = model.predict(data)
    spisok=[]
    for i in pred:
        spisok.append(str(i))

    return {"predict":spisok }