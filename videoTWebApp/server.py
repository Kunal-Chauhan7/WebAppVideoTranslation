import moviepy.editor as mp
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS

i = 1
translator = Translator()
r = sr.Recognizer()

from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    video = request.files['video']
    video_path = f"video/{i}.mp4"
    video.save(video_path)

    # Process the video file here
    # making an audio file from the video
    my_clip = mp.VideoFileClip(video_path)
    my_clip.audio.write_audiofile(f"audio/{i}.wav")

    # making a text file from audio
    file1 = open(f"text/{i}.txt", 'w')
    with sr.AudioFile(f"audio/{i}.wav") as source:
        audio = r.record(source)
        text = r.recognize_google(audio)
        file1.write(text)
        file1.close()

    # making a translated text file from text file
    with open(f"text/{i}.txt", 'r', encoding='utf-8') as file1:
        with open(f"{i}translated.txt", 'w', encoding='utf-8') as file2:
            for j in file1:
                input_text = j
                output = translator.translate(input_text, dest='hi')
                file2.write(output.text + '\n')
    file1.close()
    file2.close()

    # making an audio file from translated text file
    with open(f"{i}translated.txt", 'r', encoding='utf-8') as file1:
        input_text = file1.read()
        audio = gTTS(text=input_text, lang='hi', slow=False)
        audio.save(f'audio/{i}_translated.wav')
    file1.close()

    # making a video file from audio file
    video = mp.VideoFileClip(video_path)
    audio = mp.AudioFileClip(f'audio/{i}_translated.wav')
    final = video.set_audio(audio)
    final.write_videofile(f"video/{i}_translated.mp4")
    final.close()
    video.close()
    audio.close()

    # Return the video file as a response
    translated_video_path = f"video/{i}_translated.mp4"
    return send_file(translated_video_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)