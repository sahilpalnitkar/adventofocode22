import math

monke_item={0:[93, 54, 69, 66, 71],
            1:[89, 51, 80, 66],
            2:[90, 92, 63, 91, 96, 63, 64],
            3:[65, 77],
            4:[76, 68, 94],
            5:[86, 65, 66, 97, 73, 83],
            6:[78],
            7:[89, 57, 59, 61, 87, 55, 55, 88]}

monke_oper={0:['mul',3],
            1:['mul',17],
            2:['add',1],
            3:['add',2],
            4:['sqr',0],
            5:['add',8],
            6:['add',6],
            7:['add',7]}

monke_test={0:7,
            1:19,
            2:13,
            3:3,
            4:2,
            5:11,
            6:17,
            7:5}

monke_throw={0:[7,1],
            1:[5,7],
            2:[4,3],
            3:[4,6],
            4:[0,6],
            5:[2,3],
            6:[0,1],
            7:[2,5]}

monke_count={0:0,
             1:0,
             2:0,
             3:0,
             4:0,
             5:0,
             6:0,
             7:0,
             }
lcm = math.lcm(7, 19, 13, 3, 2, 11, 17, 5)
for i in range(0,10000):
    for j in range(0,len(monke_item)):
        for k in monke_item[j]:
            worry_level = k
            if monke_oper[j][0]=='mul':
                worry_level = worry_level * monke_oper[j][1]
            elif monke_oper[j][0]=='add':
                worry_level = worry_level + monke_oper[j][1]
            else:
                worry_level = worry_level * worry_level
            worry_level2=worry_level
            worry_level=worry_level%lcm
            if worry_level2%monke_test[j]==0:
                monke_item[monke_throw[j][0]].append(worry_level)
            else:
                monke_item[monke_throw[j][1]].append(worry_level)
            monke_count[j]+=1
        monke_item[j]=[]
    print(monke_count)
print(monke_count)
print("monkey_business = ", sorted(monke_count.values())[-1]*sorted(monke_count.values())[-2])