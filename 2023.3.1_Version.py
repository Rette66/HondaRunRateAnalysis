from pathlib import Path
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Calendar, Tab, Timeline, Pie, Line, Grid, Page, Liquid
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

name_list = [
    "AC1",
    "EC1",
    "AF ON",
    "DC2"
]

AC1_data = [
    249481, 234174, 265986, 1344377, 913736, 1175732, 1648196, 497250, 826269, 1557254, 1050647, 1451204
]

downtime_data = {
    
}

# for obj in name_list:


####**************************************************************bar chart for monthly production*********************************************************************************************************************

    
data= {
    1: [
        249481,
        82981,
        267418,
        51988
    ],

    2: [
        234174,
        69736,
        382536,
        66693
    ],

    3: [
        265986,
        49334,
        500084,
        177770
    ],

    4: [
       1344377,
        263522,
        1368401,
        41224 
    ],

    5: [
        913736,
        49667,
        913629,
        353210
    ],

    6: [
        1175732,
        47461,
        1426420,
        306065
    ],

    7: [
        1648196,
        94307,
        1485105,
        572022
    ],
    
    8: [
        497250,
        67292,
        764584,
        315764
    ],

    9: [
        826269,
        44055,
        898635,
        194469
    ],

    10: [
        1577254,
        40359,
        1025683,
        65189
    ],

    11: [
        1050647,
        40359,
        634031,
        56061
    ],

    12: [
        1451204,
        93488,
        1144921,
        392755
    ],

}

production= {
    1: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31
        ],
        [
            0,0,562,640,770,488,0,0,0,0,285,679,647,0,0,0,0,737,804,785,740,0,0,796,776,802,795,780,0,0,851
        ],
        [
            0,0,6,0,0,117,107,17,17,0,0,0,0,17,9,9,0,0,0,0,19,0,0,5,0,0,10,0,0,0,5,0,0,10
        ]
    ],
    2: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28
        ],
        [
            819,758,20,0,0,0,841,872,874,735,832,0,0,842,910,726,906,838,797,0,799,860,877,830,850,0,0,713
        ],
        [
            0,0,447,894,0,0,10,0,0,0,5,0,0,10,0,0,0,0,5,0,10,0,0,0,5,0,0,6
        ]
    ],
    3: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31
        ],
        [
            872,900,719,598,0,0,860,860,751,857,775,0,0,926,915,885,934,960,0,0,925,860,873,855,876,0,0,0,0,0,779
        ],
        [
            0,0,0,5,0,0,10,27,20,35,5,0,0,10,20,2,0,5,0,0,10,18,0,27,24,0,0,894,894,894,74
        ]
    ],
    4: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30
        ],
        [
            773,0,0,450,820,820,820,450,0,0,700,700,600,365,0,0,0,660,660,660,630,570,0,0,660,660,630,450,0,0
        ],
        [
            144,0,0,438,81,72,71,475,0,0,188,209,297,69,0,0,0,232,178,263,282,329,0,0,242,246,277,460,0,0
        ]
    ],
    5: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31
        ],
        [
            0,660,660,660,660,0,0,0,660,575,743,0,0,0,660,660,660,660,0,0,0,660,660,660,660,0,0,0,0,660
        ],
        [
            0,229,262,256,262,0,0,0,0,222,7,127,0,0,0,205,242,279,260,0,0,0,137,256,229,227,0,0,0,0,243
        ]
    ],
    6: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30
        ],
        [
            645,645,0,0,0,645,645,645,645,0,0,0,645,645,645,645,0,0,0,645,645,645,645,0,0,0,660,660,665,660
        ],
        [
            251,264,0,0,0,277,163,235,269,0,0,0,263,273,253,257,0,0,0,208,253,268,256,0,0,0,190,250,260,243
        ]
    ],
    7: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31
        ],
        [
            0,0,0,0,0,0,0,0,0,0,0,625,798,711,711,0,0,480,480,480,0,0,0,0,480,480,480,0,0,0,0
        ],
        [
            0,0,0,0,0,0,0,0,0,0,0,138,32,172,118,0,0,409,320,419,0,0,0,0,339,366,437,0,0,0,0
        ]
    ],
    8: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31
        ],
        [
            790,860,873,753,712,0,0,867,781,788,746,608,0,0,900,873,780,904,393,0,0,872,903,750,762,837,0,0,865,851,639
        ],
        [
            83,41,6,141,156,0,0,4,44,4,30,0,0,0,5,0,0,0,0,0,0,5,0,0,36,0,0,0,5,48,0
        ]
    ],
    9: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30
        ],
        [
            673,844,0,0,0,831,898,856,882,0,0,773,737,768,884,785,0,0,900,837,900,796,911,0,0,920,644,901,795,0
        ],
        [
            0,64,0,0,0,30,21,38,0,0,0,5,0,25,39,0,0,0,5,36,0,48,0,0,0,5,0,30,0,0
        ]
    ],
    10: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30
        ],
        [
            0,0,780,710,811,818,590,0,0,770,776,747,747,700,0,0,530,466,594,530,600,0,0,540,540,600,487,713,0,0,600
        ],
        [
            0,0,5,0,0,0,50,0,0,65,67,135,114,190,0,0,305,309,300,380,254,0,0,345,350,254,0,116,0,0,151
        ]
    ],
    11: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31
        ],
        [
            600,600,600,600,0,0,672,672,672,0,0,0,0,585,735,660,660,660,0,0,720,720,720,0,0,0,0,720,674,766
        ],
        [
            310,294,279,279,0,0,222,212,153,0,0,0,0,87,111,235,209,27,0,0,141,150,193,0,0,0,0,40,80,24
        ]
    ],
    12: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31
        ],
        [
            660,660,0,0,660,660,651,669,660,0,0,750,750,650,850,750,0,0,750,750,750,750,0,0,0,0,0,0,0,0,0
        ],
        [
            187,174,0,0,238,223,96,202,234,0,0,114,116,0,51,134,0,0,165,158,112,171,898,0,0,0,0,0,0,0,0
        ]
    ],
}

