from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob

# Initialize FastAPI app
app = FastAPI()

# Define request model
class SentimentRequest(BaseModel):
    text: str

# API Endpoint for Sentiment Analysis
@app.post("/analyze")
async def analyze_sentiment(request: SentimentRequest):
    analysis = TextBlob(request.text)
    score = analysis.sentiment.polarity
    sentiment = "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"
    
    return {"text": request.text, "sentiment_score": score, "sentiment": sentiment}

