import pvporcupine
import pyaudio
import struct
from config import PICO_ACCESS_KEY

def wake_word_detect():
    porcupine = pvporcupine.create(
        access_key=PICO_ACCESS_KEY,
        keywords=["jarvis"]
    )

    pa = pyaudio.PyAudio()
    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("🟢 Waiting for wake word" "...")

    while True:
        pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm = struct.unpack_from("h"*porcupine.frame_length, pcm)

        if porcupine.process(pcm) >= 0:
            stream.close()
            pa.terminate()
            porcupine.delete()
            return
