# pandas_test8.py

import pandas as pd
import numpy as np

# 데이터 프레임 인덱스 조작
# 인덱스 라벨이 없는 데이터프레임에 인덱스 라벨을 설정하거나 제거하는 것
# 행 인덱스와 열 인덱스를 서로 바꿔야 할 때도 인덱스 조작할 수 있음(인덱스 교환)
# set_index() 함수 : 기존의 행 인덱스를 제거하고, 데이터 열 중에서 하나를 행 인덱스로 설정할 때 이용함
#                   한 줄의 컬럼값들 => 행 인덱스 라벨이 됨
# reset_index() 함수 : 기존의 행 인덱스를 제거하고, 인덱스를 데이터 열로 추가함
#                   행 인덱스 라벨 => 한줄의 컬럼값들로 바뀜

np.random.seed(10)
df1 = pd.DataFrame(np.vstack([list('ABCDE'),np.round(np.random.rand(3,5),2)]).T,columns=['C1','C2','C3','C4'])
print(df1)
'''
  C1    C2    C3    C4
0  A  0.77  0.22  0.69
1  B  0.02   0.2  0.95
2  C  0.63  0.76   0.0
3  D  0.75  0.17  0.51
4  E   0.5  0.09  0.81
'''
# set_index() 함수
# 기존의 행 인덱스는 지우고, 특정 열 데이터를 행 인덱스 라벨로 지정하는 함수
df2 = df1.set_index('C1')
print(df2)
'''
      C2    C3    C4
C1                  
A   0.77  0.22  0.69
B   0.02   0.2  0.95
C   0.63  0.76   0.0
D   0.75  0.17  0.51
E    0.5  0.09  0.81
'''
print(df2.set_index('C2'))
'''
        C3    C4
C2              
0.77  0.22  0.69
0.02   0.2  0.95
0.63  0.76   0.0
0.75  0.17  0.51
0.5   0.09  0.81
'''

# reset_index() 함수
# 기존의 행인덱스 라벨을 컬럼값으로 바꿈
print(df2.reset_index())
'''
  C1    C2    C3    C4
0  A  0.77  0.22  0.69
1  B  0.02   0.2  0.95
2  C  0.63  0.76   0.0
3  D  0.75  0.17  0.51
4  E   0.5  0.09  0.81
'''

# drop=True 인수를 설정하면, 행인덱스로 변경된 열이 원래 컬럼으로 돌아오지 않고 지워짐
print(df2.reset_index(drop=True))
'''
     C2    C3    C4
0  0.77  0.22  0.69
1  0.02   0.2  0.95
2  0.63  0.76   0.0
3  0.75  0.17  0.51
4   0.5  0.09  0.81
'''

# 다중인덱스------------------------------------------
# 행이나 열에 여러 계층의 인덱스가 있을 때
# 데이터프레임 생성할 때 columns 인수에 리스트에 리스트(행렬)로 인덱스 설정한 경우
np.random.seed(8)
df3 = pd.DataFrame(np.round(np.random.randn(5,4),2),columns=[['A','A','B','B'],['C1','C2','C3','C4']])
print(df3)
'''
      A           B      
     C1    C2    C3    C4
0  0.09  1.09 -1.95 -1.39
1 -2.30  2.41  1.73  2.20
2  0.79  0.98 -1.18  1.92
3 -1.12 -0.66 -0.38 -0.79
4  0.86 -0.23 -0.07 -0.21
'''
# columns.names 속성
# 다중 인덱스에 이름 지정시 이름들도 리스트고 설정함
df3.columns.names =['Cidx1','Cidx2']
print(df3)
'''
Cidx1     A           B      
Cidx2    C1    C2    C3    C4
0      0.09  1.09 -1.95 -1.39
1     -2.30  2.41  1.73  2.20
2      0.79  0.98 -1.18  1.92
3     -1.12 -0.66 -0.38 -0.79
4      0.86 -0.23 -0.07 -0.21
'''

# 행 인덱스도 다중 인덱스로 설정할 수 있음. 일므도 지정할 수 있음 (index.names 사용)
np.random.seed(8)
df4 = pd.DataFrame(np.round(np.random.randn(6,4),2),
                   columns=[["A","A","B","B"],['C1','C2','C3','C4']],
                   index=[['M','M','M','F','F','F'],['id_' + str(i+1) for i in range(3)]*2])
df4.columns.names =['Cidx1','Cidx2']
df4.index.names =['Ridx1','Ridx2']
print(df4)
'''
Cidx1           A           B      
Cidx2          C1    C2    C3    C4
Ridx1 Ridx2                        
M     id_1   0.09  1.09 -1.95 -1.39
      id_2  -2.30  2.41  1.73  2.20
      id_3   0.79  0.98 -1.18  1.92
F     id_1  -1.12 -0.66 -0.38 -0.79
      id_2   0.86 -0.23 -0.07 -0.21
      id_3   1.35 -0.61 -0.17  0.42
'''

# 행 인덱스와 열 인덱스 교환 : stack,unstack 사용
# stack(): 열 인덱스 --> 행인덱스로 변환
print(df4.stack('Cidx1')) # 인덱스 이름 사용
'''
Cidx2                C1    C2    C3    C4
Ridx1 Ridx2 Cidx1                        
M     id_1  A      0.09  1.09   NaN   NaN
            B       NaN   NaN -1.95 -1.39
      id_2  A     -2.30  2.41   NaN   NaN
            B       NaN   NaN  1.73  2.20
      id_3  A      0.79  0.98   NaN   NaN
            B       NaN   NaN -1.18  1.92
F     id_1  A     -1.12 -0.66   NaN   NaN
            B       NaN   NaN -0.38 -0.79
      id_2  A      0.86 -0.23   NaN   NaN
            B       NaN   NaN -0.07 -0.21
      id_3  A      1.35 -0.61   NaN   NaN
            B       NaN   NaN -0.17  0.42
'''
# unstack() : 행 인덱스 --> 열인덱스로 변환
print(df4.unstack('Ridx1'))
'''
Cidx1     A                       B                  
Cidx2    C1          C2          C3          C4      
Ridx1     F     M     F     M     F     M     F     M
Ridx2                                                
id_1  -1.12  0.09 -0.66  1.09 -0.38 -1.95 -0.79 -1.39
id_2   0.86 -2.30 -0.23  2.41 -0.07  1.73 -0.21  2.20
id_3   1.35  0.79 -0.61  0.98 -0.17 -1.18  0.42  1.92
'''

# 인덱스 이름이 없으면 인덱스 정수를 사용해도 됨
print(df4.unstack(0))