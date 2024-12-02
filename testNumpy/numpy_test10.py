# numpy_test10.py

import numpy as np
# 기술 통계 (descriptive statistics) : 통계 계산용 함수를 말함
# 데이터 갯수(count), 평균(mean, average), 분산(variance), 표준편차(standard deviation)
# 최대값(maximum), 최소값(minimum), 중앙값(median), 사분위수(quartile)

x = np.array([1,5,4,78,9,32,42,-1564,-1123,-13,42,3,8,42,33,245,4,32,423,78,9,198,898,53,735,76,357,537,86,789,4,635,51,896,4,98,498,11,8911,189,4])
print(x)

# 데이터 갯수 : len()
print(len(x)) # 41

# 평균 : np.mean(배열변수)
print(np.mean(x))  # 327.3170731707317

# 표본 분산 (sample variance) : 데이터와 평균 간의 거리의 제곱의 평균
print(np.var(x))  # 2022508.704342653
print(np.var(x,ddof=1))  # 2073071.4219512194 # 비편향분산

# 표준 편차 : 표본 분산의 양의 제곱근, ss 라고 표시함
print(np.std(x)) # 1422.1493256134015

# 최대값, 최소값, 중앙값
print(np.max(x))    # 8911
print(np.min(x))    # -1564
print(np.median(x)) # 42.0

# 사분위수
# 데이터를 오름차순정렬했을 때, 1/4, 2/4, 3/4, 4/4 위치에 있는 값을 말함
# 1사분위, 2사분위, 3사분위, 4사분위라고 함
# 데이터 갯수가 100개이면, 1사분위는 25번째 값이 됨
print(np.percentile(x, 0))  # 최소값이 됨
print(np.percentile(x, 25))  # 1사분위
print(np.percentile(x, 50))  # 2사분위
print(np.percentile(x, 75))  # 3사분위
print(np.percentile(x, 100))  # 4사분위(최대값)

# 난수 발생과 카운팅
# 난수 (random number) : 프로세스가 임의로 발생시키는 숫자
# numpy에서 random 서브 패키지에서 함수들이 제공됨

# np.random.seed(인수)
# seed : 난수의 시작값
# 인수 : 정수 >= 0 사용함
np.random.seed(0) # 난수의 시작값 지정

# np.random.rand(갯수)
# 값의 범위 : 0.0 <= 난수 < 1.0
print(np.random.rand(5))
print(np.random.rand(5))

# 데이터 섞기 (shuffle)
x = np.arange(10)
np.random.shuffle(x)
print(x) # [5 2 3 4 1 0 9 8 7 6]
