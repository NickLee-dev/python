# path : loop/list_in_for.py    or    loop\\list_in_for.py
# module : loop.list_in_for
# 리스트 내포 (리스트 안의 for) 테스트용 스크립트

# 리스트 안에 값 추가를 위한 for 문을 포함하는 구문
# 작성형식 : [기록할값 for 변수 in 시퀀스객체]
# 주의 : 기록할 값과 변수의 이름이 반드시 같아야 함
# 시퀀스 객체(Iterable) : 순차적으로 값을 저장한 객체(str, list, tuple, set, dict.keys(), dict.values())
# 시퀀스 객체 대신에 range(시작값(생략가능/기본값0), 끝값, 간격(생략가능/기본값1)) 함수 사용 가능함

# 리스트에 값 기록방법 1 : append() 사용
def list_append():
    sample_list = list()    # sample_list = []
    for n in range(1,6):
        sample_list.append(n)
    print(sample_list)

# 리스트 내포로 변경
def list_append2():
    sample_list = [n for n in range(1,6)]    # 리스트 내포일 경우 함수 사용 불가
    print(sample_list)

# 리스트 내포시에 if문도 같이 포함 가능
def list_append3():
    sample_list = list()
    for n in range(1,11):
        if n % 2 == 0:
            sample_list.append(n)
    print(sample_list)
# 리스트 내포로 변경
def list_append4():
    sample_list = [n for n in range(1,11) if n % 2 == 0 ]
    print(sample_list)

# for 문 안에 for 문이 사용되는 경우 (다중 if 문)
def list_append5():
    sample_list = list()
    for n in range(1,6):
        for m in range(1,6):
            sample_list.append(n+m)
    print(sample_list)

# 리스트 내포로 바꾼다면
def list_append6():
    sample_list = [n+m for n in range(1,6) for m in range(1,6)]
    print(sample_list)

# 구구단 2단부터 9단까지 곱하기 한 결과값 리스트에 저장처리
# 리스트 내 포로 작성함
def list_append7():
    sample_list = [dan*su for dan in range(2,10) for su in range(1,10)]
    print(sample_list)

# 이 파일 안에서 작성된 함수를 바로 실행해 보자고 한다면
if __name__ == '__main__': # __name__ 이 __main__ 이 맞는지 확인
    # 함수 실행 구문 작성
    # list_append()
    # list_append2()
    # list_append3()
    # list_append4()
    # list_append5()
    # list_append6()
    list_append7()