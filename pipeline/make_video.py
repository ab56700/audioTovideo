from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

def create_video(scenes, audio_path, output_path):
    audio = AudioFileClip(audio_path)
    duration = audio.duration / len(scenes)

    clips = []
    for img in scenes:
        clips.append(ImageClip(img).set_duration(duration))

    final = concatenate_videoclips(clips, method="compose")
    final = final.set_audio(audio)
    final.write_videofile(output_path, fps=24)

    return output_path