def production_and_downtime_monthly(month: int) -> Bar:
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add_xaxis(production[month][0])
        .add_yaxis(
            series_name="Production",
            y_axis=production[month][1],
            color=Faker.rand_color(),
            # is_selected=False,
            label_opts=opts.LabelOpts(is_show=False),
            stack = "stack1"
        )
        .add_yaxis(
            series_name="Downtime",
            y_axis=production[month][2],
            color=Faker.rand_color(),
            label_opts=opts.LabelOpts(is_show=False),
            stack = "stack1"
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Object Down Time"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=[
                opts.DataZoomOpts(
                    type_="slider",
                    orient="vertical",
                    range_start=0,
                    range_end=100
                    ), 
                opts.DataZoomOpts(
                    type_="inside",
                    range_start=0,
                    range_end=100,
                    )
                ]
        )
    )
    return bar



timeline = Timeline()
for x in range(1, 13):
    timeline.add(production_and_downtime_monthly(month=x), time_point=str(x))
    
    
####**************************************************************pie chart*********************************************************************************************************************

    
des_data = ["Starved - Line Controlled Stop", "S1 Multimount Bump Stop BL 140 D106_01", "Strvd - FC2 ENT",
            "Blocked - D8000_02 F1-2 Exit Bump Stop", "Strvd - Gap Filler PM-9 - D8000-04", "MASTER 2 Process NOT IN "
                                                                                            "AUTO W502_04"]
dt_data = [46339203, 11174633, 8465353, 7817854, 7756770, 6865164]
data_pair = [list(z) for z in zip(des_data, dt_data)]
data_pair.sort(key=lambda des_data: des_data[1])


def get_downtime_description() -> Pie:
    c = (        
        Pie(init_opts=opts.InitOpts(bg_color="#2c343c"))
        .add(
            series_name="description",
            data_pair=data_pair,
            # rosetype="radius",
            radius="55%",
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Downtime Description Pie Chart",
                pos_left="center",
                pos_top="20",
                title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
        .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
            label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
        )
    )
    return c


#******************************************yearly production and downtime*********************************

