# pandas_test4.py

import pandas as pd
import numpy as np

# 데이터 입출력
# pandas 는 DataFrame 정보를 저장할 수 있는 기능을 제공함
# 데이터 파일을 읽어서 DataFrame 만드는 기능도 제공함
# 입출력 파일 종류 : csv, excel(xls), html, json, hdf5, sas, stata, sql
# 쉼표(,)로 데이터를 구분한 텍스트 파일인 csv가 기본으로 다루어짐
# 미래형 데이터 파일은 json 임

data = {
    'c1':[1,2,3],
    'c2':[1.11,2.22,3.33],
    'c3':['one','two','three']
}

df = pd.DataFrame(data)
# print(df)
'''
   c1    c2     c3
0   1  1.11    one
1   2  2.22    two
2   3  3.33  three
'''
# samp1.csv 파일에 df 정보를 저장 처리
# df.to_csv('samp1.csv',mode='w')
'''
,c1,c2,c3
0,1,1.11,one
1,2,2.22,two
2,3,3.33,three
'''

# csv 파일을 읽어서 DataFrame 만들기 : pandas.read_csv() 함수 사용함
df2 = pd.read_csv('samp1.csv')
# print(type(df2)) # <class 'pandas.core.frame.DataFrame'>
# print(df2)
'''
   Unnamed: 0  c1    c2     c3
0           0   1  1.11    one
1           1   2  2.22    two
2           2   3  3.33  three
'''

# 파일에 기록시 컬럼라벨과 행인덱스라벨을 제외할 수도 있음
# df.to_csv('samp2.csv', mode='w', header=False, index=False)

# 데이터 파일을 읽어 들일 때, 컬럼라벨을 추가할 수도 있음
df3 = pd.read_csv('samp1.csv',names=['c1','c2','c3'])
# print(df)
'''
   c1    c2     c3
0   1  1.11    one
1   2  2.22    two
2   3  3.33  three
'''

# 데이터 파일을 읽어 들일 때, 특정 컬럼 값을 인덱스 행라벨로 지정할 수도 있음
df4 = pd.read_csv('samp1.csv',index_col='c1')
# print(df4)
'''
    Unnamed: 0    c2     c3
c1                         
1            0  1.11    one
2            1  2.22    two
3            2  3.33  three
'''

# 파일에 데이터 기록 저장시, 콤마(',') 대신에 원하는 구분기호(seperator)를 지정할 수도 있음
# df.to_csv('samp3.csv',mode='w',sep='\t') # 데이터 간에 공백으로 구분함
'''
	c1	c2	c3
0	1	1.11	one
1	2	2.22	two
2	3	3.33	three
'''

# 공백으로 구분된 데이터 파일을 읽어 들일 때, 구분자가 공백임을 명시해야 함
# 정규표현식(Regular Expression) 문자열을 이용해서 구분자를 지정함
# 공백에 대한 정규 표현식 문자열 : '\s+'
df5 = pd.read_csv('samp3.csv',sep='\s+')
print(df5)

# 파일 안에 건너뛰어야 되는 행이 있다면, skiprows 매개변수 사용함
df6 = pd.read_csv('samp4.csv',skiprows=[0,1]) # 스킵할 행을 리스트로 해서 입력
print(df6)
'''
   Unnamed: 0  c1    c2     c3
0           0   1  1.11    one
1           1   2  2.22    two
2           2   3  3.33  three
'''

# 파일로 부터 읽은 데이터의 특정 값을 NaN 처리할 수도 있음
data2 = {
    'c1':[1,2,3],
    'c2':[1.11,2.22,3.33],
    'c3':['누락','two','three']
}

df7 = pd.DataFrame(data2)  # DataFrame 만들기
# df7.to_csv('samp5.csv',mode='w')  # 파일생성

df8 = pd.read_csv('samp5.csv',na_values=['누락'])
print(df8)
'''
   Unnamed: 0  c1    c2     c3
0           0   1  1.11    NaN
1           1   2  2.22    two
2           2   3  3.33  three
'''

# 반대로 파일에 기록할 때 NaN 표시값을 다른 값으로 바꿀 수도 있음
# df8.to_csv('samp6.csv',na_rep='값없음')

# 데이터프레임에 인덱스라벨 지정
#print(df)
'''
   c1    c2     c3
0   1  1.11    one
1   2  2.22    two
2   3  3.33  three
'''
df.index = ['a','b','c']
# print(df)
'''
   c1    c2     c3
a   1  1.11    one
b   2  2.22    two
c   3  3.33  three
'''

# 인터넷 상에 있는 파일들도 읽어올 수 있음
df9 = pd.read_csv('https://raw.githubusercontent.com/datascienceschool/docker_rpython/master/data/titanic.csv')
print(df9)
print(df9.head())   # 위쪽 5개만
print(df9.tail())   # 아래쪽 5개만
print(df9.columns)  # 컬럼만 공유해 줌