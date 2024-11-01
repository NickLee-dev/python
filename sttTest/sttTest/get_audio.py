import speech_recognition as sr # 구글의 음성인식 모듈 임포트
from translate import Translator
# ModuleNotFoundError : No module named 'speech_recognition'
# pip install SpeechRecognition, pip install pyaudio  # 음성 인식
# pip install translate==3.6.1
###############################
# 1. 구글 STT(음성 -> 텍스트로)
###############################

def get_audio():
    r = sr.Recognizer() # 구글 음성인식 모듈 클래스의 인스턴스(객체) 생성
    with sr.Microphone() as source: # 구글 음성인식 모듈 중 음성입력을 마크로 받음
        print("Say something!")
        audio = r.listen(source) # 구글의 음석인식모듈이 리슨하고 있다가 음성 입력을 받아서 변수에 저장
        said = " "

        try:
            said =r.recognize_google(audio, language='ko-KR') # 음성이 한국어임을 인식하고 said 변수에 저장
            print("Your speech thinks like : ", said) # 음성이 무엇인지 출력
        except Exception as e:
            print("Exception : "+str(e))

    return said

# 1. 음성입력
# text = get_audio() # 함수 호출

# 2. 번역 부분(한글 -> 영어로)
# translator = Translator(from_lang="ko", to_lang="en") # 한국어를 영어로 바꿔주는 translator 객체 생성
# translation = translator.translate(text)
# print(translation)

# 나라별 언어의 약어
# 영어 : 'en'
# 한국어 : 'ko'
# 일본어 : 'ja'
# 중국어(간체) : 'zh-CN'
# 중국어(번체) : 'zh-TW'
# 스페인어 : 'es'

