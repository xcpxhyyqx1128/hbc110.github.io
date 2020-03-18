#coding=gbk
import random
import json
import matplotlib.pyplot as plt

##疫情上报系统

## 7天1周，30天一月
def sumList(data_list): ## 求列表各元素的和
    total = 0
    for i in data_list:
        total += i
    return total

def showWeekAll():
    dict_all = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0}
    for item in list_finished:
        for i in range(0, len(item[7]), 7):
            week=item[7][i:i+7]
            if len(week) == sumList(week): ## 得病
                dict_all[i/7+1] += 1

    print(dict_all)
    name_list = list(dict_all.keys())
    num_list = list(dict_all.values())
    print(num_list)
    plt.rcParams['font.sans-serif']=['STSong']     ## 中文宋体
    plt.xticks(rotation=270)
    plt.bar(range(len(num_list)), num_list, tick_label=name_list)
    plt.show()

def showWeekWork():
    dict_work = {'T':0,'S':0}
    for item in list_finished:
        for i in range(0, len(item[7]), 7):
            week=item[7][i:i+7]
            if len(week) == sumList(week): ## 得病
                dict_work[item[3]] += 1

    print(dict_work)
    name_list = list(dict_work.keys())
    num_list = list(dict_work.values())
    print(num_list)
    plt.rcParams['font.sans-serif']=['STSong']     ## 中文宋体
    plt.xticks(rotation=270)
    plt.bar(range(len(num_list)), num_list, tick_label=name_list)
    plt.show()

def showWeekSex():
    dict_sex = {'W':0,'M':0}
    for item in list_finished:
        for i in range(0, len(item[7]), 7):
            week=item[7][i:i+7]
            if len(week) == sumList(week): ## 得病
                dict_sex[item[2]] += 1

    print(dict_sex)
    name_list = list(dict_sex.keys())
    num_list = list(dict_sex.values())
    print(num_list)
    plt.rcParams['font.sans-serif']=['STSong']     ## 中文宋体
    plt.xticks(rotation=270)
    plt.bar(range(len(num_list)), num_list, tick_label=name_list)
    plt.show()
    
def showWeekProvince():
    dict_address = {'北京市':0,'天津市':0,'重庆市':0,'上海市':0,'中国香港':0,'中国澳门':0,'中国台湾':0,'西藏自治区':0,'青海省':0,'宁夏回族自治区':0,
                     '新疆维吾尔自治区':0,'吉林省':0,'山西省':0,'贵州省':0,'福建省':0,'江苏省':0,'江西省':0,'安徽省':0,'湖南省':0,'内蒙古自治区':0,
                     '海南省':0,'云南省':0,'河南省':0,'河北省':0,'广西壮族自治区':0,'辽宁省':0,'山东省':0,'陕西省':0,'黑龙江省':0,'浙江省':0,'四川省':0,
                     '甘肃省':0,'广东省':0,'湖北省':0}
    for item in list_finished:
        for i in range(0, len(item[7]), 7):
            week=item[7][i:i+7]
            if len(week) == sumList(week): ## 得病
                dict_address[item[4]] += 1

    print(dict_address)
    name_list = list(dict_address.keys())
    num_list = list(dict_address.values())
    print(num_list)
    plt.rcParams['font.sans-serif']=['STSong']     ## 中文宋体
    plt.xticks(rotation=270)
    plt.bar(range(len(num_list)), num_list, tick_label=name_list)
    plt.show()

def showWeekCollege():  ## 画柱状图 index: 5, 7
     dict_college = {'文学院':0,'历史文化学院':0,'教育学院':0,'心理学院':0,'马克思主义学院':0,'社会发展与公共管理学院':0,'法学院':0,'经济学院':0,'商学院':0,
                     '外国语学院':0,'音乐学院':0,'舞蹈学院':0,'美术学院':0,'体育学院':0,'数学与统计学院':0,'计算机科学与工程学院':0,'物理与电子工程学院':0,
                     '化学与化工学院':0,'生命科学学院':0,'地理与环境科学学院':0,'教育技术学院':0,'传媒学院':0,'旅游学院':0,'国际文化交流学院':0,
                     '敦煌学院':0,'哲学学院':0}
     for item in list_finished:
         for i in range(0, len(item[7]), 7):
             week=item[7][i:i+7]
             if len(week) == sumList(week): ## 得病
                 dict_college[item[5]] += 1

     print(dict_college)
     name_list = list(dict_college.keys())
     num_list = list(dict_college.values())
     print(num_list)
     plt.rcParams['font.sans-serif']=['STSong']     ## 中文宋体
     plt.xticks(rotation=270)
     plt.bar(range(len(num_list)), num_list, tick_label=name_list)
     plt.show()

