from transformers import pipeline
import time

def summarize_text(text, model_name):
    summarizer = pipeline("summarization", model=model_name)
    start = time.time()
    summary = summarizer(text, max_length=60, min_length=20)
    end = time.time()
    return summary, end - start
