# FinTech Transaction Categorization API 🏦🤖
An end-to-end Machine Learning project designed to automatically categorize raw bank transfer titles into standardized expense categories. Built as a complete pipeline from synthetic data generation and model training to MLOps containerization and API deployment.

## Project Overview
In real-world banking applications (like Personal Finance Management tools), transaction titles are often messy, inconsistent, and filled with noise (e.g., dates, POS numbers, random strings). This project solves that problem by:

Simulating a real-world messy dataset of bank transactions.

Cleaning and preprocessing the text data using Regex and TF-IDF (character-level n-grams).

Classifying the transactions using a LightGBM model.

Serving the trained model via a blazing-fast FastAPI endpoint.

Containerizing the entire environment using Docker for seamless deployment.

## Tech Stack
Machine Learning: Scikit-Learn (TF-IDF Vectorizer, Pipeline), LightGBM

Data Processing: Pandas, Regex, Faker (Synthetic Data Generation)

Backend API: FastAPI, Uvicorn, Pydantic

MLOps / Deployment: Docker, Joblib

## How to Run the Project (Docker)
The easiest way to run this API is via Docker. You don't need to install Python or any libraries locally.

1. Clone the repository:

git clone https://github.com/YOUR-USERNAME/FinTech-Transaction-Classifier.git

cd FinTech-Transaction-Classifier

2. Build the Docker image:

docker build -t fintech-api .

3. Run the container:

docker run -d -p 8000:8000 fintech-api

4. Access the Interactive API Docs:
Open your browser and navigate to http://localhost:8000/docs to test the API directly via the Swagger UI.

## API Usage Example
Endpoint: POST /categorize

Request Body:

{
"transfer_title": "BLIK MCDONALDS WAW Z333"
}

Response:

{
"status": "success",
"category": "Food",
"original_title": "BLIK MCDONALDS WAW Z333",
"clean_title": "mcdonalds"
}

## Model Architecture
Text Processing: TfidfVectorizer(analyzer='char', ngram_range=(2, 4)) - Designed to catch partial matches and roots of words, effectively handling typos and unknown merchant variations (OOV problem).

Classifier: LGBMClassifier - Chosen for its high performance and speed with tabular and sparse text data.