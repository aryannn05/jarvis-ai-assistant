import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import webrtcvad
from faster_whisper import WhisperModel
import collections

model = WhisperModel("tiny", compute_type="int8")
vad = webrtcvad.Vad(2)

def listen_live():
    fs = 16000
    frame_ms = 30
    frame_size = int(fs * frame_ms / 1000)

    ring = collections.deque(maxlen=10)
    recording = []
    triggered = False
    silence = 0

    stream = sd.InputStream(
        samplerate=fs,
        channels=1,
        dtype="int16",
        blocksize=frame_size
    )

    with stream:
        while True:
            frame, _ = stream.read(frame_size)
            speech = vad.is_speech(frame.tobytes(), fs)

            if speech:
                triggered = True
                recording.append(frame)
                silence = 0
            elif triggered:
                silence += 1
                recording.append(frame)

                if silence > 12:
                    break

    audio = np.concatenate(recording, axis=0)
    wav.write("live.wav", fs, audio)

    segments, _ = model.transcribe("live.wav", language="en")

    text = ""
    for seg in segments:
        text += seg.text

    return text.strip().lower()
