from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
import re

app = FastAPI(title="Bank Transfer Categorization Engine", version="1.0")

model = joblib.load("model_fintech.joblib")

class TransferRequest(BaseModel):
    transfer_title: str

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\b\d{2}-\d{2}\b', '', text) 
    text = re.sub(r'\bz\d+\b', '', text)        
    stopwords = ['blik', 'karta', 'przelew', 'pos', 'waw', 'krakow', 'gdansk', 'poz', 'wroc']
    text = re.sub(r'\b(?:' + '|'.join(stopwords) + r')\b', '', text)
    text = re.sub(r'[^\w\s]', '', text)        
    return re.sub(r'\s+', ' ', text).strip()

@app.post("/categorize")
def categorize_transfer(request: TransferRequest):
    clean_title = clean_text(request.transfer_title)
    category = model.predict([clean_title])[0]
    return{
        "status": "success",
        "category": category,
        "original_title": request.transfer_title,
        "clean_title": clean_title
    }