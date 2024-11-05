from gtts import gTTS
import os

# Read the text file
with open('transcript.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Convert text to speech
tts = gTTS(text=text, lang='hi')

# Save the converted audio to a file
tts.save('hi_voice.mp3')

print("Audio has been saved as hi_voice.mp3")
