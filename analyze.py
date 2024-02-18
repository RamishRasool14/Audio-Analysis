import streamlit as st
from pydub import AudioSegment

from audio_recorder_streamlit import audio_recorder

from transcribe import transcribe

from sentiment import analyze_sentiment

from translate import translate, LANGUAGES

def main():
    st.title("Audio Sentiment Analysis App")

    # Option to upload or record audio
    option = st.radio("Choose an option", ("Upload Audio", "Record Audio"))

    if option == "Upload Audio":
        uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])
        if uploaded_file:
            st.audio(uploaded_file, format='audio/wav', start_time=0)
            path = process_audio(uploaded_file)

    elif option == "Record Audio":
        path = record_audio()
 
    box = st.selectbox(label="Translation", index=47, options=LANGUAGES)

    button = st.button("Analyze Audio", key="analyze_audio")

    if button:
        with st.spinner("Transcribing audio..."):
            transcription = transcribe(path)
            st.write("Transcription:", transcription)
        with st.spinner("Performing sentiment analysis..."):
            st.write("Sentiment:", analyze_sentiment(transcription))
        with st.spinner("Translating..."):
            st.write("Translation:", translate(transcription, target=box))

def process_audio(file, name="output.wav"):
    try:
        audio = AudioSegment.from_file(file)
        # Convert to WAV format
        audio = audio.set_channels(1).set_frame_rate(16000)
        audio.export(name, format="wav")
        return name
    
    except Exception as e:
        st.error(f"Error processing audio: {e}")
        return None

def record_audio(path="output.wav"):
    # record and preview audio
    audio_bytes = audio_recorder()
    if audio_bytes:
        st.audio(audio_bytes, format="audio/wav")

        with open(path, "wb") as f:
            f.write(audio_bytes)
    return path

if __name__ == "__main__":
    main()