def grid_multi_yaxis() -> Grid:
    bar = (
        Bar()
        .add_xaxis(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
        .add_yaxis(
            "AC1", [249481, 234174, 265986, 1344377, 913736, 1175732, 1648196, 497250, 826269, 1557254, 1050647,
                    1451204],
            yaxis_index=0,
            is_selected=False
        )
        .add_yaxis(
            "DC2", [51988, 66693, 177770, 41224, 353210, 306065, 572022, 315764, 194469, 65189, 56061, 392755],
            yaxis_index=0,
            is_selected=False
        )
        .add_yaxis(
            "AF_ON", [267418, 382536, 500084, 1368401, 913629, 1426420, 1485105, 764584, 898635, 1025683, 634031,
                      1144921],
            yaxis_index=0,
            is_selected=False
        )
        .add_yaxis(
            "EC1", [82981, 69736, 49334, 263522, 49667, 47461, 94307, 67292, 44055, 40359, 40164,
                      93488],
            yaxis_index=0,
            is_selected=False
        )
        .add_yaxis(
            "FC1", [201009, 37109, 155357, 20210, 31522, 59378, 30557, 79550, 31228, 27610, 275928, 14759],
            yaxis_index=0,
            is_selected=False
        )
        .add_yaxis(
            "FS1", [2111845, 1645723, 1830322, 1987318, 2144441, 1944600, 2397658, 1763843, 1797399, 2025782, 
                    2007526, 1880663],
            yaxis_index=0,
            is_selected=False
        )
        .add_yaxis(
            "FC2", [2001686, 1501410, 1737311, 1918597, 2096801, 1902199, 2359521, 1676029, 1701428, 1934679,
                    1929687, 1818380],
            yaxis_index=0,
            is_selected=False
        )
        .add_yaxis(
            "ICP_1", [27450, 23534, 154009, 56496, 69032, 69950, 62796, 61489, 141357, 254172, 41274, 267514],
            yaxis_index=0,
            is_selected=False
        )
        .add_yaxis(
            "RS1", [113498, 21759, 79073, 44331, 264863, 13632, 427586, 30001, 25877, 38189, 112927, 132478],
            yaxis_index=0,
            is_selected=False
        )
        .add_yaxis(
            "SC1", [1648672, 1393590, 1645052, 1873877, 2055907, 1893333, 2315078, 1544802, 1599914, 1849573,
                    1840984, 1820760],
            yaxis_index=0,
            is_selected=False
        )
        .add_yaxis(
            "SC2", [1903989, 1444981, 1673941, 1881719, 2061525, 1847039, 2290815, 1598329, 1595863, 1868943,
                    1856394, 1767350],
            yaxis_index=0,
            is_selected=False
        )
        .add_yaxis(
            "TC1", [1972464, 1513711, 1716461, 1929338, 2068730, 1871375, 2281982, 1669603, 1678217, 1933394,
                    1924222, 1818459],
            yaxis_index=0,
            is_selected=False
        )
        .add_yaxis(
            "TC2", [1973504, 1505849, 1711107, 1924120, 2078330, 1854484, 2354385, 1585359, 753293, 949758, 
                    1056333, 1289564],
            yaxis_index=0,
            is_selected=False
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="Good Units Produced",
                min_=0,
                max_=20000,
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                ),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                    ),
            )
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="Attendance Rate",
                # min_=-10,
                # max_=20,
                position="right",
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
                name="Downtime",
                min_=0,
                max_=2000000,
                position="right",
                offset=80,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value}s") 
            ),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=[
                opts.DataZoomOpts(type_="slider", orient="vertical", yaxis_index=0 ,range_start=0, range_end=100),
                opts.DataZoomOpts(type_="inside",range_start=0, range_end=100),
            ]
        )
    )
    line = (
        Line(
            opts.InitOpts(is_fill_bg_color=True)
        )
        .add_xaxis(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
        .add_yaxis("SumProduction", [11937, 15699, 16980, 12078, 10588, 11675, 5725, 18107, 16535, 13649, 12036, 11370],
                    yaxis_index=1,
                    linestyle_opts=opts.LineStyleOpts(color="#d14a61"),
                    itemstyle_opts=opts.ItemStyleOpts(color="#d14a61"),
                    label_opts=opts.LabelOpts(is_show=True),
                    )
    )
    attendanceRate = (
        Line()
        .add_xaxis(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
        .add_yaxis("Attendance Rate(%)", [0, 0.49, 0.92, 11.36, 6.89, 4.49, 1.44, -5.02, -6.42, 2.65, 13.37, 14.47],
                    yaxis_index=2,
                    linestyle_opts=opts.LineStyleOpts(color="#67e0e3"),
                    itemstyle_opts=opts.ItemStyleOpts(color="#67e0e3"),
                    label_opts=opts.LabelOpts(is_show=True),
                    )
    )
    bar.overlap(attendanceRate)
    bar.overlap(line)
    return Grid(init_opts=opts.InitOpts(theme=ThemeType.DARK)).add(
        bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True
    )



def feb_attendance() -> Bar:
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add_xaxis(["2/14", "2/15", "2/16", "2/17", "2/18", "2/21", "2/22", "2/23", "2/24", "2/25", "2/28"])
        .add_yaxis(
            "A-Shift", [-8.06, -1.43, -2.33, -2.69, -5.02, -3.94, -1.25, -0.36, -3.23, -11.11, -0.18],
            yaxis_index=0,
        )
        .add_yaxis(
            "B-Shift", [1.98, 7.75, 7.03, 0.90, 3.42, 5.05, 7.93, 7.21, 5.05, 0.00, -1.26],
            yaxis_index=0,
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Feb Attendance Rate"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=[
                opts.DataZoomOpts(
                    type_="inside",
                    range_start=0,
                    range_end=100,
                    )
                ]
        )
    )
    return bar

