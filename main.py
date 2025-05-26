import streamlit as st
import streamlit_shadcn_ui as ui
from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient

import datetime

now = datetime.datetime.now()

# Format the date and time
formatted_date_time = now.strftime('%Y/%m/%d %H:%M:%S')  

print(formatted_date_time) 



load_dotenv()

token = os.getenv("HUGGINGFACE_TOKEN")


st.title("Proficiency Voice Recognition")

# receive voice
audio_value = st.audio_input("Record a voice message")
# if audio_value:
#     st.audio(audio_value)



# Save the audio bytes to a temporary file
if audio_value:
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_value.getvalue())

    client = InferenceClient(
        provider="fal-ai",
        api_key=os.getenv("HUGGINGFACE_TOKEN"),
    )

    # ai
    transcription = client.automatic_speech_recognition("temp_audio.wav", model="openai/whisper-large-v3")
    
    st.write("Transcription:")
    st.write(transcription)

# @st.dialog("Cast your vote")
# def vote(item):
#     st.write(f"Why is {item} your favorite?")
#     reason = st.text_input("Because...")
#     if st.button("Submit"):
#         st.session_state.vote = {"item": item, "reason": reason}
#         st.rerun()
#
# if "vote" not in st.session_state:
#     st.write("Vote for your favorite")
#     if st.button("Voice recognize"):
#         vote("A")
#     if st.button("B"):
#         vote("B")
# else:
#     f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"
#
#