def showMonthAll():
    dict_All = {1:0, 2:0, 3:0, 4:0}
    for item in list_finished:
         for i in range(0, len(item[7]), 30):
             month=item[7][i:i+30]
             if len(month) == sumList(month): ## 得病
                 dict_All[i/30+1] += 1

    name_list = list(dict_All.keys())
    num_list = list(dict_All.values())
    print(num_list)
    plt.rcParams['font.sans-serif']=['STSong']     ## 中文宋体
    plt.xticks(rotation=270)
    plt.bar(range(len(num_list)), num_list, tick_label=name_list)
    plt.show()
    
def showMonthWork():
    dict_Work = {'T':0,'S':0}
    for item in list_finished:
         for i in range(0, len(item[7]), 30):
             month=item[7][i:i+30]
             if len(month) == sumList(month): ## 得病
                 dict_Work[item[3]] += 1

    name_list = list(dict_Work.keys())
    num_list = list(dict_Work.values())
    print(num_list)
    plt.rcParams['font.sans-serif']=['STSong']     ## 中文宋体
    plt.xticks(rotation=270)
    plt.bar(range(len(num_list)), num_list, tick_label=name_list)
    plt.show()

def showMonthSex():
    dict_Sex = {'W':0,'M':0}
    for item in list_finished:
         for i in range(0, len(item[7]), 30):
             month=item[7][i:i+30]
             if len(month) == sumList(month): ## 得病
                 dict_Sex[item[2]] += 1

    name_list = list(dict_Sex.keys())
    num_list = list(dict_Sex.values())
    print(num_list)
    plt.rcParams['font.sans-serif']=['STSong']     ## 中文宋体
    plt.xticks(rotation=270)
    plt.bar(range(len(num_list)), num_list, tick_label=name_list)
    plt.show()

def showMonthProvince(): # 画柱状图 index: 4, 7
     dict_Address = {'北京市':0,'天津市':0,'重庆市':0,'上海市':0,'中国香港':0,'中国澳门':0,'中国台湾':0,'西藏自治区':0,'青海省':0,'宁夏回族自治区':0,
                     '新疆维吾尔自治区':0,'吉林省':0,'山西省':0,'贵州省':0,'福建省':0,'江苏省':0,'江西省':0,'安徽省':0,'湖南省':0,'内蒙古自治区':0,
                     '海南省':0,'云南省':0,'河南省':0,'河北省':0,'广西壮族自治区':0,'辽宁省':0,'山东省':0,'陕西省':0,'黑龙江省':0,'浙江省':0,'四川省':0,
                     '甘肃省':0,'广东省':0,'湖北省':0}

     for item in list_finished:
         for i in range(0, len(item[7]), 30):
             month=item[7][i:i+30]
             if len(month) == sumList(month): ## 得病
                 dict_Address[item[4]] += 1

     name_list = list(dict_Address.keys())
     num_list = list(dict_Address.values())
     print(num_list)
     plt.rcParams['font.sans-serif']=['STSong']     ## 中文宋体
     plt.xticks(rotation=270)
     plt.bar(range(len(num_list)), num_list, tick_label=name_list)
     plt.show()