def mar_attendance() -> Bar:
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add_xaxis(["3/1", "3/2", "3/3", "3/4", "3/7", "3/8", "3/9", "3/10", "3/11", "3/14", "3/15", "3/16",
                   "3/17", "3/18", "3/21", "3/22", "3/23", "3/24", "3/25", "3/31"])
        .add_yaxis(
            "A-Shift", [-1.61, -1.61, -1.61, -3.23, -1.08, -1.43, -0.36, 0.54, -6.27, 1.43, 3.58, 1.43, 0.36, 
                        -1.79, 3.23, 3.23, 4.66, 5.38, 1.97, 6.45],
            yaxis_index=0,
        )
        .add_yaxis(
            "B-Shift", [0.00, -1.44, -1.44, -3.24, 1.8, 2.16, 0.18, -0.72, -6.49, 2.52, 0.36, 1.98, -1.08,
                       -5.05, 0.00, 2.34, 3.96, 2.16, -3.06, 10.09],
            yaxis_index=0,
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Mar Attendance Rate"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=[
                opts.DataZoomOpts(
                    type_="inside",
                    range_start=0,
                    range_end=100,
                    )
                ]
        )
    )
    return bar

def april_attendance() -> Bar:
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add_xaxis(["4/1/2022", "4/4/2022", "4/5/2022", "4/6/2022", "4/7/2022", "4/8/2022", "4/11/2022", "4/12/2022",          "4/13/2022", "4/14/2022", "4/18/2022", "4/19/2022", "4/20/2022", "4/21/2022", "4/22/2022", "4/25/2022", "4/26/2022", "4/27/2022", "4/28/2022"])
        .add_yaxis(
            "A-Shift", [3.41, 4.30, 7.35, 6.09, 5.38, 5.02, 6.99, 6.81, 6.99, 6.63, 6.99, 4.66, 9.14, 6.09, 6.27, 1.97, 6.99, 6.45, 4.48],
            yaxis_index=0,
        )
        .add_yaxis(
            "B-Shift", [4.86, 6.67, 6.13, 6.49, 5.23, 1.44, 4.14, 5.77, 7.57, 2.70, 7.39, 7.21, 5.77, 5.23, -3.06, 2.34, 9.01, 13.15, 5.77],
            yaxis_index=0,
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="April Attendance Rate"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=[
                opts.DataZoomOpts(
                    type_="inside",
                    range_start=0,
                    range_end=100,
                    )
                ]
        )
    )
    return bar

