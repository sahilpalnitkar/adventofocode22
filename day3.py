#Sahil Palnitkar

import string
with open('inputday3.txt', 'r') as f:
    lines = f.read().splitlines()

alphabet = list(string.ascii_lowercase)
upper = [x.upper() for x in alphabet]
alphabet = alphabet + upper
numbers = list(range(1, 53))
alphtonum = {}
for i in range (0,52):
    alphtonum[alphabet[i]] = numbers[i]

# print(lines)


sum = 0
for i in lines:
    firstpart, secondpart = i[:len(i)//2], i[len(i)//2:]
    a=list(set(firstpart)&set(secondpart))
    for i in a:
        sum += alphtonum[i]

print(sum)
badge_sum =0

triple_list = list(zip(*[iter(lines)]*3))

for i in triple_list:
    b=list(set(i[0])&set(i[1])&set(i[2]))
    for i in b:
        badge_sum += alphtonum[i]
print(badge_sum)
