# -*- coding:utf-8 -*-
# @Time : 2021/11/16 17:18
# @Author: ShuhuiLin
# @File : Visualization.py

import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from scipy import optimize

class MidSpanData:
    def __init__(self, date=4.27):
        self.date = date
        self.df = self.importData()

    def importData(self):
        # 导入4.27-4.29数据
        df = pd.read_csv("./data/{0}/final.csv".format(self.date), header=0, index_col=0)
        # 时间字段处理
        df["采集时段"] = df["采集时段"].apply(lambda x: datetime.datetime.strptime(x[:-7], '%Y-%m-%d %H:%M'))
        df.index = df['采集时段']
        del df['采集时段']
        return df

    def show(self, x, y):
        # 画时域图
        if x == 'time':
            plt.rcParams['font.sans-serif'] = ['Simhei']
            plt.rcParams['axes.unicode_minus'] = False
            plt.figure(figsize=(15, 4))
            plt.plot(self.df[y], label=y, marker='o', linewidth=2, markersize=4, alpha=0.6)
            # 设置坐标轴刻度的大小
            plt.tick_params(labelsize=12)
            # 设置注释
            plt.legend(loc="best", fontsize=12)
            # 设置标题
            plt.title('{0} - {1}'.format(y, x), fontsize=25, pad=20)
            # 设置横坐标标题
            plt.xlabel(x, fontsize=15, labelpad=10)
            plt.show()

        # 做关联图
        else:
            plt.rcParams['font.sans-serif'] = ['Simhei']
            plt.rcParams['axes.unicode_minus'] = False
            plt.figure(figsize=(15, 7))
            x_data = self.df[x].values
            if type(y) == list:
                colors = ['r', 'b', 'g', 'y', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b',
                          '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
                for i, item in enumerate(y):
                    y_data = self.df[item].values
                    plt.scatter(x_data, y_data, c=colors[i], alpha=0.2, label=item)
                    x_fitting, y_fitting = self.get_fittingCurve(x_data, y_data)
                    plt.plot(x_fitting, y_fitting, c=colors[i], linewidth=2)
            else:
                y_data = self.df[y].values
                plt.scatter(x_data, y_data, c="y", alpha=0.2, label=y)
                x_fitting, y_fitting = self.get_fittingCurve(x_data, y_data)
                plt.plot(x_fitting, y_fitting, c="y", linewidth=2)
            # 设置坐标轴刻度的大小
            plt.tick_params(labelsize=15)
            # 显示图例
            plt.legend(loc="best", fontsize=15)
            # xy轴注释
            plt.xlabel(x, size=20, labelpad=10)
            # plt.ylabel(y, size=20, labelpad=10)
            # 设置标题
            plt.title('{0} - {1}'.format(y, x), fontsize=25, pad=20)
            plt.show()

    #############################################f辅助函数#########################################3
    def f_1(self, x, A, B):
        return A * x + B

    def get_fittingCurve(self, x, y):
        # 加入判断，保证 x和y没有nan
        judg = ~np.isnan(y) * ~np.isnan(x)
        x = x[judg]
        y = y[judg]
        A1, B1 = optimize.curve_fit(self.f_1, x, y)[0]
        x_fitting = np.arange(min(x), max(x), 0.01)  # 30和75要对应x0的两个端点，0.01为步长
        y_fitting = A1 * x_fitting + B1
        return x_fitting, y_fitting