def may_attendance() -> Bar:
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add_xaxis(["5/2", "5/3", "5/4", "5/5", "5/10", "5/11", "5/12", "5/16", "5/17", "5/18", "5/19", "5/23", "5/24", "5/25", "5/26", "5/31"])
        .add_yaxis(
        "A-Shift", [-1.43, 4.30, 5.73, 3.94, 6.45, 7.35, 1.25, 2.33, 4.48, 5.56, 2.51, 4.48, 3.58, 4.12, 3.41, 4.66],
        yaxis_index=0,
        )
        .add_yaxis(
        "B-Shift", [3.78, 3.96, 5.23, 0.18, 2.70, 1.80, -1.98, -0.72, 5.77, 4.14, 2.70, 2.16, 4.68, 4.68, 0.72, 7.75],
        yaxis_index=0,
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="May Attendance Rate"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=[
                opts.DataZoomOpts(
                    type_="inside",
                    range_start=0,
                    range_end=100,
                    )
                ]
        )
    )
    return bar

def june_attendance() -> Bar:
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add_xaxis(["6/1", "6/2", "6/6", "6/7", "6/8", "6/9", "6/13", "6/14", "6/15", "6/16", "6/20", "6/21", "6/22",             "6/23", "6/27", "6/28", "6/29", "6/30"])
        .add_yaxis(
        "A-Shift", [2.14, 2.68, 2.14, 3.57, 1.96, 0.36, 1.96, 0.71, 1.96, -0.18, 3.75, 3.21, 2.86, 1.07, 0.54, 1.07, 5.00, 5.36],
        yaxis_index=0,
        )
        .add_yaxis(
        "B-Shift", [4.49, -0.36, 1.62, -3.95, 1.62, 0.54, 2.33, 3.59, 1.62, -1.97, 4.49, 5.39, 4.67, -0.72, 3.95, 5.21, 2.87, 5.21],
        yaxis_index=0,
        )

        .set_global_opts(
            title_opts=opts.TitleOpts(title="June Attendance Rate"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=[
                opts.DataZoomOpts(
                    type_="inside",
                    range_start=0,
                    range_end=100,
                    )
                ]
        )
    )
    return bar

def july_attendance() -> Bar:
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add_xaxis(["7/12", "7/13", "7/14", "7/15", "7/18", "7/19", "7/20", "7/25", "7/26", "7/27", "7/28", "7/29"])
        .add_yaxis(
            "A-Shift", [3.39, 0.36, -3.21, -6.96, -1.25, 1.07, 0.54, 1.96, 1.61, 2.86, -3.57, -3.57],
            yaxis_index=0,
        )
        .add_yaxis(
            "B-Shift", [7.18, 1.80, -1.97, -5.03, 3.95, 5.21, 2.69, -0.54, 2.15, -1.44, 1.44, -0.18],
            yaxis_index=0,
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="July Attendance Rate"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=[
                opts.DataZoomOpts(
                    type_="inside",
                    range_start=0,
                    range_end=100,
                ),
            ],
        )
    )
    return bar

def august_attendance() -> Bar:
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add_xaxis(["8/1", "8/2", "8/3", "8/4", "8/5", "8/8", "8/9", "8/10", "8/11", "8/12", "8/15", "8/16", "8/17", "8/18", "8/22", "8/23", "8/24", "8/25", "8/26", "8/29", "8/30", "8/31"])
        .add_yaxis(
            "A-Shift", [-4.29, -4.82, -3.93, -6.43, -10.89, -6.61, -3.75, -5.36, -6.43, -8.93, -6.07, -5.54, -6.25, -6.79, -7.68, -5.54, -6.79, -6.79, -11.43, -7.5, -5.71, -6.96],
            yaxis_index=0,
        )
        .add_yaxis(
            "B-Shift", [0.72, 5.21, 5.39, 2.51, -0.90, 3.77, 4.67, 0.90, -1.44, -5.75, -0.18, 0.90, 2.15, 1.97, 0.36, 1.62, 1.08, 1.26, -8.80, 7.18, 6.10, 5.39],
            yaxis_index=0,
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="August Attendance Rate"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=[
                opts.DataZoomOpts(
                    type_="inside",
                    range_start=0,
                    range_end=100,
                ),
            ],
        )
    )
    return bar