def showMonthCollege():
    dict_College = {'文学院':0,'历史文化学院':0,'教育学院':0,'心理学院':0,'马克思主义学院':0,'社会发展与公共管理学院':0,'法学院':0,'经济学院':0,'商学院':0,
                     '外国语学院':0,'音乐学院':0,'舞蹈学院':0,'美术学院':0,'体育学院':0,'数学与统计学院':0,'计算机科学与工程学院':0,'物理与电子工程学院':0,
                     '化学与化工学院':0,'生命科学学院':0,'地理与环境科学学院':0,'教育技术学院':0,'传媒学院':0,'旅游学院':0,'国际文化交流学院':0,
                     '敦煌学院':0,'哲学学院':0}

    for item in list_finished:
        for i in range(0, len(item[7]), 30):
            month=item[7][i:i+30]
            if len(month) == sumList(month): ## 得病
                dict_College[item[5]] += 1

    name_list = list(dict_College.keys())
    num_list = list(dict_College.values())
    print(num_list)
    plt.rcParams['font.sans-serif']=['STSong']     ## 中文宋体
    plt.xticks(rotation=270)
    plt.bar(range(len(num_list)), num_list, tick_label=name_list)
    plt.show()

def showPerson():
    while True:
        print("="*22,"按人物","="*22)
        print("{0:8} {1:13} {2:15}".format(" ","1. 按编号查询","2. 按姓名查询"))
        print("{0:8} {1:14} {2:15}".format(" ","3. 返回上一级"," "))
        print("="*52)
        key = input("请输入对应的选择：").strip()
        
        if key == "1":
            print("="*20,"按编号查询","="*20)
            id = int(input("请输入要查询的编号："))
            try:
                if id in range(1,2001):
                    print(list_finished[id-1])
            except:
                print("查无此人")
        elif key == "2":
            print("="*20,"按姓名查询","="*20)
            name = input("请输入要查询的姓名：")
            try:
                for i in range(len(list_finished)):
                    if list_finished[i][1] == name:
                        print(list_finished[i])   
            except:
                print("查无此人")
            
        elif key == "3":
            print("="*16, "按人物查询完毕再见", "="*16)
            break
        else:
            print("="*17, "无效的键盘输入！", "="*17)


def showWeek():
    while True:
        print("="*23,"按周","="*23)
        print("{0:8} {1:15} {2:15}".format(" ","1. 查询全部","2. 按职务查询"))
        print("{0:8} {1:14} {2:15}".format(" ","3. 按性别查询","4. 按省份查询"))
        print("{0:8} {1:14} {2:15}".format(" ","5. 按学院查询","6. 返回上一级"))
        print("="*52)
        key = input("请输入对应的选择：").strip()
        if key == "1":
            print("="*21,"查询全部","="*21)
            showWeekAll()
        elif key == "2":
            print("="*20,"按职务查询","="*20)
            showWeekWork()
        elif key == "3":
            print("="*20,"按性别查询","="*20)
            showWeekSex()
        elif key == "4":
            print("="*20,"按省份查询","="*20)
            showWeekProvince()
        elif key == "5":
            print("="*20,"按学院查询","="*20)
            showWeekCollege()
        elif key == "6":
            print("="*17 ,"按周查询完毕再见", "="*17)
            break
        else:
            print("="*17 ,"无效的键盘输入！","="*17)
            

def showMonth():
    while True:
        print("="*23,"按月","="*23)
        print("{0:8} {1:15} {2:15}".format(" ","1. 查询全部","2. 按职务查询"))
        print("{0:8} {1:14} {2:15}".format(" ","3. 按性别查询","4. 按省份查询"))
        print("{0:8} {1:14} {2:15}".format(" ","5. 按学院查询","6. 返回上一级"))
        print("="*52)
        key = input("请输入对应的选择：").strip()
        if key == "1":
            print("="*21,"查询全部","="*21)
            showMonthAll()
        elif key == "2":
            print("="*20,"按职务查询","="*20)
            showMonthWork()
        elif key == "3":
            print("="*20,"按性别查询","="*20)
            showMonthSex()
        elif key == "4":
            print("="*20,"按省份查询","="*20)
            showMonthProvince()
        elif key == "5":
            print("="*20,"按学院查询","="*20)
            showMonthCollege()
        elif key == "6":
            print("="*17 ,"按月查询完毕再见", "="*17)
            break
        else:
            print("="*17 ,"无效的键盘输入！","="*17)

