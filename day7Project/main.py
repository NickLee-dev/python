# random test
# 랜덤 : 임의의 숫자(랜덤값)를 발생시키고자 할 때, random 모듈이 제공하는 함수를 사용할 수 있음
import random

def test_random():
    # 0.0 <= 랜덤값 < 1.0 범위의 실수형 값 발생
    print('임의의 랜덤값 :',random.random())

    # start <= 랜덤값 < stop 범위의 정수형 값 발생
    print('랜덤값 확인 :', random.randrange(1,11))

# 1부터 45까지의 임의의 정수 6개를 중복되지 않게 발생시켜서 저장하고
# 오름차순으로 정렬해서 출력 처리
def lotto():
    lotto_set = set()
    while len(lotto_set) < 6:
        lotto_set.add(random.randrange(1,46))
    lotto_list = list(lotto_set)
    lotto_list.sort(reverse=False)
    print(lotto_list)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # test_random()
    lotto()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
