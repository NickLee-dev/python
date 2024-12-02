# pandas_test6.py

import pandas as pd
import numpy as np
import seaborn as sns # pip install seaborn

# 데이터프레임 데이터 조작

# 데이터 갯수 세기 : count()
# NaN 은 세지 않음
s = pd.Series(range(10)) # 1차원 배열 + 인덱스라벨
#print(s)
'''
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
9    9
dtype: int64
'''
s[3] = np.nan # index 3에 NaN 을 기록함 (값 변경)
#print(s)
'''
0    0.0
1    1.0
2    2.0
3    NaN
4    4.0
5    5.0
6    6.0
7    7.0
8    8.0
9    9.0
dtype: float64
'''
# print(s.count()) # 9

# 데이터프레임에 count() 는 각 열의 데이터 갯수를 센다.
# 데이터프레임에 값이 누락된 부분을 찾을 때 유용하게 이용함
np.random.seed(2)  # 발생 난수 값 고정 알고리즘 지정함
df = pd.DataFrame(np.random.randint(5,size=(4,4)), dtype=float)
# print(df)
'''
     0    1    2    3
0  0.0  0.0  3.0  2.0
1  3.0  0.0  2.0  1.0
2  3.0  2.0  4.0  4.0
3  4.0  3.0  4.0  2.0
'''
df.iloc[2,3] = np.nan
# print(df)
'''
     0    1    2    3
0  0.0  0.0  3.0  2.0
1  3.0  0.0  2.0  1.0
2  3.0  2.0  4.0  NaN
3  4.0  3.0  4.0  2.0
'''
# print(df.count()) # result type : Series, 각 열의 데이터 갯수임
'''
0    4
1    4
2    4
3    3
dtype: int64
'''

# 타이타닉호 승객 데이터를 데이터프레임으로 만들기 위해 seaborn 패키지 사용함
titanic = sns.load_dataset('titanic')
# print(titanic.head())
'''
   survived  pclass     sex   age  ...  deck  embark_town  alive  alone
0         0       3    male  22.0  ...   NaN  Southampton     no  False
1         1       1  female  38.0  ...     C    Cherbourg    yes  False
2         1       3  female  26.0  ...   NaN  Southampton    yes   True
3         1       1  female  35.0  ...     C  Southampton    yes  False
4         0       3    male  35.0  ...   NaN  Southampton     no   True
[5 rows x 15 columns]
'''
# print(titanic)  # [891 rows x 15 columns]

# 카테고리 갯수 세기 : value_counts() 함수 사용
# 시리즈의 값이 정수, 문자열로 된 카테고리 갯수를 반환함
# 카테고리 : 값을 종류별로 구분한 것
np.random.seed(1) # 랜덤하게 출력하는 값을 고정으로 출력
s2 = pd.Series(np.random.randint(6,size=100))  # 0~5사이의 정수 100개 발생
# print(s2.tail()) # 마지막 5개 출력
'''
95    4
96    5
97    2
98    4
99    3
dtype: int32
'''
# print(s2.value_counts()) # 발생값 별로 카운트한 결과가 출력됨
'''
1    22
0    18
4    17
5    16
3    14
2    13
Name: count, dtype: int64
'''

# 데이터프레임에는 value_counts() 함수가 없음
# 각 열(하나의 시리즈임)마다 별도로 적용해야 함
# print(df)
'''
     0    1    2    3
0  0.0  0.0  3.0  2.0
1  3.0  0.0  2.0  1.0
2  3.0  2.0  4.0  NaN
3  4.0  3.0  4.0  2.0
'''
# print(df[0].value_counts())
'''
0
3.0    2
0.0    1
4.0    1
Name: count, dtype: int64
'''

# 정렬 : sort_index(), sort_values() 함수
# sort_index() 함수 : 값을 정렬하고 난 다음에 index 배치를 확인
# sort_values() 함수 : 정렬하고 난 값들의 확인

