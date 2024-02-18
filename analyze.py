import streamlit as st
from pydub import AudioSegment

from audio_recorder_streamlit import audio_recorder

from transcribe import transcribe

from sentiment import analyze_sentiment

from translate import translate

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
 
    box = st.selectbox(label="Translation", index=47, options=['Acehnese (Arabic script)', 'Acehnese (Latin script)', 'Mesopotamian Arabic', 'Ta’izzi-Adeni Arabic', 'Tunisian Arabic', 'Afrikaans', 'South Levantine Arabic', 'Akan', 'Amharic', 'North Levantine Arabic', 'Modern Standard Arabic', 'Modern Standard Arabic (Romanized)', 'Najdi Arabic', 'Moroccan Arabic', 'Egyptian Arabic', 'Assamese', 'Asturian', 'Awadhi', 'Central Aymara', 'South Azerbaijani', 'North Azerbaijani', 'Bashkir', 'Bambara', 'Balinese', 'Belarusian', 'Bemba', 'Bengali', 'Bhojpuri', 'Banjar (Arabic script)', 'Banjar (Latin script)', 'Standard Tibetan', 'Bosnian', 'Buginese', 'Bulgarian', 'Catalan', 'Cebuano', 'Czech', 'Chokwe', 'Central Kurdish', 'Crimean Tatar', 'Welsh', 'Danish', 'German', 'Southwestern Dinka', 'Dyula', 'Dzongkha', 'Greek', 'English', 'Esperanto', 'Estonian', 'Basque', 'Ewe', 'Faroese', 'Fijian', 'Finnish', 'Fon', 'French', 'Friulian', 'Nigerian Fulfulde', 'Scottish Gaelic', 'Irish', 'Galician', 'Guarani', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hebrew', 'Hindi', 'Chhattisgarhi', 'Croatian', 'Hungarian', 'Armenian', 'Igbo', 'Ilocano', 'Indonesian', 'Icelandic', 'Italian', 'Javanese', 'Japanese', 'Kabyle', 'Jingpho', 'Kamba', 'Kannada', 'Kashmiri (Arabic script)', 'Kashmiri (Devanagari script)', 'Georgian', 'Central Kanuri (Arabic script)', 'Central Kanuri (Latin script)', 'Kazakh', 'Kabiyè', 'Kabuverdianu', 'Khmer', 'Kikuyu', 'Kinyarwanda', 'Kyrgyz', 'Kimbundu', 'Northern Kurdish', 'Kikongo', 'Korean', 'Lao', 'Ligurian', 'Limburgish', 'Lingala', 'Lithuanian', 'Lombard', 'Latgalian', 'Luxembourgish', 'Luba-Kasai', 'Ganda', 'Luo', 'Mizo', 'Standard Latvian', 'Magahi', 'Maithili', 'Malayalam', 'Marathi', 'Minangkabau (Arabic script)', 'Minangkabau (Latin script)', 'Macedonian', 'Plateau Malagasy', 'Maltese', 'Meitei (Bengali script)', 'Halh Mongolian', 'Mossi', 'Maori', 'Burmese', 'Dutch', 'Norwegian Nynorsk', 'Norwegian Bokmål', 'Nepali', 'Northern Sotho', 'Nuer', 'Nyanja', 'Occitan', 'West Central Oromo', 'Odia', 'Pangasinan', 'Eastern Panjabi', 'Papiamento', 'Western Persian', 'Polish', 'Portuguese', 'Dari', 'Southern Pashto', 'Ayacucho Quechua', 'Romanian', 'Rundi', 'Russian', 'Sango', 'Sanskrit', 'Santali', 'Sicilian', 'Shan', 'Sinhala', 'Slovak', 'Slovenian', 'Samoan', 'Shona', 'Sindhi', 'Somali', 'Southern Sotho', 'Spanish', 'Tosk Albanian', 'Sardinian', 'Serbian', 'Swati', 'Sundanese', 'Swedish', 'Swahili', 'Silesian', 'Tamil', 'Tatar', 'Telugu', 'Tajik', 'Tagalog', 'Thai', 'Tigrinya', 'Tamasheq (Latin script)', 'Tamasheq (Tifinagh script)', 'Tok Pisin', 'Tswana', 'Tsonga', 'Turkmen', 'Tumbuka', 'Turkish', 'Twi', 'Central Atlas Tamazight', 'Uyghur', 'Ukrainian', 'Umbundu', 'Urdu', 'Northern Uzbek', 'Venetian', 'Vietnamese', 'Waray', 'Wolof', 'Xhosa', 'Eastern Yiddish', 'Yoruba', 'Yue Chinese', 'Chinese (Simplified)', 'Chinese (Traditional)', 'Standard Malay', 'Zulu'])

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
