import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle
import pandas as pd


# Run the API with uvicorn : uvicorn app:app --reload
app = FastAPI()

# Load ML classification model
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


# Data class model
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float


@app.get('/')
def index():
    return {'message': 'Hello, World'}


# Expose the prediction functionality, make a prediction from the passed
# JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_banknote(data: BankNote):
    data = data.dict()

    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']

    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])

    if(prediction[0] > 0.5):
        prediction = "Fake note"
    else:
        prediction = "Its a Bank note"

    return {'prediction': prediction}


