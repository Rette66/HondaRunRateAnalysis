
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
    X =[1,2,3,4,5,6,7,8,9,10,11,12]
    SC2 = [1903989, 1444981, 1673941, 1881719, 2061525, 1847039, 2290815, 1598329, 1595863, 1868943,
                    1856394, 1767350]
    FC1 = [2111845, 1645723, 1830322, 1987318, 2144441, 1944600, 2397658, 1763843, 1797399, 2025782, 
                    2007526, 1880663]
    AFM10 = [267418, 382536, 500084, 1368401, 913629, 1426420, 1485105, 764584, 898635, 1025683, 634031,
                      1144921]
    Equipment = [56294, 49686, 32474, 19964, 41631, 42167, 20693, 68235, 32530, 58419, 42700, 37591]
    Process = [634530, 662859, 436685, 237501, 204362, 233676, 160594, 485576, 609880, 512206, 405607, 378669]
    
    for i in range(0,12):
        SC2[i] = (SC2[i]/60-10000)/10
        FC1[i] = (FC1[i]/60)/10
        AFM10[i] = (AFM10[i]/60)/40
        Equipment[i] = Equipment[i]/60
        Process[i] = (Process[i]/60)/20
    
 
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
    
    CRV_Production_data = [2000,2000,2000,2000,2000]
    MDX_Production_data = [3000,3000,3000,3000,3000]
    weather_data = [0,0,0,0,0]    
    
    Run_Rate_data = []
    
    for i in range(13,18):
        SC2_Predict_data.append(SC2LineModel.coef_[0][0] * i + SC2LineModel.intercept_[0])
        FC1_Predict_data.append(FC1LineModel.coef_[0][0] * i + FC1LineModel.intercept_[0])
        AFM10_Predict_data.append(AFM10LineModel.coef_[0][0] * i + AFM10LineModel.intercept_[0])
        Equipment_Predict_data.append(EquipmentLineModel.coef_[0][0] * i + EquipmentLineModel.intercept_[0])
        Process_Predict_data.append(ProcessLineModel.coef_[0][0] * i + ProcessLineModel.intercept_[0])

    for i in range(0,5):
        Run_Rate_data.append(
            0.8715+0.0005111*CRV_Production_data[i] + 0.000156*MDX_Production_data[i] - 0.00116*Equipment_Predict_data[i] -0.000213*SC2_Predict_data[i] + 0.000136*FC1_Predict_data[i] 
            -0.00072*Process_Predict_data[i] -0.000082*weather_data[i] -0.00111*AFM10_Predict_data[i] 
        )
        Run_Rate_data[i] = Run_Rate_data[i] *100
        print(Run_Rate_data[i])


    bar = (
            Bar()
            .add_xaxis(["Jan", "Feb", "Mar", "Apr", "May"])
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
        .add_xaxis(["Jan", "Feb", "Mar", "Apr", "May"])
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