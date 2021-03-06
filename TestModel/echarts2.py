# *_*coding:utf-8 *_*
# __author__ = 'GonzaloWang'
from pyecharts.charts import Pie
from pyecharts import options as opts
from django.db import connection


def mkhtml2(name1):
    """
    饼图
    :return:生成豆瓣top250电影产源国家数量占比分析图html文件
    """

    # with open("config.yaml", 'r', encoding='utf-8')as f:
    #     x = yaml.safe_load(f)
    #
    # con = mysql.connector.connect(
    #     host=str(x['DB']['host']), port=str(x['DB']['port']),
    #     user=str(x['DB']['user']), password=str(x['DB']['password']),
    #     database=str(x['DB']['data']),
    # )
    # sql查询语句
    sql = "SELECT 地区 AS '地区', COUNT(*) AS '统计量' FROM t_movies GROUP BY `地区` ORDER BY 统计量 DESC LIMIT 0, 10"
    # mycursor = con.cursor()
    cursor = connection.cursor()
    cursor.execute(sql)
    myresult = cursor.fetchall()
    # fetchall() 获取所有记录
    namelist = []
    # 将变量存在列表里
    numlist = []
    for name in myresult:
        namelist.append(name[0])
        numlist.append(name[1])
    # print(len(namelist))
    # print(numlist)
    pie = Pie()
    pie.add("占比",
            [list(z) for z in zip(namelist, numlist)],
            center=["40%", "60%"],
            )
    pie.set_global_opts(
        title_opts=opts.TitleOpts(title="豆瓣top250电影产源国家数量占比"),
        legend_opts=opts.LegendOpts(pos_left="35%"),
    )
    # 设置显示的样子，加入了百分比
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c} ({d}%)"))
    pie.render(f'{name1}')
    print(f'{name1}已生成')


if __name__ == '__main__':
    mkhtml2("自定义名字")
