import argparse
import logging
logging.basicConfig(level=logging.INFO)

from translate import translate, LANGUAGES

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Process audio with different classifications')

# Add arguments for audio path and classification type
parser.add_argument('--audio_path', type=str, help='Path to the audio file', required=True)
parser.add_argument('--type', type=str, choices=['sentiment', 'translation', 'all'], help='Type of classification', required=True)
parser.add_argument('--target', type=str, help='Target language for translation', default="Modern Standard Arabic", choices=LANGUAGES)

# Parse the command line arguments
args = parser.parse_args()

# Access the values of the arguments
audio_path = args.audio_path
classification_type = args.type
target_language = args.target

from sentiment import analyze_sentiment

from transcribe import transcribe

logging.info(f"Processing audio at {audio_path}...")

# Transcribe the audio
transcription = transcribe(audio_path)

logging.info(f"Transcribed Successfully!\nTranscription: {transcription}")

if classification_type == "sentiment" or classification_type == "all":
    # Analyze sentiment
    logging.info("Analyzing sentiment...")
    sentiment = analyze_sentiment(transcription)
    logging.info(f"Sentiment: {sentiment}")

if classification_type == "translation" or classification_type == "all":
    # Translate the transcription
    logging.info("Translating...")
    translation = translate(transcription, target=target_language)
    logging.info(f"Translation: {translation}")