from transformers import pipeline
import time

def classify_email(text, model_name):
    classifier = pipeline("text-classification", model=model_name)
    start = time.time()
    result = classifier(text)
    end = time.time()
    return result, end - start
