from pathlib import Path
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Calendar, Tab, Timeline


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

# def format_data(data: dict) -> dict:
#     for month in range(1, 12):
#         max_data, sum_data = 0, 0
#         temp = data[mmonth]
#         max_data = max(temp)
#         for i in range(len(temp)):
#             sum_data+

def get_month_overlap_chart(month: int) -> Bar:
    bar = (
        Bar()
        .add_xaxis(name_list)
        .add_yaxis(
            series_name="Downtime",
            y_axis=data[month],
            # is_selected=False,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Object Down Time"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=opts.DataZoomOpts(
                type_="slider",
                orient="vertical",
            ),
            
            
            # visualmap_opts=opts.VisualMapOpts(
            #     orient="vertical",
            #     pos_left="right",
            #     pos_top="center",
            #     min_=10,
            #     max_=10000000,
            #     range_text=["High downtime", "Low downtime"],
            #     dimension=0,
            # )
        )
    )
    return bar

timeline = Timeline()
for x in range(1, 13):
    timeline.add(get_month_overlap_chart(month=x), time_point=str(x))
timeline.render("test.html")



# bar = (
#     Bar()
#     .add_xaxis(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
#     .add_yaxis("AC1",AC1_data)
#     .add_yaxis("DC2", [51988, 66693, 177770, 41224, 353210, 306065, 572022, 315764, 194469, 65189, 56061, 392755])
#     .set_global_opts(
#         # set title
#         title_opts=opts.TitleOpts(title="Object Down Time"),
        
#         # set tool box
#         toolbox_opts = opts.ToolboxOpts(is_show = True),
        
#         visualmap_opts=opts.VisualMapOpts(
#             orient= "vertical",
#             pos_left= "right",
#             pos_top="center",
#             min_= 10,
#             max_= 10000000,
#             range_text=["High downtime", "Low downtime"],
#             dimension = 0,
            
#         )
#     )
# )


#bar.render()