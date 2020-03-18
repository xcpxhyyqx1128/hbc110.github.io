#coding=gbk
import random
import json
import matplotlib.pyplot as plt

##�����ϱ�ϵͳ

## 7��1�ܣ�30��һ��
def sumList(data_list): ## ���б��Ԫ�صĺ�
    total = 0
    for i in data_list:
        total += i
    return total

def showWeekAll():
    dict_all = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0}
    for item in list_finished:
        for i in range(0, len(item[7]), 7):
            week=item[7][i:i+7]
            if len(week) == sumList(week): ## �ò�
                dict_all[i/7+1] += 1

    print(dict_all)
    name_list = list(dict_all.keys())
    num_list = list(dict_all.values())
    print(num_list)
    plt.rcParams['font.sans-serif']=['STSong']     ## ��������
    plt.xticks(rotation=270)
    plt.bar(range(len(num_list)), num_list, tick_label=name_list)
    plt.show()

def showWeekWork():
    dict_work = {'T':0,'S':0}
    for item in list_finished:
        for i in range(0, len(item[7]), 7):
            week=item[7][i:i+7]
            if len(week) == sumList(week): ## �ò�
                dict_work[item[3]] += 1

    print(dict_work)
    name_list = list(dict_work.keys())
    num_list = list(dict_work.values())
    print(num_list)
    plt.rcParams['font.sans-serif']=['STSong']     ## ��������
    plt.xticks(rotation=270)
    plt.bar(range(len(num_list)), num_list, tick_label=name_list)
    plt.show()

def showWeekSex():
    dict_sex = {'W':0,'M':0}
    for item in list_finished:
        for i in range(0, len(item[7]), 7):
            week=item[7][i:i+7]
            if len(week) == sumList(week): ## �ò�
                dict_sex[item[2]] += 1

    print(dict_sex)
    name_list = list(dict_sex.keys())
    num_list = list(dict_sex.values())
    print(num_list)
    plt.rcParams['font.sans-serif']=['STSong']     ## ��������
    plt.xticks(rotation=270)
    plt.bar(range(len(num_list)), num_list, tick_label=name_list)
    plt.show()
    
def showWeekProvince():
    dict_address = {'������':0,'�����':0,'������':0,'�Ϻ���':0,'�й����':0,'�й�����':0,'�й�̨��':0,'����������':0,'�ຣʡ':0,'���Ļ���������':0,
                     '�½�ά���������':0,'����ʡ':0,'ɽ��ʡ':0,'����ʡ':0,'����ʡ':0,'����ʡ':0,'����ʡ':0,'����ʡ':0,'����ʡ':0,'���ɹ�������':0,
                     '����ʡ':0,'����ʡ':0,'����ʡ':0,'�ӱ�ʡ':0,'����׳��������':0,'����ʡ':0,'ɽ��ʡ':0,'����ʡ':0,'������ʡ':0,'�㽭ʡ':0,'�Ĵ�ʡ':0,
                     '����ʡ':0,'�㶫ʡ':0,'����ʡ':0}
    for item in list_finished:
        for i in range(0, len(item[7]), 7):
            week=item[7][i:i+7]
            if len(week) == sumList(week): ## �ò�
                dict_address[item[4]] += 1

    print(dict_address)
    name_list = list(dict_address.keys())
    num_list = list(dict_address.values())
    print(num_list)
    plt.rcParams['font.sans-serif']=['STSong']     ## ��������
    plt.xticks(rotation=270)
    plt.bar(range(len(num_list)), num_list, tick_label=name_list)
    plt.show()

