import speech_recognition as sr

# Create a recognizer instance
recognizer = sr.Recognizer()

# Load audio file
audio_file = "test.wav"  # Replace with the path to your audio file

# Load audio data
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)

# Recognize speech using Google Web Speech API
try:
    # Specify language as English (United States) and Portuguese (Brazil)
    text_en = recognizer.recognize_google(audio_data, language="en-US")
    text_pt = recognizer.recognize_google(audio_data, language="de")
    
    print("English Transcription:", text_en)
    print("Portuguese Transcription:", text_pt)
    
except sr.UnknownValueError:
    print("Google Web Speech API could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Web Speech API; {0}".format(e))
