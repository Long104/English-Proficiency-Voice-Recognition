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

# transcription = ""
# result = " "

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

        st.write("Transcription:")
        st.write(transcription)
        # st.write(result)

        st.write("Language:")
        match transcription:
            case "สวัสดี":
                st.write("Thai")
                st.image("./img/thai.png", caption="Thai")
            case "Hello.":
                st.write("English")
                st.image("./img/english.png", caption="English")
            case "Hola.":
                st.write("Spanish")
                st.image("./img/spanish.png", caption="Spanish")
            case "Bonjour.":
                st.write("French")
                st.image("./img/french.png", caption="French")
            case "你好":
                st.write("Chinese")
                st.image("./img/chinese.png", caption="Chinese")
            case "مرحبا":
                st.write("Arabic")
                st.image("./img/arabic.png", caption="Arabic")
            case "こんにちは":
                st.write("Japanese")
                st.image("./img/japanese.png", caption="Japanese")
            case "привет":
                st.write("Russian")
                st.image("./img/russia.png", caption="Russia")
            case _:
                st.write("Unknown language")

        # if transcription == "สวัสดี":
        #     st.write("Thai")
        #     st.image("./img/thai.png", caption="Thai")
        # elif transcription == "Hello.":
        #     st.write("English")
        #     st.image("./img/english.png", caption="English")
        # elif transcription == "Hola.":
        #     st.write("Spanish")
        #     st.image("./img/spanish.png", caption="Spanish")
        # elif transcription == "Bonjour.":
        #     st.write("French")
        #     st.image("./img/french.png", caption="French")
        # elif transcription == "你好":
        #     st.write("Chinese")
        #     st.image("./img/chinese.png", caption="Chinese")
        # elif transcription == "مرحبا":
        #     st.write("Arabic")
        #     st.image("./img/arabic.png", caption="Arabic")
        # elif transcription == "こんにちは":
        #     st.write("Japanese")
        #     st.image("./img/japanese.png", caption="Japanese")
        # elif transcription == "привет":
        #     st.write("Russian")
        #     st.image("./img/russia.png", caption="Russia")
        # else:
        #     st.write("Unknown language")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err.response.status_code}")
        print(f"Details: {err.response.text}")
    except Exception as e:
        print(f"Error: {str(e)}")


# st.write("language:")
# st.write(transcription.inferred_languages[0])
