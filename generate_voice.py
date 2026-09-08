import os
import wave
from google import genai
from google.genai import types

API_KEY = os.environ["GEMINI_API_KEY"]

client = genai.Client(api_key=API_KEY)

with open("fact.txt", "r", encoding="utf-8") as f:
    fact = f.read().strip()

prompt = f"""
Read the following amazing fact naturally and clearly.
Use an engaging voice suitable for a short TikTok video.

Amazing fact:
{fact}
"""

response = client.models.generate_content(
    model="gemini-3.1-flash-tts-preview",
    contents=prompt,
    config=types.GenerateContentConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name="Kore"
                )
            )
        )
    )
)

audio_data = response.candidates[0].content.parts[0].inline_data.data

with wave.open("narration.wav", "wb") as wav:
    wav.setnchannels(1)
    wav.setsampwidth(2)
    wav.setframerate(24000)
    wav.writeframes(audio_data)

print("Voice generated successfully!")
print("Created: narration.wav")