# -*- coding:utf-8 -*-
# @Time : 2021/11/25 8:56
# @Author: ShuhuiLin
# @File : utils.py

import pandas as pd
import datetime

dir_path = '../data'

def importData_Ver1(file_path):
    df = pd.read_csv(file_path, header=0, index_col=0)
    df["采集时段"] = df["采集时段"].apply(lambda x: datetime.datetime.strptime(x[:-7], '%Y-%m-%d %H:%M'))
    df.index = df['采集时段']
    del df['采集时段']
    return df

def importData_Ver2(file_path):
    df = pd.read_csv(file_path, header=0, index_col=0)
    df["采集时间"] = df["采集时间"].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f'))
    df.index = df['采集时间']
    del df['采集时间']
    return df

def getMaxWindSpedTime(date):
    file_path = dir_path + '/' + date + '/' + 'final.csv'
    df = importData_Ver1(file_path=file_path)
    maxWindSped = df['总风速'].max()
    maxWindSpedTime = df[df['总风速']==maxWindSped].index[0]
    return maxWindSpedTime



def getWindSped(time_point, date):
    file_path = dir_path + '/' + date + '/' + 'final.csv'
    df = importData_Ver1(file_path=file_path)
    WindSped = df[df.index==time_point]['总风速'][0]
    return WindSped

def getWindowData(start_time, date, type='跨中横向加速度', duration=10):
    '''
    :param start_time: window starts from 'start_time'
    :param duration:  select data between [start_time, start_time+duration]
    :return:
    '''
    file_path = '../../浦仪夹江大桥数据' + date + '/processed_data/tmp/' + type + '.csv'
    df = importData_Ver2(file_path)
    stop_time = start_time + datetime.timedelta(minutes=duration)
    window_df = df[(df.index.__ge__(start_time))*(df.index.__le__(stop_time))]
    print('缺失值情况：')
    print(window_df.isnull().sum())
    window_df.fillna(method='ffill', axis=0, inplace=True)
    window_df.dropna(how='any', axis=0, inplace=True)
    return window_df

if __name__ == '__main__':
    maxWindSpedTime = getMaxWindSpedTime(date ='4.27')
    time_point = datetime.datetime(2021, 4, 28, 0, 0, 0)
    WindSped = getWindSped(time_point, date='4.27')
    print(maxWindSpedTime, WindSped)
    # df = getWindowData(time_point, '4.27', type='跨中横向加速度', duration=10)
    # print(df)

