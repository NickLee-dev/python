# test_dict 디렉토리 안에있는 dict_sample.py 파일 안의 함수를 사용하려면
# import 문을 사용해서 임포트 선언해야 함

# 모듈 : 함수를 가지고 있는 파이썬 파일
# import 파일명 => 같은 디렉토리 안의 파일을 임포트할 때
# import 디렉토리명.파일명 => 다른 디렉토리의 파일을 임포트할 때

# import test_dict.dict_sample
# 모듈명이 길거나 복잡하거나 사용시 불편할 경우 줄임말을 지정할 수 있음
# import 모듈명 as 줄임말
import test_dict.dict_sample as ts



# Press the green button in the gutter to run the script.
if __name__ == '__main__':  # 자바의 메인 함수의 역할
    # 임포트한 모듈 안의 함수 사용시 :
    # 임포트한 모듈명 그대로 사용 : 모듈명.함수명()
    # test_dict.dict_sample.test1() # 모듈명에 줄임말이 지정되면 정식 모듈명 사용 못 함
    # ts.test1()
    # ts.test2()
    # ts.test3()
    # ts.test4()
    # ts.test5()
    # ts.test6()
    ts.test7()

# test