# s2 시리즈의 값에 따른 데이터 갯수를 인덱스에 따라 정렬한다면
# print(s2) # 0~5의 숫자 100개가 Series 타입으로 되어있음
# print(s2.value_counts()) # 카테고리별 갯수 출력
# print(s2.value_counts().sort_index()) # 인덱스 순으로 정렬
# print(s2.value_counts().sort_values(ascending=False)) # 값순으로 정렬 + 내림차순

# NaN 값이 있는 경우에는 정렬하면 NaN 이 가장 나중에 배치됨
# print(s)
# print(s.sort_values()) # 값으로 정렬 NaN은 제일 하단에 배치됨

# 내림차순정렬하면, ascending=False로 지정하면 됨
# print(s.sort_values(ascending=False)) # NaN은 마지막에 위치함

# 데이터프레임처럼 여러 컬럼(열 : 하나의 시리즈임)을 가진 경우에는
# sort_values()로 정렬시에 by 매개변수로 정렬 기준이 되는 컬럼을 지정할 수 있음
# print(df)
'''
     0    1    2    3
0  0.0  0.0  3.0  2.0
1  3.0  0.0  2.0  1.0
2  3.0  2.0  4.0  NaN
3  4.0  3.0  4.0  2.0
'''
# print(df.sort_values(by=3))  # 3번열을 기준으로 정령됨
'''
     0    1    2    3
1  3.0  0.0  2.0  1.0
0  0.0  0.0  3.0  2.0
3  4.0  3.0  4.0  2.0
2  3.0  2.0  4.0  NaN
'''

# 첫번째 기준열로 정렬하고 나서, 첫번째 기준 열의 같은 값들에 대해
# 두번째 기준 열로 다시 정렬하게 하려면, by 인수에 리스트를 사용해서 순서대로 열을 나열하면 됨
# print(df.sort_values(by=[1,2]))
'''
     0    1    2    3
1  3.0  0.0  2.0  1.0
0  0.0  0.0  3.0  2.0
2  3.0  2.0  4.0  NaN
3  4.0  3.0  4.0  2.0
'''
# print(df.sort_values(by=[1,2], ascending=[False,True]))
'''
     0    1    2    3
3  4.0  3.0  4.0  2.0
2  3.0  2.0  4.0  NaN
1  3.0  0.0  2.0  1.0
0  0.0  0.0  3.0  2.0
'''

# 행, 열 합계 : sum() 함수
# 행과 열의 합계를 구할 때 sum(axis=숫자) 사용
# axis인수에는 합계로 없어지는 방향쪽을 지정함 : 0 - 행(열별합계), 1 - 열(행별합계)
np.random.seed(1)
df2 = pd.DataFrame(np.random.randint(10,size=(4,8))) # 4행 8열로 0~9 사이의 정수로 초기화(랜덤)
print(df2)
'''
   0  1  2  3  4  5  6  7
0  5  8  9  5  0  0  1  7
1  6  9  2  4  5  2  4  2
2  4  7  7  9  1  7  0  6
3  9  9  7  6  9  1  0  1
'''
# 행방향으로 합계를 구할때는 sum(axis=1) 로 지정함
print(df2.sum(axis=1)) # 행별 합계
'''
0    35
1    34
2    41
3    42
dtype: int64
'''
print(df2.sum(axis=0)) # 열별 합계
'''
0    24
1    33
2    25
3    24
4    15
5    10
6     5
7    16
dtype: int64
'''

# 행별 합계를 구하면서, 컬럼 하나를 추가하면서 합계 결과를 출력한다면
df2['RowSum'] = df2.sum(axis=1)
print(df2)
'''
   0  1  2  3  4  5  6  7  RowSum
0  5  8  9  5  0  0  1  7      35
1  6  9  2  4  5  2  4  2      34
2  4  7  7  9  1  7  0  6      41
3  9  9  7  6  9  1  0  1      42
'''

