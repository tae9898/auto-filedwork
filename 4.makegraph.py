import numpy as np
from pandas import read_excel, read_csv, read_table
import pandas as pd
from matplotlib import pyplot as plt
a= open('/make/final1.txt','r')
#detect.py
b= open('/make/test/final.mp4.txt','r')
#gender.py
column_name_1 = ['인원']
column_name_2 = ['응시','남','여','나이']
column_name_3 = ['비율']
dataa = a.readlines()
datab = b.readlines()

data_split_a = [x.strip().split() for x in dataa[0:]]
data_split_b = [x.strip().split() for x in datab[0:]]
df1 = pd.DataFrame(data_split_a, columns = column_name_1).astype(float)
df2 = pd.DataFrame(data_split_b, columns = column_name_2).astype(float)

df11 = pd.DataFrame(data_split_a).astype(float)
df22 = pd.DataFrame(data_split_b).astype(float)




result3 = pd.concat([df1,df2],axis=1)
#print(result3)

#필요한 시간대 범위지정, 단위지정
small_range = list(range(1120,1320,10))
a1 = result3.loc[1640:1740,['남','여']]
a1.plot(linestyle='-')
plt.show()

#csv파일로 저장
#result3.to_csv('/make/hello.csv')

