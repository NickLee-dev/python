# path : test_matplotlib.py
# module : test_matplotlib
# matplotlib 모듈 사용한 시각화 테스트

# matplotlib 패키지 설치함 : pip install matplotlib
import matplotlib as mpl    #
import matplotlib.pyplot as plt # plot = 그래프(차트를 의미)

def test_plot1():
    "간단한 plot 그리기 : 기본은 선 그래프(line plot)"
    # 그래프로 표현할 데이터는 리스트 또는 배열이어야 함
    # 배열은 numpy사용해야함
    data = [1,4,9,16]
    plt.title('Line Plot')      # 그래프 제목 지정 함수
    plt.plot(data)              # 선 그래프를 만드는 함수
    # 리스트가 하나이면 y축 값으로 사용됨
    plt.show()                  # 선 그래프 생성 함수 /plots view에서 확인가능(파이참)

def test_plot2():
    "x축과 y축을 리스트로 만들어서 그래프 만들기"
    # title('표시할 제목') : 그래프 제목 지정 함수
    # x 축 값도 함께 지정 : plot([x축값들],[y축값들])
    x_data = [10,20,30,40]
    y_data = [1,4,9,16]
    plt.title('x tics')
    plt.plot(x_data, y_data)
    plt.show()

# 그래프에 한글을 사용하려면, 한글 폰트 파일을 다운받아서 사용함 ------------------------------------------------
import matplotlib.font_manager as fm


def test_fonts():
    # 라이브러리 자원(설치한 패키지의 자원) 저장 폴더 확인하기
    print(mpl.matplotlib_fname())
    # D:\python_workspace\testVisualization\.venv\Lib\site-packages\matplotlib\mpl-data\matplotlibrc
    # matplotlib 모듈에서 다운받은 글꼴은 그래프(plot)의 기본 글꼴로 사용하게 하려면,
    # D:\python_workspace\testVisualization\.venv\Lib\site-packages\matplotlib\mpl-data\fonts/ttf 폴더 확인
    # ttf 폴더 안에 다운받은 글꼴 파일을 복사해 넣음
    # 참고 : 압축 푼 ttf 파일을 더블 클릭해서 설치 버튼 누르고 설치한 경우에는
    # c:/windows/fonts 에 기본 설치됨

    # 글꼴 파일 복사해 넣고나서, matplotlib 캐시에 변경 내용 반영함
    # 1. 캐시 파일 저장 위치 확인함
    print(mpl.get_cachedir())       # C:\Users\ict01-13\.matplotlib
    # 2. 해당 위치의 캐시 파일을 직접 파일 탐색기로 찾아내서 삭제함
    # => 이전 폰트리스트 정보를 가진 캐시이므로 캐시삭제 필요
    # 3. 프로그램 다시 실행(shift + F10) 하면 캐시 파일 생김 > 파일 탐색기에서 확인함
    # => 만약, 캐시파일 안 생기면 컴퓨터 리부팅함

def test_fonts2():
    # 폰트 설정 :
    # 첫번째 방법 : rc parameter 를 설정해서, 설정 이후 그래프 작업 전체에 사용하게 함

    # 현재 사용되고 있는 폰트 종류와 글자 크기 확인
    print(mpl.rcParams['font.family'])          # 설정된 설정값 확인
    print(mpl.rcParams['font.size'])            # 설정된 글자크기 확인

    # 한글 폰트 설정 변경해 봄
    mpl.rc('font', family='NanumGothic')
    mpl.rc('axes', unicode_minus=False)
    # axes 에 적용되는 유니코드(0~65535) 숫자에 음수 부호 사용

    # 그래프에 설정된 글꼴을 사용 확인
    plt.title('한글 그래프 제목')               # 한글 제목 설정
    plt.plot([10,20,30,40],[1,4,9,16])  # x,y값 리스트 바로입력
    plt.xlabel('x축 제목')                     # x축 라벨 설정
    plt.ylabel('y축 제목')                     # y축 라벨 설정
    plt.show()

def test_fonts3():
    # 그래프의 특정 부분만 원하는 글꼴로 설정을 변경할 수도 있음
    # 이용할 글꼴 파일 위치는 어디든 상관없음
    # 변수명 = 드라이브:/디렉토리경로명/....../글꼴파일이 있는 폴더명/사용할 글꼴 파일명.확장자
    # font_path = 'D:/python_workspace/testVisualization/fonts/NanumGothic.ttf'
    font_path = './fonts/NanumGothicBold.ttf'
    font_prop = fm.FontProperties(fname=font_path)                  # 대문자

    plt.title('예제 그래프', fontproperties=font_prop)          # 소문자
    plt.plot([10,20,30,40],[1,4,9,16])
    plt.xlabel('x축 제목', fontproperties=font_prop)           # 소문자
    plt.ylabel('y축 제목', fontproperties=font_prop)           # 소문자
    plt.show()

def test_fonts4():
    # 각 객체마다 별도의 폰트 적용 : fontdict 인수에 넣어서 사용함
    font1 = {'family': 'NanumGothic', 'size': 24, 'color': 'yellow', 'weight': 'bold'}
    font2 = {'family': 'NanumMyeongjo', 'size': 16, 'color': 'red', 'weight': 'bold'}
    font3 = {'family': 'NanumGothic', 'size': 12, 'color': 'green', 'weight': 'light'}

    plt.title('예제 그래프', fontdict=font1)
    plt.plot([10,20,30,40],[1,4,9,16])
    plt.xlabel('x축 제목',fontdict=font2)
    plt.ylabel('y축 제목', fontdict=font3)
    plt.show()

if __name__ == '__main__':
    # test_plot1()
    # test_plot2()
    # test_fonts()
    # test_fonts2()
    # test_fonts3()
    test_fonts4()