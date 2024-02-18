import os
import logging
logging.basicConfig(level=logging.INFO)

import whisper

logging.info(f"""Loading whisper model '{os.environ.get("WHISPER_MODEL")}'...""")

model = whisper.load_model(os.environ.get("WHISPER_MODEL"))

logging.info("Whisper model loaded successfully\n")

def transcribe(path):
    transcript = model.transcribe(path)
    return transcript.get("text")
