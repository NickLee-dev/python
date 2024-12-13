import os
import whisper
from gtts import gTTS
import sounddevice as sd
import wave

# 녹음 설정
SAMPLE_RATE = 16000
DURATION = 5  # 녹음 시간 (초)

def record_audio(filename="input.wav"):
    """
    사용자의 음성을 녹음하고 WAV 파일로 저장
    """
    try:
        print("Recording...")
        audio_data = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
        sd.wait()  # 녹음이 끝날 때까지 대기

        # 녹음 파일 저장
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)  # 16-bit
            wf.setframerate(SAMPLE_RATE)
            wf.writeframes(audio_data.tobytes())
        print(f"Audio recorded and saved to {filename}")
    except Exception as e:
        print(f"Error while recording audio: {e}")

def stt_with_whisper(audio_path):
    try:
        absolute_path = audio_path
        if not os.path.exists(absolute_path):
            print(f"Error: File not found at {absolute_path}")
            exit(1)
        print(f"Processing audio file: {absolute_path}")
        print("Loading Whisper model...")
        model = whisper.load_model("base")
        print("Transcribing audio...")
        result = model.transcribe(absolute_path)
        text = result.get("text", "")
        print(f"Transcription: {text}")
        return text
    except FileNotFoundError:
        print(f"Audio file not found: {absolute_path}")
        return ""
    except Exception as e:
        print(f"Error during transcription: {e}")
        return ""

def tts_with_gtts(text, output_path="output.mp3", lang="ko"):
    """
    텍스트를 음성으로 변환하고 MP3 파일로 저장
    """
    try:
        print("Converting text to speech...")
        tts = gTTS(text=text, lang=lang)
        tts.save(output_path)
        print(f"Audio saved to {output_path}")
        os.system(f"start {output_path}")  # Windows에서 MP3 파일 재생
    except Exception as e:
        print(f"Error during TTS: {e}")

if __name__ == "__main__":
    audio_file = "D:/python_workspace/whisper_test/input.wav"
    audio_file = os.path.abspath(audio_file)
    # 음성 녹음
    record_audio(audio_file)

    # 녹음 파일이 실제로 존재하는지 확인
    if not os.path.exists(audio_file):
        print(f"Error: File {audio_file} does not exist.")
        exit(1)

    # 음성을 텍스트로 변환
    text = stt_with_whisper(audio_file)

    # 변환된 텍스트가 있을 경우 TTS 수행
    if text:
        tts_with_gtts(text, "output.mp3", lang="ko")  # 언어 설정을 변경할 수 있음
    else:
        print("No transcription available. Skipping TTS.")