list_id = []

list_Xing = ['赵','钱','孙','李','周','吴','郑','王','冯','陈','褚','卫','蒋','沈','韩','杨','朱','秦','尤','许','何','吕','施','张'
,'孔','曹','严','华','金','魏','陶','姜']
list_Ming = ['零','一','二','三','四','五','六','七','八','九','十']
list_personName= []

list_Sex = ['M','W']
list_personSex= []

list_Work = ['T','S']
list_personWork= []

list_Address = ['北京市','天津市','重庆市','上海市','中国香港','中国澳门','中国台湾','西藏自治区','青海省','宁夏回族自治区','新疆维吾尔自治区','吉林省','山西省','贵州省','福建省','江苏省','江西省','安徽省','湖南省','内蒙古自治区','海南省','云南省','河南省','河北省','广西壮族自治区','辽宁省','山东省','陕西省','黑龙江省','浙江省','四川省','甘肃省','广东省','湖北省']
list_personAddress = []

list_XueYuan = ['文学院','历史文化学院','教育学院','心理学院','马克思主义学院','社会发展与公共管理学院','法学院','经济学院','商学院','外国语学院','音乐学院','舞蹈学院','美术学院','体育学院','数学与统计学院','计算机科学与工程学院','物理与电子工程学院','化学与化工学院','生命科学学院','地理与环境科学学院','教育技术学院','传媒学院','旅游学院','国际文化交流学院','敦煌学院','哲学学院']
list_personXueYuan = []

list_TF = ['是','否']
list_personGoWH = []

#确诊
list_numbers = [0,1]
list_personQZ = []

list_finished = []

for i in range(1,2001):
    list_id =list_id  + [i]

##for personid in list_id:
##    print (personid)

for i in range(2000):
    name = random.choice(list_Xing)+random.choice(list_Ming)+random.choice(list_Ming)
    list_personName.append(name)
#for personname in list_personName:
##    print (personname)

for i in range(2000):
    sex = random.choice(list_Sex)
    list_personSex.append(sex)

for i in range(2000):
    work = random.choice(list_Work)
    list_personWork.append(work)

for i in range(2000):
    address = random.choice(list_Address)
    list_personAddress.append(address)

for i in range(2000):
    xueyuan = random.choice(list_XueYuan)
    list_personXueYuan.append(xueyuan)

for i in range(2000):
    gowh = random.choice(list_TF)
    list_personGoWH.append(gowh)

for i in range(2000):
    list_personQZ.append([])
    for j in range(100):
        num = random.choice(list_numbers)
        list_personQZ[i].append(num)

##for personSex in list_personSex:
##    print (personSex)

for i in range(len(list_personName)):
    tuple_temp = (list_id[i],list_personName[i],list_personSex[i],list_personWork[i],list_personAddress[i],list_personXueYuan[i],list_personGoWH[i],list_personQZ[i])
    list_finished.append(tuple_temp)

##print(list_finished[0][7][0])


filename = "numbers.json"
with open(filename, 'w') as file_obj:
    json.dump(list_finished, file_obj)

##print(len(list_finished))
##print(list_finished[0])
##
##print(list_finished[7][0])
##print(list_finished[7][1])
##print(list_finished[7][7][0])
##print(list_finished[7][7][99])

while True:
    #输出初始界面
    print("="*12,"西北师范大学疫情查询系统","="*14)
    print("{0:8} {1:13} {2:15}".format(" ","1. 按人物查询","2. 按周查询"))
    print("{0:8} {1:14} {2:15}".format(" ","3. 按月查询","4. 退出系统"))
    print("="*52)
    key = input("请输入对应的选择：")
    #根据键盘值判断并执行相应操作
    if key == "1":
        print("="*20,"按人物查询","="*20)
        showPerson()
    elif key == "2":
        print("="*21,"按周查询","="*21)
        showWeek()
    elif key == "3":
        print("="*21,"按月查询","="*21)
        showMonth()
    elif key == "4":
        print("="*23 ,"再见", "="*23)
        break
    else:
        print("="*17 ,"无效的键盘输入！","="*17)









