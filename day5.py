#Sahil Palnitkar

#Hardcoding initial stack input
# [N]             [R]             [C]
# [T] [J]         [S] [J]         [N]
# [B] [Z]     [H] [M] [Z]         [D]
# [S] [P]     [G] [L] [H] [Z]     [T]
# [Q] [D]     [F] [D] [V] [L] [S] [M]
# [H] [F] [V] [J] [C] [W] [P] [W] [L]
# [G] [S] [H] [Z] [Z] [T] [F] [V] [H]
# [R] [H] [Z] [M] [T] [M] [T] [Q] [W]
#  1   2   3   4   5   6   7   8   9 


############PART 1
stack1 = ['R','G','H','Q','S','B','T','N']
stack2 = ['H','S','F','D','P','Z','J']
stack3 = ['Z','H','V']
stack4 = ['M','Z','J','F','G','H']
stack5 = ['T','Z','C','D','L','M','S','R']
stack6 = ['M','T','W','V','H','Z','J']
stack7 = ['T','F','P','L','Z']
stack8 = ['Q','V','W','S']
stack9 = ['W','H','L','M','T','D','N','C']

stack_list = {1:stack1,2:stack2,3:stack3,4:stack4,5:stack5,6:stack6,7:stack7,8:stack8,9:stack9}
with open('inputday5.txt', 'r') as f:
    lines = f.read().splitlines()
commands = []
import re
for line in lines:
    line1=[]
    splitline = line.split()
    splitline.remove('move')
    splitline.remove('from')
    splitline.remove('to')
    res = [eval(i) for i in splitline]
    commands.append(res)

# # print(commands)
# print(stack_list[1].pop())
count=0
for i in commands:
    # print(i)
    # print('\n')
    for j in range(0,i[0]):
        # print(j)
        # print('\n')

        x = stack_list[i[1]].pop()
        stack_list[i[2]].append(x)
        # print('\n')
        # for key, value in stack_list.items():
        #     print(key, value)
    # count+=1
    # print(count)
answer_string=""
for i in range(1,10):
    answer_string = answer_string + stack_list[i][-1]

print(answer_string)





######PART 2


stack1 = ['R','G','H','Q','S','B','T','N']
stack2 = ['H','S','F','D','P','Z','J']
stack3 = ['Z','H','V']
stack4 = ['M','Z','J','F','G','H']
stack5 = ['T','Z','C','D','L','M','S','R']
stack6 = ['M','T','W','V','H','Z','J']
stack7 = ['T','F','P','L','Z']
stack8 = ['Q','V','W','S']
stack9 = ['W','H','L','M','T','D','N','C']

stack_list = {1:stack1,2:stack2,3:stack3,4:stack4,5:stack5,6:stack6,7:stack7,8:stack8,9:stack9}
with open('inputday5.txt', 'r') as f:
    lines = f.read().splitlines()
commands = []
import re
for line in lines:
    line1=[]
    splitline = line.split()
    splitline.remove('move')
    splitline.remove('from')
    splitline.remove('to')
    res = [eval(i) for i in splitline]
    commands.append(res)

# # print(commands)
# print(stack_list[1].pop())
count=0
for i in commands:
    # print(i)
    # print('\n')
    # print(j)
    # print('\n')
    popped = stack_list[i[1]][-i[0]:]
    del stack_list[i[1]][-i[0]:]
    stack_list[i[2]] =  stack_list[i[2]] + popped
    # print('\n')
    # for key, value in stack_list.items():
    #     print(key, value)
    # count+=1
    # print(count)
answer_string=""
for i in range(1,10):
    answer_string = answer_string + stack_list[i][-1]

print(answer_string)