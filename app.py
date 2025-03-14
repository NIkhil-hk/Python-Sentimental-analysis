from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()

# 🔥 Enable CORS 🔥
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any origin (Change this to specific domains for security)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

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
