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