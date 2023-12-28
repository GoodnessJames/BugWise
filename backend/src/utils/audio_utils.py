import sounddevice as sd
import os
from config.audio_config import SAMPLE_RATE, AUDIO_FORMAT


def record_audio(file_path, duration=10):
    audio_data = sd.rec(int(SAMPLE_RATE * duration), samplerate=SAMPLE_RATE,
                        channels=2, dtype='int16')
    sd.wait()
    save_audio(file_path, audio_data)


def save_audio(file_path, audio_data):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    sd.write(file_path, audio_data, samplerate=SAMPLE_RATE, format=AUDIO
             _FORMAT)
