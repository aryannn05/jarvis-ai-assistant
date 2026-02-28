import sounddevice as sd
import scipy.io.wavfile as wav
from faster_whisper import WhisperModel
import numpy as np

model = WhisperModel("tiny", compute_type="int8")


def listen():
    fs = 16000
    duration = 2.5  # FAST listening

    print("🎙 Listening...")

    recording = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype=np.int16
    )
    sd.wait()

    wav.write("temp.wav", fs, recording)

    segments, _ = model.transcribe("temp.wav", language="en")

    text = ""
    for seg in segments:
        text += seg.text

    return text.strip().lower()
