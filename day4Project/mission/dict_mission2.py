# 경로 표시 : mission\\dict_mission2.py
#            mission/dict_mission2.py
# 모듈 표시 : mission.dict_mission2

# 사전 자료형 복습문제 2
'''     키보드로 값을 입력받고 요구대로 처리한 다음 출력 확인하시오.
입력내용 :
    번호 : 12 (sno : int)
    이름 : 황지니 (sname : str)
    국어 : 85 (kor : int)
    영어 : 85 (eng : int)
    수학 : 85 (mat : int)
처리내용 :
    입력받은 값들을 사전(sungjuk_dict)에 저장하시오.      키는 위의 변수이름을 문자형으로 사용하시오.
    3과목의 총점 (tot : int) 과 3과목의 평균 (avg : float)을 사전에 추가하시오.
출력내용 :
    12번 황지니의 총점은 255 점, 평균은 85.0 점.
    국어 : 85 점, 영어 : 85 점, 수학 : 85 점입니다.
'''

def dictfunc1():
    sungjuk_dict = {}
    sungjuk_dict['sno'] = int(input('번호 : '))
    sungjuk_dict['sname'] = input('이름 : ')
    sungjuk_dict['kor'] = int(input('국어 : '))
    sungjuk_dict['eng'] = int(input('영어 : '))
    sungjuk_dict['mat'] = int(input('수학 : '))
    sungjuk_dict['tot'] = sungjuk_dict['kor'] + sungjuk_dict['eng'] + sungjuk_dict['mat']
    sungjuk_dict['avg'] = sungjuk_dict['tot'] / 3

    print("{}번 {}의 총점은 {} 점, 평균은 {} 점.\n"
          "국어 : {} 점, 영어 : {} 점, 수학 : {} 점입니다."
          .format(sungjuk_dict['sno'], sungjuk_dict['sname'],
                  sungjuk_dict['tot'], sungjuk_dict['avg'],
                  sungjuk_dict['kor'], sungjuk_dict['eng'],
                  sungjuk_dict['mat']))

# dict 저장 방식을 변경해 보시오.   # 학생번호를 키로 사용하고, 나머지 학생정보를 리스트로 만들어서
# 번호 : [이름, 국어, 영어, 수학, 총점, 평균]  # sungjuk_dict 에 저장한 다음 출력하시오.
def dictfunc2():

    sno = int(input('번호 : '))
    sname = input('이름 : ')
    kor = int(input('국어 : '))
    eng = int(input('영어 : '))
    mat = int(input('수학 : '))
    tot = kor + eng + mat
    avg = tot / 3
    sungjuk_dict = {sno : [sname, kor, eng, mat, tot, avg]}

    print('{}번 {}의 총점은 {}점, 평균은 {:0.2f}점,\n'
        '국어 : {}점, 영어 : {}점, 수학 : {}점 입니다.'
          .format(sno, sungjuk_dict[sno][0],
                  sungjuk_dict[sno][4], sungjuk_dict[sno][5],
                  sungjuk_dict[sno][1], sungjuk_dict[sno][2],sungjuk_dict[sno][3]))