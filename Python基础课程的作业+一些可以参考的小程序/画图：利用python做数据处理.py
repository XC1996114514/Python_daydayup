import  numpy as np
import  pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams['font.family']='simhei'
#高端版本可以封装成函数，可以套在任意excel中(成功），图是打开一个，然后生成下一个
#高端版本能根据xlsx里面的内容自动分类，不需要创造数组
#更高端的版本可以调用其他库进行线性拟合等等（待发现）
#测试是否能打开
def paper_numberanalyze(name):

    paper = pd.read_excel(name)
    print(paper)

    #测试输出打印一行
    print(paper["性别（统计一波"])

    #统计男女生数目并统计比例,制作成表格和柱状图（扩展一下，年级，家庭所在地）
    # ——》可以作为抽样调查是否合理的依据

    data = '统计.xlsx'

    data = pd.read_excel('统计.xlsx')

    sex = data['性别（统计一波'].value_counts() #sex为属性标签

    print(sex)
    #看看性别类统计结果是什么类型
    print('type_sex=',type('sex'))
    print(sex)

    sex_list=['boy','girl']
    num_list = []

    for nums in sex:
        num_list.append(nums)
    ##统计出男女人数
    print(num_list)

    #如何用 value_counts() 求各个值的相对频率——》扩展一下各个消费的比例
    sex_per = data['性别（统计一波'].value_counts(normalize=True)
    print(sex_per)

    #消费水平制作成柱状图——》往上延申，不同地区的学生消费水平的柱状图
    # ——》甚至还可以画个折线图
    #value count 进行升序排序
    spent_money=data['消费（柱状图）'].value_counts(ascending=True)
    print(spent_money)
    spent_money_fromlargetosmall=['1000','2000','3000','4000']
    spent_money_number= []

    for nums in spent_money:
        spent_money_number.append(nums)
    plt.bar(spent_money_fromlargetosmall,spent_money_number)
    plt.title('月花费')
    # 中文防止乱码
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.show()

    #柱状图躺倒
    plt.barh(spent_money_fromlargetosmall,spent_money_number)
    plt.title('月花费,躺倒')

    #是否冲动消费，做成饼图——》中间空心的饼图
    Whether_impulse_consumption = data['是否冲动消费（饼图'].value_counts()  # sex为属性标签

    print(Whether_impulse_consumption)

    Whether_impulse_consumption_yesorno=['是','否']
    Whether_impulse_consumption_yesorno_number= []

    for nums in  Whether_impulse_consumption:
        Whether_impulse_consumption_yesorno_number.append(nums)

    plt.figure(figsize = (10,5),dpi=100)
    #根据数目改颜色
    colors=['b','g']
    #autopct =  保留2位小数
    #shadow = true 是否有阴影
    plt.pie(Whether_impulse_consumption_yesorno_number,labels=Whether_impulse_consumption_yesorno\
            ,autopct="%1.2f%%",colors=colors,shadow=True,startangle=90)
    #显示图例
    plt.legend()
    #保持饼的圆形
    #添加标题
    plt.title('是否冲动消费')
    #中文防止乱码
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus']= False
    plt.show()



if __name__ == '__main__':
    a='统计.xlsx'
    paper_numberanalyze(a)