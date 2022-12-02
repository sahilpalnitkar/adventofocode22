#Samantha Papageorge

with open('inputday2.txt', 'r') as f:
    lines = f.readlines()

def points(opponent, me):

    score = 0

    if me == 'X':
        score += 1
        if opponent == 'A':
            score += 3
        elif opponent == 'C':
            score += 6

    elif me == 'Y':
        score += 2
        if opponent == 'A':
            score += 6
        elif opponent == 'B':
            score += 3

    else:
        score += 3
        if opponent == 'B':
            score += 6
        elif opponent == 'C':
            score += 3

    return score
                
total = 0

for l in lines:
    game = l.strip().split()
    total += points(game[0],game[1])

print(total)

def points2(opponent, result):

    score = 0

    if result == 'X':
        if opponent == 'A':
            score += 3
        elif opponent == 'B':
            score += 1
        else:
            score += 2

    elif result == 'Y':
        score += 3
        if opponent == 'A':
            score += 1
        elif opponent == 'B':
            score += 2
        else:
            score += 3

    else:
        score += 6
        if opponent == 'A':
            score += 2
        elif opponent == 'B':
            score += 3
        else:
            score += 1

    return score
             
grandtotal = 0

for l in lines:
    game = l.strip().split()
    grandtotal += points2(game[0],game[1])

print(grandtotal)