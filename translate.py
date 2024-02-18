# Use a pipeline as a high-level helper
# from transformers import pipeline

# print("Loading translation model...")

# pipe = pipeline("translation", model="facebook/nllb-200-distilled-600M")

# print("Translation model loaded successfully\n")

# def translate(text, source="en", target="ar"):
#     try:
#         translation = pipe(text, src_lang=source, tgt_lang=target)
#         return translation
#     except Exception as e:
#         print(f"Error translating text: {e}")
#         return None

import os
import json

import httpx

LANGUAGES = ['Acehnese (Arabic script)', 'Acehnese (Latin script)', 'Mesopotamian Arabic', 'Ta’izzi-Adeni Arabic', 'Tunisian Arabic', 'Afrikaans', 'South Levantine Arabic', 'Akan', 'Amharic', 'North Levantine Arabic', 'Modern Standard Arabic', 'Modern Standard Arabic (Romanized)', 'Najdi Arabic', 'Moroccan Arabic', 'Egyptian Arabic', 'Assamese', 'Asturian', 'Awadhi', 'Central Aymara', 'South Azerbaijani', 'North Azerbaijani', 'Bashkir', 'Bambara', 'Balinese', 'Belarusian', 'Bemba', 'Bengali', 'Bhojpuri', 'Banjar (Arabic script)', 'Banjar (Latin script)', 'Standard Tibetan', 'Bosnian', 'Buginese', 'Bulgarian', 'Catalan', 'Cebuano', 'Czech', 'Chokwe', 'Central Kurdish', 'Crimean Tatar', 'Welsh', 'Danish', 'German', 'Southwestern Dinka', 'Dyula', 'Dzongkha', 'Greek', 'English', 'Esperanto', 'Estonian', 'Basque', 'Ewe', 'Faroese', 'Fijian', 'Finnish', 'Fon', 'French', 'Friulian', 'Nigerian Fulfulde', 'Scottish Gaelic', 'Irish', 'Galician', 'Guarani', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hebrew', 'Hindi', 'Chhattisgarhi', 'Croatian', 'Hungarian', 'Armenian', 'Igbo', 'Ilocano', 'Indonesian', 'Icelandic', 'Italian', 'Javanese', 'Japanese', 'Kabyle', 'Jingpho', 'Kamba', 'Kannada', 'Kashmiri (Arabic script)', 'Kashmiri (Devanagari script)', 'Georgian', 'Central Kanuri (Arabic script)', 'Central Kanuri (Latin script)', 'Kazakh', 'Kabiyè', 'Kabuverdianu', 'Khmer', 'Kikuyu', 'Kinyarwanda', 'Kyrgyz', 'Kimbundu', 'Northern Kurdish', 'Kikongo', 'Korean', 'Lao', 'Ligurian', 'Limburgish', 'Lingala', 'Lithuanian', 'Lombard', 'Latgalian', 'Luxembourgish', 'Luba-Kasai', 'Ganda', 'Luo', 'Mizo', 'Standard Latvian', 'Magahi', 'Maithili', 'Malayalam', 'Marathi', 'Minangkabau (Arabic script)', 'Minangkabau (Latin script)', 'Macedonian', 'Plateau Malagasy', 'Maltese', 'Meitei (Bengali script)', 'Halh Mongolian', 'Mossi', 'Maori', 'Burmese', 'Dutch', 'Norwegian Nynorsk', 'Norwegian Bokmål', 'Nepali', 'Northern Sotho', 'Nuer', 'Nyanja', 'Occitan', 'West Central Oromo', 'Odia', 'Pangasinan', 'Eastern Panjabi', 'Papiamento', 'Western Persian', 'Polish', 'Portuguese', 'Dari', 'Southern Pashto', 'Ayacucho Quechua', 'Romanian', 'Rundi', 'Russian', 'Sango', 'Sanskrit', 'Santali', 'Sicilian', 'Shan', 'Sinhala', 'Slovak', 'Slovenian', 'Samoan', 'Shona', 'Sindhi', 'Somali', 'Southern Sotho', 'Spanish', 'Tosk Albanian', 'Sardinian', 'Serbian', 'Swati', 'Sundanese', 'Swedish', 'Swahili', 'Silesian', 'Tamil', 'Tatar', 'Telugu', 'Tajik', 'Tagalog', 'Thai', 'Tigrinya', 'Tamasheq (Latin script)', 'Tamasheq (Tifinagh script)', 'Tok Pisin', 'Tswana', 'Tsonga', 'Turkmen', 'Tumbuka', 'Turkish', 'Twi', 'Central Atlas Tamazight', 'Uyghur', 'Ukrainian', 'Umbundu', 'Urdu', 'Northern Uzbek', 'Venetian', 'Vietnamese', 'Waray', 'Wolof', 'Xhosa', 'Eastern Yiddish', 'Yoruba', 'Yue Chinese', 'Chinese (Simplified)', 'Chinese (Traditional)', 'Standard Malay', 'Zulu']

def translate(text, source="English", target="Urdu"):
    try:
        response = httpx.request(
            "POST",
            "https://geonmo-nllb-translation-demo.hf.space/api/predict",
            timeout=500,
            data=json.dumps({
                "data": [
                    source,
                    target,
                    text
                ],
                "session_hash": ""
                }),
            headers={"Authorization" : f"Bearer {os.environ.get('HF_API_KEY')}"}
        )
        sentiment_result = response.json()
        return sentiment_result.get("data")[0].get("result")
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return None