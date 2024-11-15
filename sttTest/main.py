import sttTest.get_audio as ga
import sttTest.speak as sp
if __name__ == '__main__':
    text = ga.get_audio()
    sp.speak(text)