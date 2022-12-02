"A,X - rock"
"B,Y - paper"
"C,Z - scissor"

scores = {('A','X'):6, ('A','Y'):8, ('A','Z'):1, ('B','X'):1, ('B','Y'):6, ('B','Z'):8, ('C','X'):8, ('C','Y'):1, ('C','Z'):6 }
f = open("inputday2.txt","r")
lines = f.read().split('\n')
strategy = [line.split() for line in lines]
# print(strategy)

sum = 0
for i in strategy:
    if len(i) == 2:
        sum += scores[(i[0],i[1])]

print(sum)