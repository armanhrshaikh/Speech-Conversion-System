from gtts import gTTS
import os

# Your Hindi text goes here
hindi_text = """
Yahan apna Hindi text likhein. Yeh text aapke video ki translation hoga.
"""

# Specify the language as Hindi
language = 'hi'

# Create the gTTS object
speech = gTTS(text=hindi_text, lang=language, slow=False)

# Save the audio file
speech.save("hindi_voice.mp3")

# Optional: Play the audio file (you might need to use a different method based on your OS)
os.system("start hindi_voice.mp3")  # For Windows
# os.system("afplay hindi_voice.mp3")  # For macOS
# os.system("xdg-open hindi_voice.mp3")  # For Linux
