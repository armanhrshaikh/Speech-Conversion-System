import sys
import speech_recognition as sr
import subprocess

# Create a recognizer instance
recognizer = sr.Recognizer()

# Get the audio file path from command line arguments
if len(sys.argv) < 2:
    print("Usage: python script_name.py <audio_file>")
    sys.exit(1)

audio_file = sys.argv[1]

# Convert audio file using ffmpeg
try:
    subprocess.run(["ffmpeg", "-i", audio_file, "output.wav", "-y" ])

    subprocess.run(["rm", audio_file]) #remove userinput opus file
    audio_file = "output.wav"
except subprocess.CalledProcessError as e:
    print("Error occurred while converting audio:", e)

# Load audio data
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)

# Recognize speech using Google Web Speech API
try:
    # Specify language as English (United States) and Portuguese (Brazil)
    text_en = recognizer.recognize_google(audio_data, language="en-US")
    text_pt = recognizer.recognize_google(audio_data, language="pt-BR")

    print("English Transcription:", text_en)
    subprocess.run(["clear"])
    subprocess.run(["rm", audio_file]) #remove output.wav
    print("Portuguese Transcription:", text_pt)
    result = subprocess.run(["trans", "-b", "-s", "pt", text_pt], capture_output=True, text=True)
    print(" ")
    print("English Trans: ", result.stdout)

except sr.UnknownValueError:
    print("Google Web Speech API could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Web Speech API; {0}".format(e))
