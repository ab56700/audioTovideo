from faster_whisper import WhisperModel

def generate_scenes(audio_path):
    model = WhisperModel("tiny", device="cpu")
    segments, _ = model.transcribe(audio_path)

    scenes = [seg.text.strip() for seg in segments]
    return scenes
