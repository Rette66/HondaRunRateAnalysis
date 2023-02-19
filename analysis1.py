from pathlib import Path
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Calendar, Tab, Timeline, Pie, Line, Grid


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
        ]
    ],
    2: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28
        ],
        [
            819,758,20,0,0,0,841,872,874,735,832,0,0,842,910,726,906,838,797,0,799,860,877,830,850,0,0,713
        ]
    ],
    3: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31
        ],
        [
            872,900,719,598,0,0,860,860,751,857,775,0,0,926,915,885,934,960,0,0,925,860,873,855,876,0,0,0,0,0,779
        ]
    ],
    4: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30
        ],
        [
            773,0,0,450,820,820,820,450,0,0,700,700,600,365,0,0,0,660,660,660,630,570,0,0,660,660,630,450,0,0
        ]
    ],
    5: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31
        ],
        [
            0,660,660,660,660,0,0,0,660,575,743,0,0,0,660,660,660,660,0,0,0,660,660,660,660,0,0,0,0,660
        ]
    ],
    6: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30
        ],
        [
            645,645,0,0,0,645,645,645,645,0,0,0,645,645,645,645,0,0,0,645,645,645,645,0,0,0,660,660,665,660
        ]
    ],
    7: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31
        ],
        [
            0,0,0,0,0,0,0,0,0,0,0,625,798,711,711,0,0,480,480,480,0,0,0,0,480,480,480,0,0,0,0
        ]
    ],
    8: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31
        ],
        [
            790,860,873,753,712,0,0,867,781,788,746,608,0,0,900,873,780,904,393,0,0,872,903,750,762,837,0,0,865,851,639
        ]
    ],
    9: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30
        ],
        [
            673,844,0,0,0,831,898,856,882,0,0,773,737,768,884,785,0,0,900,837,900,796,911,0,0,920,644,901,795,0
        ]
    ],
    10: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30
        ],
        [
            0,0,780,710,811,818,590,0,0,770,776,747,747,700,0,0,530,466,594,530,600,0,0,540,540,600,487,713,0,0,600
        ]
    ],
    11: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31
        ],
        [
            600,600,600,600,0,0,672,672,672,0,0,0,0,585,735,660,660,660,0,0,720,720,720,0,0,0,0,720,674,766
        ]
    ],
    12: [
        [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31
        ],
        [
            660,660,0,0,660,660,651,669,660,0,0,750,750,650,850,750,0,0,750,750,750,750,0,0,0,0,0,0,0,0,0
        ]
    ],
}

def production_and_downtime_monthly(month: int) -> Bar:
    bar = (
        Bar()
        .add_xaxis(production[month][0])
        .add_yaxis(
            series_name="Production",
            y_axis=production[month][1],
            # is_selected=False,
            label_opts=opts.LabelOpts(is_show=False),
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
            # datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
            # datazoom_opts=opts.DataZoomOpts(),
        )
    )
    return bar

# def production_and_downtime_yearly() -> Bar:
#     bar = (
#         Bar()
#         .add_xaxis(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
#         .add_yaxis("AC1",AC1_data)
#         .add_yaxis("DC2", [51988, 66693, 177770, 41224, 353210, 306065, 572022, 315764, 194469, 65189, 56061, 392755])
#         .set_global_opts(
#             # set title
#             title_opts=opts.TitleOpts(title="Object Down Time"),
            
#             # set tool box
#             toolbox_opts = opts.ToolboxOpts(is_show = True),
            
#             visualmap_opts=opts.VisualMapOpts(
#                 orient= "vertical",
#                 pos_left= "right",
#                 pos_top="center",
#                 min_= 10,
#                 max_= 10000000,
#                 range_text=["High downtime", "Low downtime"],
#                 dimension = 0,
                
#             )
#         )
#     )


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
            color="#d14a61",
        )
        .add_yaxis(
            "DC2", [51988, 66693, 177770, 41224, 353210, 306065, 572022, 315764, 194469, 65189, 56061, 392755],
            yaxis_index=1,
            color="#5793f3",
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

            )
        )
    )
    line = (
        Line()
        .add_xaxis(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
        .add_yaxis("SumProduction", [11937, 15699, 16980, 12078, 10588, 11675, 5725, 18107, 16535, 13649, 12036, 11370],
                   yaxis_index=0,
                   color="#675bba",
                   label_opts=opts.LabelOpts(is_show=False),
                   )
    )
    bar.overlap(line)
    return Grid().add(
        bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=False
    )




tab = Tab()
tab.add(grid_multi_yaxis(), "Monthly Production and Downtime")
tab.add(timeline, "Daily Production and Downtime")
tab.add(get_downtime_description(),"pie example" )
tab.render("tab_example.html")
# tab.add(pie_rosetype(), "pie-example")




#bar.render()