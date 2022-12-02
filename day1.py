input =[]
with open("inputday1.txt", "r") as f:
    input=[a.split('\n') for a in f.read().split("\n\n")]
# print(input)
total_cal = [sum([int(i) for i in j if i.isdigit()]) for j in input]
# total_cal = []
# for i in input:
#     total_cal.append(sum(map(int, i)))
# print(total_cal)
max_index = total_cal.index(max(total_cal))
print("Most calories is {}".format(total_cal[max_index]))
print("Sum of top 3 elves calories are {}".format(sum(sorted(total_cal, reverse=True)[:3])))
