import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import lightgbm as lgb
import joblib

df = pd.read_csv("sample_data.csv", encoding='utf-8')

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\b\d{2}-\d{2}\b', '', text) 
    text = re.sub(r'\bz\d+\b', '', text)        
    stopwords = ['blik', 'karta', 'przelew', 'pos', 'waw', 'krakow', 'gdansk', 'poz', 'wroc']
    text = re.sub(r'\b(?:' + '|'.join(stopwords) + r')\b', '', text)
    text = re.sub(r'[^\w\s]', '', text)        
    return re.sub(r'\s+', ' ', text).strip()

df['clean_title'] = df['transfer_title'].apply(clean_text)

X_train, X_test, y_train, y_test = train_test_split(
    df['clean_title'], 
    df['category'], 
    test_size=0.2, 
    random_state=42
)

model_pipeline = Pipeline([
    (
        'vectorizer', 
        TfidfVectorizer(
            analyzer='char',
            ngram_range=(2, 4),
            max_features=5000
        )
    ),
    (
        'classifier', 
        lgb.LGBMClassifier(
            n_estimators=100,
            random_state=42,
            verbose=-1
        )
    )
])

print("Training the model...")
model_pipeline.fit(X_train, y_train)

predictions = model_pipeline.predict(X_test)
print("\nClassification report (including F1-Score):")
print(classification_report(y_test, predictions, zero_division=0))

new_transaction = "BLIK MCDONALDS Z333"
cleaned_text = clean_text(new_transaction)
result = model_pipeline.predict([cleaned_text])

print("-" * 40)
print(f"Raw transaction: {new_transaction}")
print(f"Model prediction: {result[0]}")

joblib.dump(model_pipeline, "model_fintech.joblib")
print("Model has been saved to 'model_fintech.joblib'")