from transformers import pipeline

print("Loading sentiment analysis model...")

classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=3)

print("Sentiment analysis model loaded successfully\n")

def analyze_sentiment(text):
    try:
        sentiment_result = classifier(text)[0]
        # convert to dictionary
        return {result.get("label"): result.get("score") for result in sentiment_result}
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return None