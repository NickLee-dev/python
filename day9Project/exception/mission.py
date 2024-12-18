# path : exceiption\\mission.py
# 예외처리 실습문제

# 2단에서 9단까지의 구구단을 선택해서 한개의 단을 출력처리함
# 키보드로 출력할 단을 입력받아서 진행함
# 입력된 단수는 정수여야 함 (예외처리)
# 입력된 단수는  2~ 9 사이의 값이여야 구구단 출력됨
# 입력된 단수가 2보다 작으면 단수는 2로 처리함
# 입력된 단수가 9보다 크면 단수는 9로 처리함
# try: except: else: finally: 형식으로 작성함

def gugudan():
    try:
        dan = int(input('단을 입력해 주세요 : '))
    except ValueError as msg:
        print('정수만 입력해 주세요.',msg)
    except Exception as msg:
        print('예상치 못한 에러 발생함',msg)
    else:
        if dan < 2 :
            for a in range(1,10):
                print(f'2*{a}={2*a}')
        elif dan > 9 :
            for b in range(1,10):
                print(f'9*{b}={9*b}')
        else :
            for c in range(1,10):
                print(f'{dan}*{c}={dan*c}')
    finally:
        print('구구단 출력 종료. -----------------------')
if __name__ == '__main__':
    gugudan()