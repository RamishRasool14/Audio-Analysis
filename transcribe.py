import whisper

print("Loading whisper model...")

model = whisper.load_model("large")

print("Whisper model loaded successfully\n")

def transcribe(path):
    transcript = model.transcribe(path)
    return transcript.get("text")
