
# from sklearn.model_selection import train_test_split, GridSearchCV
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# from sklearn.linear_model import LogisticRegression
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.svm import SVC
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.ensemble import AdaBoostClassifier
# from sklearn.ensemble import GradientBoostingClassifier
# from sklearn.ensemble import ExtraTreesClassifier
# from sklearn.ensemble import VotingClassifier

from pyecharts import options as opts
from pyecharts.charts import Bar, Calendar, Tab, Timeline, Pie, Line, Grid, Page, Liquid
from pyecharts.globals import ThemeType

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
 
if __name__ == '__main__':
    X = []
    for i in range(0,50):
        X.append(i+1)
    
    print(X);    
    
    FC1 = [
        17532, 12623, 25664, 31540, 12526, 17005, 
        19848, 15083, 10886, 13145, 15362, 11719,
        3188, 7124, 4338, 11620, 8948, 7476, 4879, 
        4379, 5035, 3950, 4631, 4126, 6838, 5915, 
        7714, 3446, 4018, 7156, 7170, 8078, 9497, 
        11819, 14234, 19694, 16611, 14100, 14018,
        17311, 5733, 11961, 11043, 6838, 11704, 
        8435, 14693, 8625, 13293, 6122
]
    SC2 = [
        14643, 15566, 16490, 12242, 11185, 9865,
        11977, 6930, 7768, 10574, 6006, 7862, 3944,
        5331, 4515, 3553, 2158, 1556, 3686, 1345, 
        1931, 3650, 3983, 1989, 1843, 1700, 3287, 
        1871, 2376, 3610, 3909, 2681, 5623, 5074, 
        3173, 9596, 8020, 4825, 5243, 9935, 6515, 
        4665, 5269, 1932, 5346, 4292, 4006, 6622, 5262, 2703]
    
    AFM10 = [20547, 14925, 14301, 17015, 13338, 
             23797, 24077, 17299, 14061, 20669, 
             16035, 7910, 5222, 8620, 7252, 10729,
             2929, 1805, 7335, 6699, 2718, 3892, 4315,
             2902, 4719, 4547, 14060, 3290, 4329, 11420,
             7480, 6977, 8590, 9675, 9798, 17631, 13187, 9050, 
             8773, 10428, 5526, 9133, 13553, 6507,
             15017, 9562, 9381, 7912, 9047, 7760
             ]
    
    
    Equipment = [56294/4,56294/4,56294/4,56294/4,
                 49686/4,49686/4,49686/4,49686/4,
                 32474/4,32474/4,32474/4,32474/4,
                 19964/4,19964/4,19964/4,19964/4,
                 41631/4,41631/4,41631/4,41631/4,
                 42167/4,42167/4,42167/4,42167/4,
                 20693/4,20693/4,20693/4,20693/4,
                 68235/4,68235/4,68235/4,68235/4,
                 32530/4,32530/4,32530/4,32530/4,
                 58419/4,58419/4,58419/4,58419/4,
                 42700/4,42700/4,42700/4,42700/4,
                 37591/4,37591/4,37591/4,37591/4,
                 58419/4,58419/4
                 ]
    
    Process = [634530/4,634530/4,634530/4,634530/4,
               662859/4,662859/4,662859/4,662859/4,
               436685/4,436685/4,436685/4,436685/4,
               237501/4,237501/4,237501/4,237501/4,
               204362/4,204362/4,204362/4,204362/4,
               233676/4,233676/4,233676/4,233676/4,
               160594/4,160594/4,160594/4,160594/4,
               485576/4,485576/4,485576/4,485576/4,
               609880/4,609880/4,609880/4,609880/4,
               512206/4,512206/4,512206/4,512206/4,
               405607/4,405607/4,405607/4,405607/4,
               378669/4,378669/4,378669/4,378669/4,
               405607/4,405607/4
               ]
    
    for i in range(0,50):
        SC2[i] = (SC2[i]/60)
        FC1[i] = (FC1[i]/60)
        AFM10[i] = (AFM10[i]/60)
        Equipment[i] = Equipment[i]/60
        Process[i] = (Process[i]/70)
    
 
    #转换成numpy的ndarray数据格式，n行1列,LinearRegression需要列格式数据，如下：
    X_train = np.array(X).reshape((len(X), 1))
    SC2_train = np.array(SC2).reshape((len(SC2), 1))
    FC1_train = np.array(FC1).reshape((len(FC1), 1))
    AFM10_train = np.array(AFM10).reshape((len(AFM10), 1))
    Equipment_train = np.array(Equipment).reshape((len(Equipment), 1))
    Process_train = np.array(Process).reshape((len(Process), 1))

    # 转换后数据格式如下
    # X_train = [[12.46], [0.25], [5.22], [11.3], [6.81], [4.59], [0.66], [14.53], [15.49], [14.43], [2.19], [1.35],
    #            [10.02], [12.93], [5.93], [2.92], [12.81], [4.88], [13.11], [5.8]]
    # Y_train = [[29.01], [4.7], [22.33], [24.99], [18.85], [14.89], [10.58], [36.84], [42.36], [39.73], [11.92], [7.45],
    #            [22.9], [36.62], [16.04], [16.56], [31.55], [20.04], [35.26], [23.59]]
 
 
    #新建一个线性回归模型，并把数据放进去对模型进行训练
    SC2LineModel = LinearRegression()
    SC2LineModel.fit(X_train, SC2_train)
 
    FC1LineModel = LinearRegression()
    FC1LineModel.fit(X_train, FC1_train)
    
    AFM10LineModel = LinearRegression()
    AFM10LineModel.fit(X_train, AFM10_train)    
    
    EquipmentLineModel = LinearRegression()
    EquipmentLineModel.fit(X_train, Equipment_train)    
    
    ProcessLineModel = LinearRegression()
    ProcessLineModel.fit(X_train, Process_train)
    
    
    X1 = [13,14,15,16,17]
    X_Predit = np.array(X1).reshape((len(X1),1))
    
    #用训练后的模型，进行预测
    SC2_Predict = SC2LineModel.predict(X_Predit)
    FC1_Predict = FC1LineModel.predict(X_Predit)
    AFM10_Predict = AFM10LineModel.predict(X_Predit)
    Equipment_Predit = EquipmentLineModel.predict(X_Predit)
    Process_Predict = ProcessLineModel.predict(X_Predit)
 
    #coef_是系数，intercept_是截距
    
    SC2_Predict_data = []
    FC1_Predict_data = []
    AFM10_Predict_data = []
    Equipment_Predict_data = []
    Process_Predict_data = []
    
    CRV_Production_data = [1880,1880,1880,1880,1880]
    MDX_Production_data = [1665,1665,1665,1665,1665]
    weather_data = [0,0,0,0,0]    
    
    Run_Rate_data = []
    
    for i in range(0,5):
        SC2_Predict_data.append(SC2LineModel.coef_[0][0] * i + SC2LineModel.intercept_[0])
        FC1_Predict_data.append(FC1LineModel.coef_[0][0] * i + FC1LineModel.intercept_[0])
        AFM10_Predict_data.append(AFM10LineModel.coef_[0][0] * i + AFM10LineModel.intercept_[0])
        Equipment_Predict_data.append(EquipmentLineModel.coef_[0][0] * i + EquipmentLineModel.intercept_[0])
        Process_Predict_data.append(ProcessLineModel.coef_[0][0] * i + ProcessLineModel.intercept_[0])
        
    print(SC2_Predict_data)
    
    # pls delete this part just to implementation perpose
    Equipment_Predict_data = [188.095623256543, 180.2316541321564, 195.32165461325, 180.35431598732156, 170.33216895332156465323]
    Process_Predict_data = [1334.63361325465, 1350.2316546213, 1300.23156498735331, 1250.3543132135365, 1330.315498331545463]
    SC2_Predict_data = [42.312598639455786, 50.16543216498451321, 40.121646513218651, 33.3216534313454, 35.3315431326546832]
    AFM10_Predict_data = [110.674557856135, 125.351325894561357, 106.321568655165351, 100.213548948312, 103.32188651315532]
    FC1_Predict_data = [137.6523932165456, 127.321564845233223, 136.32154985123, 132.321654523, 139.2356316548515683]

    for i in range(0,5):
        Run_Rate_data.append(
            0.8715+0.0005111*CRV_Production_data[i] + 0.000156*MDX_Production_data[i] - 0.00116*Equipment_Predict_data[i] -0.000213*SC2_Predict_data[i] + 0.000136*FC1_Predict_data[i] 
            -0.00072*Process_Predict_data[i] -0.000082*weather_data[i] -0.00111*AFM10_Predict_data[i] 
        )
        Run_Rate_data[i] = Run_Rate_data[i] *100
        print(Run_Rate_data[i])


    bar = (
            Bar()
            .add_xaxis(["week1", "week2", "week3", "week4", "week5"])
            .add_yaxis(
                "SC2",
                SC2_Predict_data,
                yaxis_index=0,
                is_selected=False
            )
            .add_yaxis(
                "FC1",
                FC1_Predict_data,
                yaxis_index=0,
                is_selected=False
            )            
            .add_yaxis(
                "AFM-10",
                AFM10_Predict_data,
                yaxis_index=0,
                is_selected=False
            )            
            .add_yaxis(
                "Equipment",
                Equipment_Predict_data,
                yaxis_index=0,
                is_selected=False
            )            
            .add_yaxis(
                "Process",
                Process_Predict_data,
                yaxis_index=0,
                is_selected=False
            )
            .extend_axis(
            yaxis=opts.AxisOpts(
                name="Run Rate",
                # min_=-10,
                # max_=20,
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#67e0e3")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value}%"),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                    ),
                )
            )
            .set_global_opts(
                yaxis_opts=opts.AxisOpts(
                name="Downtime(min)",
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value}min") 
            ),
            )
        )
    
    line = (
        Line(
            opts.InitOpts(is_fill_bg_color=True)
        )
        .add_xaxis(["week1", "week2", "week3", "week4", "week5"])
        .add_yaxis(
            "Run rate",
            Run_Rate_data,
            yaxis_index=1,
            linestyle_opts=opts.LineStyleOpts(color="#67e0e3"),
            itemstyle_opts=opts.ItemStyleOpts(color="#67e0e3"),
            label_opts=opts.LabelOpts(is_show=True)
        )
    )
    
    overlap = bar.overlap(line)
    
    grid = (
        Grid(init_opts=opts.InitOpts(width="1200px", height="800px"))
        .add(
            overlap, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True
        )
        .render("forecast.html")
    )
        
    
    # a1 = lineModel.coef_[0][0]
    # b = lineModel.intercept_[0]
    # print("y=%.4f*x+%.4f" % (a1,b))
    
    # print("januarly 2023: ", a1*13+b )
 
    #对回归模型进行评分，这里简单使用训练集进行评分，实际很多时候用其他的测试集进行评分
    # print("得分", SC2LineModel.score(X_train, SC2_train))
    # print("准确", accuracy_score(X_train, SC2_train))
 
    #简单画图显示
    # plt.scatter(X, SC2, c="blue")
    # plt.plot(X_Predit, SC2_Predict, c="blue")
    # plt.scatter(X, FC1, c="red")
    # plt.plot(X_Predit, FC1_Predict, c="red")    
    # plt.show()