import argparse
from gtts import gTTS
import os

# Set up argument parser
parser = argparse.ArgumentParser(description="Convert text from a file to speech and save it as an audio file.")
parser.add_argument('text_file', type=str, help="Path to the text file to convert to speech.")

# Parse command-line arguments
args = parser.parse_args()

# Read the text file
try:
    with open(args.text_file, 'r', encoding='utf-8') as file:
        text = file.read()
except FileNotFoundError:
    print(f"Error: The file '{args.text_file}' does not exist.")
    exit(1)

# Convert text to speech
tts = gTTS(text=text, lang='hi')

# Save the converted audio to a file
output_file = 'hi_voice.mp3'
tts.save(output_file)

print(f"Audio has been saved as {output_file}")
