# stt.py
import sounddevice as sd
import queue
import vosk
import json

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def listen_and_transcribe(model_path='vosk-model-small-en-us-0.15'):
    vosk.SetLogLevel(-1)
    model = vosk.Model(model_path)
    rec = vosk.KaldiRecognizer(model, 16000)
    
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("🎙️ Listening... (say something)")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text.strip():
                    print(f"🗣️ You said: {text}")
                    return text