from pyecharts.charts import Bar
from pyecharts import options as opts

def september_attendance() -> Bar:
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add_xaxis(["9/1", "9/2", "9/6", "9/7", "9/8", "9/9", "9/12", "9/13", "9/14", "9/15", "9/16", "9/19", "9/20", "9/21", "9/22", "9/23", "9/26", "9/27", "9/28", "9/29"])
        .add_yaxis(
            "A-Shift", [-8.39, -8.21, -6.96, -7.86, -11.43, -10.00, -10.71, -5.71, -7.86, -9.64, -12.86, -8.39, -5.89, -6.07, -6.07, -15.71, -4.46, -0.71, -1.07, -0.36],
            yaxis_index=0,
        )
        .add_yaxis(
            "B-Shift", [1.80, 0.18, 8.26, 5.03, 2.33, -4.67, 0.72, 4.49, 2.51, 3.41, -7.72, 0.72, 2.87, 4.31, 1.62, -4.85, -1.62, 1.44, -0.18, -0.72],
            yaxis_index=0,
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="September Attendance Rate"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=[
                opts.DataZoomOpts(
                    type_="inside",
                    range_start=0,
                    range_end=100,
                ),
            ],
        )
    )
    return bar

def september_attendance() -> Bar:
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add_xaxis(["9/1", "9/2", "9/6", "9/7", "9/8", "9/9", "9/12", "9/13", "9/14", "9/15", "9/16", "9/19", "9/20", "9/21", "9/22", "9/23", "9/26", "9/27", "9/28", "9/29"])
        .add_yaxis(
            "A-Shift", [-8.39, -8.21, -6.96, -7.86, -11.43, -10.00, -10.71, -5.71, -7.86, -9.64, -12.86, -8.39, -5.89, -6.07, -6.07, -15.71, -4.46, -0.71, -1.07, -0.36],
            yaxis_index=0,
        )
        .add_yaxis(
            "B-Shift", [1.80, 0.18, 8.26, 5.03, 2.33, -4.67, 0.72, 4.49, 2.51, 3.41, -7.72, 0.72, 2.87, 4.31, 1.62, -4.85, -1.62, 1.44, -0.18, -0.72],
            yaxis_index=0,
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="September Attendance Rate"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=[
                opts.DataZoomOpts(
                    type_="inside",
                    range_start=0,
                    range_end=100,
                ),
            ],
        )
    )
    return bar

def october_attendance() -> Bar:
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add_xaxis(["10/3", "10/4", "10/5", "10/6", "10/7", "10/10", "10/11", "10/12", "10/13", "10/14", "10/17", "10/18", "10/19", "10/20", "10/24", "10/25", "10/26", "10/27", "10/28", "10/31"])
        .add_yaxis(
            "A-Shift", [-3.21, 2.68, 3.04, 1.96, -2.14, 1.25, 0.71, 0.00, -0.71, -2.50, 0.89, 3.57, 5.36, 3.57, 3.93, 7.32, 8.75, 8.21, 2.86, 5.89],
            yaxis_index=0,
        )
        .add_yaxis(
            "B-Shift", [2.33, 4.85, 1.80, -0.36, -8.44, -0.90, 1.26, -0.72, -1.62, -7.90, 0.90, 1.80, 1.80, -0.90, 3.95, 3.59, 3.95, 0.00, -3.05, -0.72],
            yaxis_index=0,
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="October Attendance Rate"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=[
                opts.DataZoomOpts(
                    type_="inside",
                    range_start=0,
                    range_end=100,
                ),
            ],
        )
    )
    return bar