def showWeekCollege():  ## ����״ͼ index: 5, 7
     dict_college = {'��ѧԺ':0,'��ʷ�Ļ�ѧԺ':0,'����ѧԺ':0,'����ѧԺ':0,'���˼����ѧԺ':0,'��ᷢչ�빫������ѧԺ':0,'��ѧԺ':0,'����ѧԺ':0,'��ѧԺ':0,
                     '�����ѧԺ':0,'����ѧԺ':0,'�赸ѧԺ':0,'����ѧԺ':0,'����ѧԺ':0,'��ѧ��ͳ��ѧԺ':0,'�������ѧ�빤��ѧԺ':0,'��������ӹ���ѧԺ':0,
                     '��ѧ�뻯��ѧԺ':0,'������ѧѧԺ':0,'�����뻷����ѧѧԺ':0,'��������ѧԺ':0,'��ýѧԺ':0,'����ѧԺ':0,'�����Ļ�����ѧԺ':0,
                     '�ػ�ѧԺ':0,'��ѧѧԺ':0}
     for item in list_finished:
         for i in range(0, len(item[7]), 7):
             week=item[7][i:i+7]
             if len(week) == sumList(week): ## �ò�
                 dict_college[item[5]] += 1

     print(dict_college)
     name_list = list(dict_college.keys())
     num_list = list(dict_college.values())
     print(num_list)
     plt.rcParams['font.sans-serif']=['STSong']     ## ��������
     plt.xticks(rotation=270)
     plt.bar(range(len(num_list)), num_list, tick_label=name_list)
     plt.show()

def showMonthAll():
    dict_All = {1:0, 2:0, 3:0, 4:0}
    for item in list_finished:
         for i in range(0, len(item[7]), 30):
             month=item[7][i:i+30]
             if len(month) == sumList(month): ## �ò�
                 dict_All[i/30+1] += 1

    name_list = list(dict_All.keys())
    num_list = list(dict_All.values())
    print(num_list)
    plt.rcParams['font.sans-serif']=['STSong']     ## ��������
    plt.xticks(rotation=270)
    plt.bar(range(len(num_list)), num_list, tick_label=name_list)
    plt.show()
    
def showMonthWork():
    dict_Work = {'T':0,'S':0}
    for item in list_finished:
         for i in range(0, len(item[7]), 30):
             month=item[7][i:i+30]
             if len(month) == sumList(month): ## �ò�
                 dict_Work[item[3]] += 1

    name_list = list(dict_Work.keys())
    num_list = list(dict_Work.values())
    print(num_list)
    plt.rcParams['font.sans-serif']=['STSong']     ## ��������
    plt.xticks(rotation=270)
    plt.bar(range(len(num_list)), num_list, tick_label=name_list)
    plt.show()

def showMonthSex():
    dict_Sex = {'W':0,'M':0}
    for item in list_finished:
         for i in range(0, len(item[7]), 30):
             month=item[7][i:i+30]
             if len(month) == sumList(month): ## �ò�
                 dict_Sex[item[2]] += 1

    name_list = list(dict_Sex.keys())
    num_list = list(dict_Sex.values())
    print(num_list)
    plt.rcParams['font.sans-serif']=['STSong']     ## ��������
    plt.xticks(rotation=270)
    plt.bar(range(len(num_list)), num_list, tick_label=name_list)
    plt.show()

def showMonthProvince(): # ����״ͼ index: 4, 7
     dict_Address = {'������':0,'�����':0,'������':0,'�Ϻ���':0,'�й����':0,'�й�����':0,'�й�̨��':0,'����������':0,'�ຣʡ':0,'���Ļ���������':0,
                     '�½�ά���������':0,'����ʡ':0,'ɽ��ʡ':0,'����ʡ':0,'����ʡ':0,'����ʡ':0,'����ʡ':0,'����ʡ':0,'����ʡ':0,'���ɹ�������':0,
                     '����ʡ':0,'����ʡ':0,'����ʡ':0,'�ӱ�ʡ':0,'����׳��������':0,'����ʡ':0,'ɽ��ʡ':0,'����ʡ':0,'������ʡ':0,'�㽭ʡ':0,'�Ĵ�ʡ':0,
                     '����ʡ':0,'�㶫ʡ':0,'����ʡ':0}

     for item in list_finished:
         for i in range(0, len(item[7]), 30):
             month=item[7][i:i+30]
             if len(month) == sumList(month): ## �ò�
                 dict_Address[item[4]] += 1

     name_list = list(dict_Address.keys())
     num_list = list(dict_Address.values())
     print(num_list)
     plt.rcParams['font.sans-serif']=['STSong']     ## ��������
     plt.xticks(rotation=270)
     plt.bar(range(len(num_list)), num_list, tick_label=name_list)
     plt.show()