# 열별 합계를 출력할 행을 추가하고, 열방향 (세로) 합계를 구하는 방식도 가능
print(df2.sum()) # axis 가 생략되면, 기본값이 0임
df2.loc['colTotal',:] = df2.sum()
print(df2)
'''
             0     1     2     3     4     5    6     7  RowSum
0          5.0   8.0   9.0   5.0   0.0   0.0  1.0   7.0    35.0
1          6.0   9.0   2.0   4.0   5.0   2.0  4.0   2.0    34.0
2          4.0   7.0   7.0   9.0   1.0   7.0  0.0   6.0    41.0
3          9.0   9.0   7.0   6.0   9.0   1.0  0.0   1.0    42.0
colTotal  24.0  33.0  25.0  24.0  15.0  10.0  5.0  16.0   152.0
'''

# 평균 : mean(), 갯수 : count(), 합계 : sum() 사용하면 됨
# apply() 함수
# 행이나 열 단위로 좀 더 복잡한 계산을 적용하고자 할 때 사용함
# 복잡한 계산식은 람다함수를 사용함
df3 = pd.DataFrame({
    'A':[1,3,4,3,4],
    'B':[2,3,1,2,3],
    'C':[1,3,2,4,4]
})
print(df3)
'''
   A  B  C
0  1  2  1
1  3  3  3
2  4  1  2
3  3  2  4
4  4  3  4
'''

# 예 : 각 열의 최대값과 최소값의 차이를 구한다면
print(df3.apply(lambda x: x.max() - x.min()))
'''
A    3
B    2
C    3
dtype: int64
'''
# 예 : 각 행의 최대값과 최소값의 차이를 구한다면
print(df3.apply(lambda x: x.max() - x.min(),axis=1))
'''
0    1
1    0
2    3
3    2
4    1
dtype: int64
'''
# 예 : 각 열의 값을 빈도수를 구한다면
print(df3.apply(lambda x: x.value_counts(),axis=0))
'''
     A    B  C
1  1.0  1.0  1
2  NaN  2.0  1
3  2.0  2.0  1
4  2.0  NaN  2
'''
# 타이타닉호의 승객 중 나이 20살 기준으로
# 20살 이상이면 성인(adult), 20살 미만이면 미성년자(child)로 구별하고
# 라벨링된 컬럼을 추가해서 표시되게 한다면
titanic['adult|child'] = titanic.apply(lambda r:'adult' if r.age >= 20 else 'child', axis=1)
print(titanic.tail(10))
'''
     survived  pclass     sex   age  ...  embark_town  alive  alone adult|child
881         0       3    male  33.0  ...  Southampton     no   True       adult
882         0       3  female  22.0  ...  Southampton     no   True       adult
883         0       2    male  28.0  ...  Southampton     no   True       adult
884         0       3    male  25.0  ...  Southampton     no   True       adult
885         0       3  female  39.0  ...   Queenstown     no  False       adult
886         0       2    male  27.0  ...  Southampton     no   True       adult
887         1       1  female  19.0  ...  Southampton    yes   True       child
888         0       3  female   NaN  ...  Southampton     no  False       child
889         1       1    male  26.0  ...    Cherbourg    yes   True       adult
890         0       3    male  32.0  ...   Queenstown     no   True       adult
'''

# fillna() 함수
# NaN을 원하는 값으로 바꿀 때 사용
print(df3.apply(lambda x: x.value_counts(),axis=0).fillna(0.0).astype(int))
# astype() 함수 : 전체 데이터의 자료형을 바꿀 때 사용
'''
   A  B  C
1  1  1  1
2  0  2  1
3  2  2  1
4  2  0  2
'''

# 실수값을 카테고리 값(컬럼단위)으로 변환
# cut() 함수 : 실수값을 경계선으로 지정하는 경우
# qcut() 함수 : 갯수가 똑같은 구간으로 분류하는 경우

