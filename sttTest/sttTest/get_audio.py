import speech_recognition as sr # 구글의 음성인식 모듈 임포트
# ModuleNotFoundError : No module named 'speech_recognition'
# pip install SpeechRecognition, pip install pyaudio

###############################
# 1. 구글 STT(음성 -> 텍스트로)
###############################

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        said = " "

        try:
            said =r.recognize_google(audio, language='ko-RK') # 음성이 한국어임을 인식하고 said 변수에 저장
            print("Your speech thinks like : ", said)
        except Exception as e:
            print("Exception : "+str(e))

    return said

# 1. 음성입력
text = get_audio() # 함수 호출