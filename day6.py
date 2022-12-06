#Sahil Palnitkar


with open('inputday6.txt', 'r') as f:
    input = f.read()

answer_string=''
answer = -9999
for i in range(0,len(input)):
    check_string = input[i:i+4]
    duplicate_char=[]
    for character in check_string:
        if check_string.count(character) > 1:
            duplicate_char.append(character)  
    if not duplicate_char:
        answer = i+4
        answer_string=answer_string+check_string
        break

print(answer)
print(answer_string)

#######PART 2? LITERALLY THE SAME CODE
answer_string=''
answer = -9999
for i in range(0,len(input)):
    check_string = input[i:i+14]
    duplicate_char=[]
    for character in check_string:
        if check_string.count(character) > 1:
            duplicate_char.append(character)  
    if not duplicate_char:
        answer = i+14
        answer_string=answer_string+check_string
        break

print(answer)
print(answer_string)