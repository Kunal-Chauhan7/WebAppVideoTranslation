import moviepy.editor as mp

def videoToAudio(fileSource: str, title: str):
    my_clip = mp.VideoFileClip(fileSource)
    my_clip.audio.write_audiofile(f"audio/{title}.wav")
