from gtts import gTTS

import os

def TTS(input: str , language: str):
    audio = gTTS(text=input,lang=language,slow=False)
    title_list = input.split()
    title = ""
    for i in range(0,3):
        title+=title_list[i]
    audio.save(f'audio/{title}.wav')