def october_attendance() -> Bar:
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add_xaxis(["10/3", "10/4", "10/5", "10/6", "10/7", "10/10", "10/11", "10/12", "10/13", "10/14", "10/17", "10/18", "10/19", "10/20", "10/24", "10/25", "10/26", "10/27", "10/28", "10/31"])
        .add_yaxis(
            "A-Shift", [-3.21, 2.68, 3.04, 1.96, -2.14, 1.25, 0.71, 0.00, -0.71, -2.50, 0.89, 3.57, 5.36, 3.57, 3.93, 7.32, 8.75, 8.21, 2.86, 5.89],
            yaxis_index=0,
        )
        .add_yaxis(
            "B-Shift", [2.33, 4.85, 1.80, -0.36, -8.44, -0.90, 1.26, -0.72, -1.62, -7.90, 0.90, 1.80, 1.80, -0.90, 3.95, 3.59, 3.95, 0.00, -3.05, -0.72],
            yaxis_index=0,
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="October Attendance Rate"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=[
                opts.DataZoomOpts(
                    type_="inside",
                    range_start=0,
                    range_end=100,
                ),
            ],
        )
    )
    return bar

def nov_attendance() -> Bar:
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add_xaxis(["11/1", "11/2", "11/3", "11/4", "11/7", "11/8", "11/9", "11/14", "11/15", "11/16", "11/17", "11/18", "11/21", "11/22", "11/23", "11/28", "11/29", "11/30"])
        .add_yaxis(
            "A-Shift", [4.27, 7.12, 6.76, 4.09, 9.61, 9.43, 11.39, 5.95, 6.84, 7.06, 6.95, 4.85, 5.40, 6.17, 7.61, 9.96, 6.41, 6.76],
            yaxis_index=0,
        )
        .add_yaxis(
            "B-Shift", [4.47, 4.29, 3.04, -1.61, 3.22, 9.30, 7.33, 7.67, 7.22, 6.09, 5.64, 2.37, 5.76, 5.42, 7.00, 13.60, 11.63, 11.63],
            yaxis_index=0,
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="November Attendance Rate"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=[
                opts.DataZoomOpts(
                    type_="inside",
                    range_start=0,
                    range_end=100,
                ),
            ],
        )
    )
    return bar

def dec_attendance() -> Bar:
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add_xaxis([
            "12/1", "12/2", "12/5", "12/6", "12/7", "12/8", "12/9", 
            "12/12", "12/13", "12/14", "12/15", "12/16"
        ])
        .add_yaxis(
            "A-Shift", [
                4.98, 2.67, 4.98, 7.12, 7.47, 6.94, 5.87, 
                6.41, 5.69, 7.65, 6.76, 4.63
            ],
            yaxis_index=0,
        )
        .add_yaxis(
            "B-Shift", [
                11.27, 5.01, 8.05, 9.30, 8.77, 7.69, 3.04, 
                11.27, 12.16, 10.38, 10.73, 4.83
            ],
            yaxis_index=0,
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="December Attendance Rate"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=[
                opts.DataZoomOpts(
                    type_="inside",
                    range_start=0,
                    range_end=100,
                ),
            ],
        )
    )
    return bar

def liquid_ShiftA() -> Liquid:
    liquid = (
        Liquid(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add("ShiftA", [0.625, 0.375], is_outline_show=False)
        .set_global_opts(title_opts=opts.TitleOpts(title="ShiftA Attendance Rate"))
    )
    return liquid

def liquid_ShiftB() -> Liquid:
    liquid = (
        Liquid(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add("ShiftB", [0.88, 0.12], is_outline_show=False)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="ShiftB Attendance Rate"),
        )
    )
    return liquid

def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        liquid_ShiftA(),
        liquid_ShiftB(),
        feb_attendance(),
        mar_attendance(),
        april_attendance(),
        may_attendance(),
        june_attendance(),
        july_attendance(),
        august_attendance(),
        september_attendance(),
        october_attendance(),
        nov_attendance(),
        dec_attendance(),
    )
    page.render("page_example.html")
    
tab = Tab()
tab.add(grid_multi_yaxis(), "Monthly Production and Downtime")
tab.add(timeline, "Daily Production and Downtime")
tab.add(get_downtime_description(),"pie example" )
tab.render("tab_example.html")

if __name__ == "__main__":
    page_draggable_layout()