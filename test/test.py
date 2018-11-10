# -*- encoding:utf-8 -*-
# http://nittaku.tistory.com/259?category=734633

import pandas as pd
# import xlrd

df = pd.read_excel('mandoo_management.xlsx',sheet_name='Sheet1')
print(df)
print(df['이름'])
df['근무시간'] = df['퇴근시간']-df['출근시간']
print(df)
df['시간당 만두'] = df['만두생산'] / df['근무시간']
print(df)
df = df.sort_values(by=['시간당 만두','근무시간'],ascending=[False,False])
print(df)

df.to_excel('result.xlsx',sheet_name='Sheet1')

test = df['근무시간']
test.to_excel('asdf.xlsx',sheet_name='Sheet1')

'''
결론적이로, 기본 엑셀파일이 -> pandas를 거쳐 
-> 계산식을 통한 새로운 칼럼추가 및 sorting되어 저장
-> pandas에서 엑셀파일을 열때는 xlrd 모듈이 필요
-> pandas에서 엑셀파일을 저장할 때는 openpyxl 모듈이 필요
'''