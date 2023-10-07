import pandas as pd
import numpy as np
from datetime import datetime

df = pd.read_csv('제11회 산업통상자원부 공공데이터활용 BI공모전_빅데이터 분석 과제 5_데이터.csv')

#날짜 리스트 생성
date_list = list(set(df['일자']))

#발전소 리스트 생성
power_code_list = list(set(df['발전소코드']))

#시간대 생성
time_list = []
for i in range(0,24,1) : 
    time = str(i)+':00'
    time_list.append(time)
time_list.append('합계')

#구분
real_list = ['실측','예측']


#데이터  프레임 생성
data_dict = {'Date':[], 'Power_Code':[], 'Power_Volume(kw)':[], 
        '0:00_Real':[], '1:00_Real':[],'2:00_Real':[],'3:00_Real':[],'4:00_Real':[],'5:00_Real':[],
        '6:00_Real':[],'7:00_Real':[],'8:00_Real':[],'9:00_Real':[],'10:00_Real':[],'11:00_Real':[],
        '12:00_Real':[],'13:00_Real':[], '14:00_Real':[],'15:00_Real':[],'16:00_Real':[],'17:00_Real':[],
        '18:00_Real':[],'19:00_Real':[],'20:00_Real':[],'21:00_Real':[],'22:00_Real':[],'23:00_Real':[], 'Sum_Real':[],
        '0:00_Pred':[], '1:00_Pred':[],'2:00_Pred':[],'3:00_Pred':[],'4:00_Pred':[],'5:00_Pred':[],
        '6:00_Pred':[],'7:00_Pred':[],'8:00_Pred':[],'9:00_Pred':[],'10:00_Pred':[],'11:00_Pred':[],
        '12:00_Pred':[],'13:00_Pred':[], '14:00_Pred':[],'15:00_Pred':[],'16:00_Pred':[],'17:00_Pred':[],
        '18:00_Pred':[],'19:00_Pred':[],'20:00_Pred':[],'21:00_Pred':[],'22:00_Pred':[],'23:00_Pred':[], 'Sum_Pred':[]}
data = pd.DataFrame(data_dict)


#데이터 삽입
i = 1
for date in date_list : 
    for power_code in power_code_list : 
        time_real = []
        for real in real_list :
            data_real = df[df.일자==date][df.발전소코드==power_code][df.구분1==real][df.columns]
            for time in time_list:
                time_real.append(str(data_real[time].to_list()[0]).replace('-','0'))
        newdata = {
        'Date':date, 'Power_Code':power_code, 'Power_Volume(kw)':data_real['발전소용량(KW)'].to_list()[0],
        '0:00_Real':float(time_real[0]),'1:00_Real':float(time_real[1]),'2:00_Real':float(time_real[2]),'3:00_Real':float(time_real[3]),
        '4:00_Real':float(time_real[4]),'5:00_Real':float(time_real[5]),'6:00_Real':float(time_real[6]),'7:00_Real':float(time_real[7]),
        '8:00_Real':float(time_real[8]),'9:00_Real':float(time_real[9]),'10:00_Real':float(time_real[10]),'11:00_Real':float(time_real[11]),
        '12:00_Real':float(time_real[12]),'13:00_Real':float(time_real[13]),'14:00_Real':float(time_real[14]),'15:00_Real':float(time_real[15]),
        '16:00_Real':float(time_real[16]),'17:00_Real':float(time_real[17]),'18:00_Real':float(time_real[18]),'19:00_Real':float(time_real[19]),
        '20:00_Real':float(time_real[20]),'21:00_Real':float(time_real[21]),'22:00_Real':float(time_real[22]),'23:00_Real':float(time_real[23]),
        'Sum_Real':float(time_real[24]),
        '0:00_Pred':float(time_real[25]), '1:00_Pred':float(time_real[26]),'2:00_Pred':float(time_real[27]),'3:00_Pred':float(time_real[28]),
        '4:00_Pred':float(time_real[29]),'5:00_Pred':float(time_real[30]),'6:00_Pred':float(time_real[31]),'7:00_Pred':float(time_real[32]),
        '8:00_Pred':float(time_real[33]),'9:00_Pred':float(time_real[34]),'10:00_Pred':float(time_real[35]),'11:00_Pred':float(time_real[36]),
        '12:00_Pred':float(time_real[37]),'13:00_Pred':float(time_real[38]), '14:00_Pred':float(time_real[39]),'15:00_Pred':float(time_real[40]),
        '16:00_Pred':float(time_real[41]),'17:00_Pred':float(time_real[42]),'18:00_Pred':float(time_real[43]),'19:00_Pred':float(time_real[44]),
        '20:00_Pred':float(time_real[45]),'21:00_Pred':float(time_real[46]),'22:00_Pred':float(time_real[47]),'23:00_Pred':float(time_real[48]),
        'Sum_Real':float(time_real[49])}

        data = data.append(newdata, ignore_index=True)

        # data.to_csv('2023공모전데이터'+'_'+str(i)+'.csv')
        print(i)
        i = i+1      
        

#csv로 추출
data.to_csv('2023공모전데이터.csv')
