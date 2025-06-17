import os

import requests
import streamlit as st

# import streamlit_shadcn_ui as ui
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("HUGGINGFACE_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
headers = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_TOKEN')}",
    "Content-Type": "audio/flac",
}


st.title("Proficiency Voice Recognition")

# receive voice
audio_value = st.audio_input("Record a voice message")

transcription = ""

# Save the audio bytes to a temporary file
if audio_value:
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_value.getvalue())

    with open("temp_audio.wav", "rb") as audio_file:
        audio_data = audio_file.read()

    try:
        # Send the request
        response = requests.post(API_URL, headers=headers, data=audio_data)
        response.raise_for_status()  # Raise exception for non-200 status

        # Parse the response
        result = response.json()

        # Extract both text and language
        transcription = result.get("text", "").strip()
        language = result.get("language", "unknown")

        # print(f"Detected language: {language}")
        # print(f"Transcription: {transcription}")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err.response.status_code}")
        print(f"Details: {err.response.text}")
    except Exception as e:
        print(f"Error: {str(e)}")

    # ai

st.write("Transcription:")
st.write(transcription)
# st.write("language:")
# st.write(transcription.inferred_languages[0])
