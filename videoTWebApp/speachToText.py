import speech_recognition as sr
r = sr.Recognizer()

def STT(audio_source :str,title :str):
    
    file1 = open(f"text/{title}",'w')
    with sr.AudioFile(audio_source) as source:
        audio = r.record(source)
        text = r.recognize_google(audio)
        file1.write(text)
        file1.close()