from gtts import gTTS
# ModuleNotFoundError : No module named 'gtts'
# pip install gtts

import os
import playsound
# ModuleNotFoundError : No module named 'playsound'
# pip install playsound==1.2.2


###############################
# 3. 구글 TTS(텍스트 -> 음성으로)
###############################

def speak(text):
    tts = gTTS(text=text, lang='ko', ) # 구글의 TTS 클래스로 tts 객체 생성(텍스트 -> 음성으로 변경)
    filename='voice.mp3' # 파일이름을 정해주고
    tts.save(filename) # 파일을 만들고,
    playsound.playsound(filename) # 해당 음성파일을 실행(즉, 음성을 말함)
    os.remove(filename) # 파일을 삭제

# speak("만나서 반갑습니다.")# 함수 호출하여 텍스트를 음성으로 바꿔줌