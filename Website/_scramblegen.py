import random
moves = ["U", "D", "F", "B", "R", "L"]
direction = ["", "'", "2"]

#generates the scramble, length of 20 - 25
def gen():
    scramble_len = random.randint(20, 25)
    scramble =[[]]
    for i in range(scramble_len):
        current = []
        current.append(moves[random.randint(0, len(moves)-1)])
        current.append(direction[random.randint(0, 2)])
        scramble.append(current)
    scramble.pop(0)
    #make sure that the scramble is valid
    valid(scramble)
    scramble.append(scramble_len)
    # strscramble = ''
    # for i in range(scramble_len):
    #     strscramble += str(scramble[i][0]) + str(scramble[i][1]) + ' '
    # strscramble += '['+str(scramble_len)+']'
    # return strscramble
    return scramble

#turns the scramble from 2D list into a single string
def stringscramble(scramble):
    scramble_len = len(scramble)
    strscramble = ''
    for i in range(scramble_len-1):
        strscramble += str(scramble[i][0]) + str(scramble[i][1]) + ' '
    strscramble += '['+str(scramble_len - 1)+']'
    return strscramble

def valid(s):
    #this checks to see if the moves behind each other are the same and gets rids of repeats like 'B B2' or 'B' F B'
    for x in range(1, len(s)):
        while s[x][0] == s[x-1][0]:
            s[x][0] = moves[random.randint(0, len(moves)-1)]
    for x in range(2, len(s)):
        while s[x][0]== s[x-2][0] or s[x][0] == s[x-1][0]:
            s[x][0] = moves[random.randint(0, len(moves)-1)]
    return s

current_scramble = gen()
#current_scramble = [['R', ''], ['D', ''], ['L', '2'], ['U', "'"], ['F', "'"], ['R', ''], ['L', '2'], ['F', ''], ['D', '2'], ['R', "'"], ['B', '2'], ['U', ''], ['F', "'"], ['B', '2'], ['R', "'"], ['D', ''], ['L', '2'], ['B', ''], ['D', ''], ['U', '2'], 20]