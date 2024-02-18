import logging
logging.basicConfig(level=logging.INFO)

from transformers import pipeline

logging.info("Loading sentiment analysis model...")

classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=3)

logging.info("Sentiment analysis model loaded successfully\n")

def analyze_sentiment(text):
    try:
        sentiment_result = classifier(text)[0]
        # convert to dictionary
        return {result.get("label"): result.get("score") for result in sentiment_result}
    except Exception as e:
        logging.error(f"Error analyzing sentiment: {e}")
        return None