# 예 : 나이 데이터를 가진 리스트의 경우
ages = [0,32,31,2,20,48,88,54,45,32,11,3]
# cut() 을 사용해서 카테고리(열) 값으로 변경할 수 있음
# bins 인수로 분류하는 기준값을 지정함. 기준을 넘는 값은 NaN이 됨
bins = [1,20,30,50,70,100]
labels = ['미성년자','청년','중년','장년','노년']
result = pd.cut(ages, bins, labels=labels)
print(result)
'''
[NaN, '중년', '중년', '미성년자', '미성년자', ..., '장년', '중년', '중년', '미성년자', '미성년자']
Length: 12
Categories (5, object): ['미성년자' < '청년' < '중년' < '장년' < '노년']
'''
print(type(result)) # <class 'pandas.core.arrays.categorical.Categorical'>

# cut() 의 반환 자료형이 Categorical 클래스 객체임
# 이 객체는 categories 속성으로 라벨 문자열을, codes 속성으로 정수로 인코딩된 값을 확인함
print(result.categories) # Index(['미성년자', '청년', '중년', '장년', '노년'], dtype='object')
print(result.codes) # [-1  2  2  0  0  2  4  3  2  2  0  0]

# 위 결과를 데이터프레임에 적용한다면
df4 = pd.DataFrame(ages,columns=['ages'])
print(df4)
'''
    ages
0      0
1     32
2     31
3      2
4     20
5     48
6     88
7     54
8     45
9     32
10    11
11     3
'''
df4['age_category'] = pd.cut(df4.ages, bins, labels=labels)
print(df4)
'''
    ages age_category
0      0          NaN
1     32           중년
2     31           중년
3      2         미성년자
4     20         미성년자
5     48           중년
6     88           노년
7     54           장년
8     45           중년
9     32           중년
10    11         미성년자
11     3         미성년자
'''
print(type(df4['age_category']))  # <class 'pandas.core.series.Series'> # Categorical형에서 Series로 변환

# 데이터 프레임의 age_category 열의 값은 문자열이 아님 => 문자열로 바꾸려면
print(df4.age_category.astype(str))
'''
0      nan
1       중년
2       중년
3     미성년자
4     미성년자
5       중년
6       노년
7       장년
8       중년
9       중년
10    미성년자
11    미성년자
Name: age_category, dtype: object
'''
# 확인 : 문자열 + 문자열 => 문자열, 'a'+'b'=>'ab'
print(df4.age_category.astype(str)+df4.age_category.astype(str))
'''
0       nannan
1         중년중년
2         중년중년
3     미성년자미성년자
4     미성년자미성년자
5         중년중년
6         노년노년
7         장년장년
8         중년중년
9         중년중년
10    미성년자미성년자
11    미성년자미성년자
Name: age_category, dtype: object
'''

# qcut() 함수
# 구간 경계선을 지정하지 않고, 데이터 갯수가 같도록 갯수로 구간을 나누는 함수임
# 예 : 1000개의 데이터를 4개의 구간으로 나눈다면, 각 구간에 250개씩 나누어짐
data = np.random.randn(1000)
print(data)
data_qcut = pd.qcut(data,4,labels=['Q1','Q2','Q3','Q4'])
print(data_qcut)
'''
['Q2', 'Q1', 'Q2', 'Q3', 'Q1', ..., 'Q1', 'Q1', 'Q4', 'Q4', 'Q2']  # 각 숫자가 어디 구간에 해당하는지 표시
Length: 1000
Categories (4, object): ['Q1' < 'Q2' < 'Q3' < 'Q4']
'''
print(type(data_qcut)) # <class 'pandas.core.arrays.categorical.Categorical'>
print(pd.value_counts(data_qcut))
'''
Q1    250
Q2    250
Q3    250
Q4    250
Name: count, dtype: int64
'''