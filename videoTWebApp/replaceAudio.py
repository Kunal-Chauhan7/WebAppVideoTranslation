import moviepy.editor as mp

def ReplacingAudio(videoSource: str, audioSource: str, title: str):
    video = mp.VideoFileClip(videoSource)
    audio = mp.AudioFileClip(audioSource)
    final = video.set_audio(audio)
    final.write_videofile(f"video/{title}_translated.mp4")
    final.close()
    video.close()
    audio.close()