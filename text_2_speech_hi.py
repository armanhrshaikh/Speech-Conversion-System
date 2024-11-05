from gtts import gTTS

# Replace the text below with your Hindi translation
text = """दोस्तों, इस ट्यूटोरियल सीरीज़ में आपका स्वागत है
मैं ट्यूटोरियल के अंत के करीब हूँ, मुझे लगता है कि मैं आपको
जो सिखा सकता हूँ, वह मैं भविष्य के वीडियो में
करूँगा"""  # Example Hindi text; replace with your actual text
tts = gTTS(text, lang='hi')
tts.save("gtt_hi_voice.mp3")


