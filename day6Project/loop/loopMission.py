# path : loop/loopMission.py  or  loop\\loopMission.py
# module : loop.loopMission

# 연습 1 :
# 리스트 안의 튜플 아이템의 값들에 대해 둘중 큰 값과 작은값을 분류해서 출력 처리

# 방법 1 : 조건식 직접 작성
def practice1():
    nlist = [(12,45),(90,32),(56,19)]
    for n,m in nlist:
        if n > m:
            print(f'큰값 : {n}')
            print(f'작은값 : {m}')
        else :
            print(f'큰값 : {m}')
            print(f'작은값 : {n}')
    print('-----------------------------------')
    for n in nlist:
        if n[0]>n[1] :
            print(f'큰값 : {n[0]}')
            print(f'작은값 : {n[1]}')
        if n[0]<n[1] :
            print(f'큰값 : {n[1]}')
            print(f'작은값 : {n[0]}')

# 방법 2 : 내장함수 이용
def practice2():
    nlist = [(12, 45), (90, 32), (56, 19)]
    for n,m in nlist:
        vmax = max(n,m)
        vmin = min(n,m)
        print(f'큰값 : {vmax}, 작은값 : {vmin}')

# 활용 실습 :
# 리스트 안에 있는 군집 자료형들이 가진 값들 중에서 각각 가장 큰값을 골라내서
# 별도의 리스트에 저장 처리하고 출력 확인

# 조건문을 직접 사용해서 해결
def practice3() :
    lists = [[43,1,20],(22,41,10,73),{12,32,45,3,9}]
    max_list = []
    for i in lists :
        max_value = 0 # 큰값 기록할 변수
        for j in i :
            if max_value < j :
                max_value = j
        max_list.append(max_value)
    print(max_list)


# 내장함수 사용해서 해결 : max(Iterable)
def practice4():
    lists = [[43,1,20],(22,41,10,73),{12,32,45,3,9}]
    max_list = []
    # 각 아이템별로 큰값을 골라내서 max_list에 저장처리
    for i in lists :
        max_list.append(max(i))
    print(max_list)

''' while 문 실습문제
아래의 작성된 for문을 while문으로 변경하시오.
sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]

for student in sungjuk_list:
    if(student[2] >= 60):
        print('{}번 {} 학생은 합격입니다.'.format(student[0], student[1]))
    else:
        print('{}번 {} 학생은 불합격입니다.'.format(student[0], student[1]))
'''
# 1. while 문으로 변경
def practice_while():
    sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]
    i = 0
    while i < len(sungjuk_list):
        i+=1
        if (sungjuk_list[i][2] >= 60):
            print('{}번 {} 학생은 합격입니다.'.format(sungjuk_list[i][0], sungjuk_list[i][1]))
        else:
            print('{}번 {} 학생은 불합격입니다.'.format(sungjuk_list[i][0], sungjuk_list[i][1]))
if __name__ == '__main__':
    # practice1()
    # practice2()
    # practice3()
    # practice4()
    practice_while()