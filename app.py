# import os
#
# # ⛔ Must be before ANY transformers import
# os.environ["TRANSFORMERS_NO_TF"] = "1"
#
# from transformers import pipeline
# import torch
#
# pipe = pipeline(
#     "automatic-speech-recognition",
#     model="openai/whisper-large-v3",
#     device=0 if torch.backends.mps.is_available() else -1
# )
#
# output = pipe("your_audio.wav")
# print("Transcription:", output["text"])
