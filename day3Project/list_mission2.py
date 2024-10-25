# list_mission2.py
# 리스트 실습문제2
"""    키보드로 값들을 입력받아, 요구대로 처리하고 확인 출력 코드를 작성하시오.
입력 내용 :
    국어 점수 : 78.5 (kor : float)
    영어 점수 : 88.7 (eng: float)
    수학 점수 : 93.5 (mat : float)
처리 내용 :
    3명의 학생 점수를 입력 받음, 각 학생의 총점과 평균은 각각 계산함
    학생별 점수는 각 리스트에 저장한 다음, [국어, 영어, 수학, 총점, 평균]
    각 학생 점수를 리스트(sungjuk_list)에 순서대로 저장 처리함
    [[국, 영, 수, 총, 평], [국, 영, 수, 총, 평], [국, 영, 수, 총, 평]]
    3명의 점수의 총합(total_score : int)과 전체평균(average_score : float)를
    계산하시오.
출력 내용 :
    리스트에 저장된 값들을 출력함,   국, 영, 수, 총, 평균 순서로 출력
     -> 점수는 소수점아래 둘째자리까지 표시
    -> format() 사용함
    전체 총점과 전체 평균을 출력하시오.
"""
sungjuk_list = []
kor = float(input('국어 점수 : '))
eng = float(input('영어 점수 : '))
mat = float(input('수학 점수 : '))
sungjuk_list.append([kor,eng,mat,kor+eng+mat,(kor+eng+mat)/3])
kor = float(input('국어 점수 : '))
eng = float(input('영어 점수 : '))
mat = float(input('수학 점수 : '))
sungjuk_list.append([kor,eng,mat,kor+eng+mat,(kor+eng+mat)/3])
kor = float(input('국어 점수 : '))
eng = float(input('영어 점수 : '))
mat = float(input('수학 점수 : '))
sungjuk_list.append([kor,eng,mat,kor+eng+mat,(kor+eng+mat)/3])
total_score = sungjuk_list[0][3]+sungjuk_list[1][3]+sungjuk_list[2][3]
average_score = total_score/9
# 출력서식 : %로 시작, 자료형별로 지정 영문자 사용(int:d, o, x, float: f, e, str: s, bool : b)
# %d, %s, %f 로 표기함
# 필요시 % 출력자리수포맷 문자로 사용할 수 있음 : %10d ( 정수를 10칸 차지하면서 출력을 의미함)
# 실수형일 때는 소숫점 아래 자릿수도 지정할 수 있음 : %.2f (소숫점 아래 둘째짜리까지 부동소숫점형으로 출력)
# 또는 %10.2f(전체 10칸 차지하면서 소수점 아래 둘째짜리까지 부동소숫점형으로 출력 의미함)
print('|{:7.2f}|{:7.2f}|{:7.2f}|{:7.2f}|{:7.2f}|'\
      .format(sungjuk_list[0][0],sungjuk_list[0][1],sungjuk_list[0][2],sungjuk_list[0][3],sungjuk_list[0][4]))
# |  12.00|  13.00|  14.00|  39.00|  13.00|
print('|{:7.2f}|{:7.2f}|{:7.2f}|{:7.2f}|{:7.2f}|'\
      .format(sungjuk_list[1][0],sungjuk_list[1][1],sungjuk_list[1][2],sungjuk_list[1][3],sungjuk_list[1][4]))
# |  15.00|  16.00|  17.00|  48.00|  16.00|
print('|{:7.2f}|{:7.2f}|{:7.2f}|{:7.2f}|{:7.2f}|'\
      .format(sungjuk_list[2][0],sungjuk_list[2][1],sungjuk_list[2][2],sungjuk_list[2][3],sungjuk_list[2][4]))
# |  18.00|  19.00|  20.00|  57.00|  19.00|
print('전체 총점 : %10.2f , 전체 평균 : %10.2f' % (total_score,average_score))
# 전체 총점 :     144.00 , 전체 평균 :      16.00