import pyaudio
from vosk import KaldiRecognizer
import vosk_languages
import json

def talk_to_write_US():
    model = vosk_languages.model_US
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    print("Listening...")
    rec = KaldiRecognizer(model, 16000)

    while True:
        data = stream.read(1024)
        if rec.AcceptWaveform(data):
            result_json = json.loads(rec.Result())
            return result_json.get("text", "")