def showMonthCollege():
    dict_College = {'��ѧԺ':0,'��ʷ�Ļ�ѧԺ':0,'����ѧԺ':0,'����ѧԺ':0,'���˼����ѧԺ':0,'��ᷢչ�빫������ѧԺ':0,'��ѧԺ':0,'����ѧԺ':0,'��ѧԺ':0,
                     '�����ѧԺ':0,'����ѧԺ':0,'�赸ѧԺ':0,'����ѧԺ':0,'����ѧԺ':0,'��ѧ��ͳ��ѧԺ':0,'�������ѧ�빤��ѧԺ':0,'��������ӹ���ѧԺ':0,
                     '��ѧ�뻯��ѧԺ':0,'������ѧѧԺ':0,'�����뻷����ѧѧԺ':0,'��������ѧԺ':0,'��ýѧԺ':0,'����ѧԺ':0,'�����Ļ�����ѧԺ':0,
                     '�ػ�ѧԺ':0,'��ѧѧԺ':0}

    for item in list_finished:
        for i in range(0, len(item[7]), 30):
            month=item[7][i:i+30]
            if len(month) == sumList(month): ## �ò�
                dict_College[item[5]] += 1

    name_list = list(dict_College.keys())
    num_list = list(dict_College.values())
    print(num_list)
    plt.rcParams['font.sans-serif']=['STSong']     ## ��������
    plt.xticks(rotation=270)
    plt.bar(range(len(num_list)), num_list, tick_label=name_list)
    plt.show()

def showPerson():
    while True:
        print("="*22,"������","="*22)
        print("{0:8} {1:13} {2:15}".format(" ","1. ����Ų�ѯ","2. ��������ѯ"))
        print("{0:8} {1:14} {2:15}".format(" ","3. ������һ��"," "))
        print("="*52)
        key = input("�������Ӧ��ѡ��").strip()
        
        if key == "1":
            print("="*20,"����Ų�ѯ","="*20)
            id = int(input("������Ҫ��ѯ�ı�ţ�"))
            try:
                if id in range(1,2001):
                    print(list_finished[id-1])
            except:
                print("���޴���")
        elif key == "2":
            print("="*20,"��������ѯ","="*20)
            name = input("������Ҫ��ѯ��������")
            try:
                for i in range(len(list_finished)):
                    if list_finished[i][1] == name:
                        print(list_finished[i])   
            except:
                print("���޴���")
            
        elif key == "3":
            print("="*16, "�������ѯ����ټ�", "="*16)
            break
        else:
            print("="*17, "��Ч�ļ������룡", "="*17)


def showWeek():
    while True:
        print("="*23,"����","="*23)
        print("{0:8} {1:15} {2:15}".format(" ","1. ��ѯȫ��","2. ��ְ���ѯ"))
        print("{0:8} {1:14} {2:15}".format(" ","3. ���Ա��ѯ","4. ��ʡ�ݲ�ѯ"))
        print("{0:8} {1:14} {2:15}".format(" ","5. ��ѧԺ��ѯ","6. ������һ��"))
        print("="*52)
        key = input("�������Ӧ��ѡ��").strip()
        if key == "1":
            print("="*21,"��ѯȫ��","="*21)
            showWeekAll()
        elif key == "2":
            print("="*20,"��ְ���ѯ","="*20)
            showWeekWork()
        elif key == "3":
            print("="*20,"���Ա��ѯ","="*20)
            showWeekSex()
        elif key == "4":
            print("="*20,"��ʡ�ݲ�ѯ","="*20)
            showWeekProvince()
        elif key == "5":
            print("="*20,"��ѧԺ��ѯ","="*20)
            showWeekCollege()
        elif key == "6":
            print("="*17 ,"���ܲ�ѯ����ټ�", "="*17)
            break
        else:
            print("="*17 ,"��Ч�ļ������룡","="*17)
            

