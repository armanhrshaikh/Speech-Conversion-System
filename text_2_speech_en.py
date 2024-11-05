from gtts import gTTS

# Replace the text below with your Hindi translation
text = """
Hey friends, 
How Are you all?"""  # Example Hindi text; replace with your actual text
tts = gTTS(text, lang='en')
tts.save("gtt_en_voice.mp3")


