import random
moves = ["U", "D", "F", "B", "R", "L"]
direction = ["", "'", "2"]

#generates the scramble
def gen():
    scramble_len = random.randint(20, 25)
    scramble =[[]]
    for i in range(scramble_len):
        current = []
        current.append(random.choice(moves))
        current.append(random.choice(direction))
        scramble.append(current)
    scramble.pop(0)
    #make sure that the scramble is valid
    valid(scramble)
    scramble.append(scramble_len)
    return scramble

#turns the scramble into a single string for display purposes
def stringscramble(scramble):
    scramble_len = len(scramble)
    strscramble = ''
    for i in range(scramble_len-1):
        strscramble += str(scramble[i][0]) + str(scramble[i][1]) + ' '
    strscramble += '['+str(scramble_len - 1)+']'
    return strscramble

def valid(s):
    #this checks to see if the moves behind each other are the same and gets rids of repeats like 'B B2' or 'B L B2'
    for x in range(1, len(s)):
        while s[x][0] == s[x-1][0]:
            s[x][0] = moves[random.randint(0, len(moves)-1)]
    for x in range(2, len(s)):
        while s[x][0]== s[x-2][0] or s[x][0] == s[x-1][0]:
            s[x][0] = moves[random.randint(0, len(moves)-1)]
    return s

#generates the scramble that is used by colourscanning, cube and scramblemap
current_scramble = gen()
#current_scramble = [['R', ''], ['D', ''], ['L', '2'], ['U', "'"], ['F', "'"], ['R', ''], ['L', '2'], ['F', ''], ['D', '2'], ['R', "'"], ['B', '2'], ['U', ''], ['F', "'"], ['B', '2'], ['R', "'"], ['D', ''], ['L', '2'], ['B', ''], ['D', ''], ['U', '2'], 20]