def showMonth():
    while True:
        print("="*23,"����","="*23)
        print("{0:8} {1:15} {2:15}".format(" ","1. ��ѯȫ��","2. ��ְ���ѯ"))
        print("{0:8} {1:14} {2:15}".format(" ","3. ���Ա��ѯ","4. ��ʡ�ݲ�ѯ"))
        print("{0:8} {1:14} {2:15}".format(" ","5. ��ѧԺ��ѯ","6. ������һ��"))
        print("="*52)
        key = input("�������Ӧ��ѡ��").strip()
        if key == "1":
            print("="*21,"��ѯȫ��","="*21)
            showMonthAll()
        elif key == "2":
            print("="*20,"��ְ���ѯ","="*20)
            showMonthWork()
        elif key == "3":
            print("="*20,"���Ա��ѯ","="*20)
            showMonthSex()
        elif key == "4":
            print("="*20,"��ʡ�ݲ�ѯ","="*20)
            showMonthProvince()
        elif key == "5":
            print("="*20,"��ѧԺ��ѯ","="*20)
            showMonthCollege()
        elif key == "6":
            print("="*17 ,"���²�ѯ����ټ�", "="*17)
            break
        else:
            print("="*17 ,"��Ч�ļ������룡","="*17)

list_id = []

list_Xing = ['��','Ǯ','��','��','��','��','֣','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','ʩ','��'
,'��','��','��','��','��','κ','��','��']
list_Ming = ['��','һ','��','��','��','��','��','��','��','��','ʮ']
list_personName= []

list_Sex = ['M','W']
list_personSex= []

list_Work = ['T','S']
list_personWork= []

list_Address = ['������','�����','������','�Ϻ���','�й����','�й�����','�й�̨��','����������','�ຣʡ','���Ļ���������','�½�ά���������','����ʡ','ɽ��ʡ','����ʡ','����ʡ','����ʡ','����ʡ','����ʡ','����ʡ','���ɹ�������','����ʡ','����ʡ','����ʡ','�ӱ�ʡ','����׳��������','����ʡ','ɽ��ʡ','����ʡ','������ʡ','�㽭ʡ','�Ĵ�ʡ','����ʡ','�㶫ʡ','����ʡ']
list_personAddress = []

list_XueYuan = ['��ѧԺ','��ʷ�Ļ�ѧԺ','����ѧԺ','����ѧԺ','���˼����ѧԺ','��ᷢչ�빫������ѧԺ','��ѧԺ','����ѧԺ','��ѧԺ','�����ѧԺ','����ѧԺ','�赸ѧԺ','����ѧԺ','����ѧԺ','��ѧ��ͳ��ѧԺ','�������ѧ�빤��ѧԺ','��������ӹ���ѧԺ','��ѧ�뻯��ѧԺ','������ѧѧԺ','�����뻷����ѧѧԺ','��������ѧԺ','��ýѧԺ','����ѧԺ','�����Ļ�����ѧԺ','�ػ�ѧԺ','��ѧѧԺ']
list_personXueYuan = []

list_TF = ['��','��']
list_personGoWH = []

#ȷ��
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
    #�����ʼ����
    print("="*12,"����ʦ����ѧ�����ѯϵͳ","="*14)
    print("{0:8} {1:13} {2:15}".format(" ","1. �������ѯ","2. ���ܲ�ѯ"))
    print("{0:8} {1:14} {2:15}".format(" ","3. ���²�ѯ","4. �˳�ϵͳ"))
    print("="*52)
    key = input("�������Ӧ��ѡ��")
    #���ݼ���ֵ�жϲ�ִ����Ӧ����
    if key == "1":
        print("="*20,"�������ѯ","="*20)
        showPerson()
    elif key == "2":
        print("="*21,"���ܲ�ѯ","="*21)
        showWeek()
    elif key == "3":
        print("="*21,"���²�ѯ","="*21)
        showMonth()
    elif key == "4":
        print("="*23 ,"�ټ�", "="*23)
        break
    else:
        print("="*17 ,"��Ч�ļ������룡","="*17)









