from transformers import pipeline
import time

def analyze_sentiment(text, model_name):
    sentiment = pipeline("sentiment-analysis", model=model_name)
    start = time.time()
    result = sentiment(text)
    end = time.time()
    return result, end - start
