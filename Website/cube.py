from ._scramblegen import *
#s = gen()
#s = [['U','2'], ['B','2'], ['F',"2"], ["L",''],["U","2"], ['L','2'], ['F','2'], ['R',"'"],['U','2'],['R',"'"],["D", ""],['R',"'"],["U","2"], ['L',''], ['B',"'"], ["D","'"], ['F',''], ['D','2'], ['U',"'"], ['B','2']]
#'w', 'w', 'w','w', 'w', 'w','w', 'w', 'w'
#'y', 'y', 'y','y', 'y', 'y','y', 'y', 'y'
#'1', '2', '3','4', '5', '6','7', '8', '9'

#Creation of cube class
class Cube:
    def __init__(self):
        # self.cube = [['w', 'w', 'w','w', 'w', 'w','w', 'w', 'w'],
        #              ['o', 'o', 'o','o', 'o', 'o','o', 'o', 'o'],
        #              ['g', 'g', 'g','g', 'g', 'g','g', 'g', 'g'],
        #              ['r', 'r', 'r','r', 'r', 'r','r', 'r', 'r'],
        #              ['b', 'b', 'b','b', 'b', 'b','b', 'b', 'b'],
        #              ['y', 'y', 'y','y', 'y', 'y','y', 'y', 'y']]
        #the cube is a 2D list, each sublist is the faces' colour and elements in the sublist are the individual piece
        self.cube = [['g', 'g', 'g','g', 'g', 'g','g', 'g', 'g'],
                     ['o', 'o', 'o','o', 'o', 'o','o', 'o', 'o'],
                     ['b', 'b', 'b','b', 'b', 'b','b', 'b', 'b'],
                     ['r', 'r', 'r','r', 'r', 'r','r', 'r', 'r'],
                     ['w', 'w', 'w','w', 'w', 'w','w', 'w', 'w'], 
                     ['y', 'y', 'y','y', 'y', 'y','y', 'y', 'y']]
        
    def clockwise_move(self,y): #will be used for all normal moves
        #y = sublist (coloured face of the cube)
        temp = []
        #To turn 1D array of colour into 2D array so that I can rotate the matrix
        for i in range(0, 8, 3):
            singlelist = self.cube[y]
            list = singlelist[i:i+3]
            temp.append(list)
        tempcube = []
        #it appends three pieces at a time as one sublist, it does this from a range of 0-8 (since there are 9 pieces) and it goes up in increments of 3 in order to append the 3 pieces in each list to make a 2D list made up of 3 sublists each with 3 pieces. 
        # ex: turns ['g', 'g', 'g','g', 'g', 'g','g', 'g', 'g'] into [['g', 'g', 'g'], ['g', 'g', 'g'],['g', 'g', 'g']]
        for i in range(0,8,3):
            cubelist = self.cube[y]
            listc = cubelist[i:i+3]
            tempcube.append(listc)
        #Rotating the matrix (rows are turned into columns), 1st value of ori = last value of new sublist, 2nd value of ori = last value of next sublist etc..
        for i in range(3):
            for x in range(3):
                temp[x][2-i] = tempcube[i][x]
                #pass
        #Flattening it back into a 1D array
        final = []
        for i in range(3):
            for x in range(3):
                final.append(temp[i][x])
        self.cube[y] = final
        return self.cube
    
    def anticlockwise_move(self,y): #Will be used for all prime moves
        temp = []
        #To turn 1D array into 2D array so that I can rotate the matrix
        for i in range(0, 8, 3):
            singlelist = self.cube[y]
            list = singlelist[i:i+3]
            temp.append(list)
        tempcube = []
        for i in range(0,8,3):
            cubelist = self.cube[y]
            listc = cubelist[i:i+3]
            tempcube.append(listc)
        #Rotating the matrix (rows are turned into columns), this time, last from ori = 1st to new sublist, 2nd last from ori = 1st to next sublist etc..
        for i in range(3):
            for x in range(3):
                temp[x][i] = tempcube[i][2-x]
                pass
        #Flattening it back into a 1D array
        final = []
        for i in range(3):
            for x in range(3):
                final.append(temp[i][x])
        self.cube[y] = final
        return self.cube
    
    #swapping the pieces based on the move done, this swaps one piece in the layer at a time.
    # cx = colour, px = piece
    def swap(self,c1, c2, c3, c4, p1, p2, p3, p4):
        self.cube[c1][p1], self.cube[c2][p2], self.cube[c3][p3], self.cube[c4][p4] = self.cube[c2][p2], self.cube[c3][p3], self.cube[c4][p4], self.cube[c1][p1]
        return self.cube
    
    def getcube(self):
        return self.cube
    

#this scrambles the cube, s = 2D list of generated scramble
def scramble(s):
    #creation of cube object
    c = Cube()
    # -1 because last value in scramble is the length of the scramble
    for i in range(len(s)-1):
        #checking what the type of move is
        if s[i][0] == 'U':
        #checking to see if it a plain move or another variation of a move (', 2)
            if s[i][1] == '':
                # colour to be rotated = white , hence 4 is passed in
                c.clockwise_move(4)
                #first 4 values are the colours affected (ex: 0 = green), last 4 valuse are the pieces affected (ex: 1 = second piece on that face)
                c.swap(0,3,2,1,0,0,0,0)
                c.swap(0,3,2,1,1,1,1,1)
                c.swap(0,3,2,1,2,2,2,2)
            if s[i][1] == "'":
                c.anticlockwise_move(4)
                c.swap(0,1,2,3,0,0,0,0)
                c.swap(0,1,2,3,1,1,1,1)
                c.swap(0,1,2,3,2,2,2,2)
            if s[i][1] == "2":
                #for double moves, everything is done twice (hence clockwise and anticlockwise would give same result)
                c.clockwise_move(4)
                c.clockwise_move(4)
                c.swap(0,3,2,1,0,0,0,0)
                c.swap(0,3,2,1,1,1,1,1)
                c.swap(0,3,2,1,2,2,2,2)
                c.swap(0,3,2,1,0,0,0,0)
                c.swap(0,3,2,1,1,1,1,1)
                c.swap(0,3,2,1,2,2,2,2)
        elif s[i][0] == 'D':
            if s[i][1] == '':
                #colour to be rotated = yellow , hence 5 is passed in
                c.clockwise_move(5) 
                c.swap(0,1,2,3,8,8,8,8)
                c.swap(0,1,2,3,7,7,7,7)
                c.swap(0,1,2,3,6,6,6,6)
            if s[i][1] == "'":
                c.anticlockwise_move(5)
                c.swap(0,3,2,1,8,8,8,8)
                c.swap(0,3,2,1,7,7,7,7)
                c.swap(0,3,2,1,6,6,6,6)
            if s[i][1] == "2":
                c.clockwise_move(5)
                c.clockwise_move(5)
                c.swap(0,1,2,3,8,8,8,8)
                c.swap(0,1,2,3,7,7,7,7)
                c.swap(0,1,2,3,6,6,6,6)
                c.swap(0,1,2,3,8,8,8,8)
                c.swap(0,1,2,3,7,7,7,7)
                c.swap(0,1,2,3,6,6,6,6)
        elif s[i][0] == 'R':
            #finalised
            if s[i][1] == '':
                c.clockwise_move(3)
                c.swap(4,0,5,2,2,2,2,6)
                c.swap(4,0,5,2,5,5,5,3)
                c.swap(4,0,5,2,8,8,8,0)
            if s[i][1] == "'":
                c.anticlockwise_move(3)
                c.swap(4,2,5,0,2,6,2,2)
                c.swap(4,2,5,0,5,3,5,5)
                c.swap(4,2,5,0,8,0,8,8)
            if s[i][1] == "2":
                c.clockwise_move(3)
                c.clockwise_move(3)
                c.swap(4,0,5,2,2,2,2,6)
                c.swap(4,0,5,2,5,5,5,3)
                c.swap(4,0,5,2,8,8,8,0)
                c.swap(4,0,5,2,2,2,2,6)
                c.swap(4,0,5,2,5,5,5,3)
                c.swap(4,0,5,2,8,8,8,0)
        elif s[i][0] == 'L':
            #finalised
            if s[i][1] == '':
                c.clockwise_move(1) 
                c.swap(4,2,5,0,0,8,0,0)
                c.swap(4,2,5,0,3,5,3,3)
                c.swap(4,2,5,0,6,2,6,6)
            if s[i][1] == "'":
                c.anticlockwise_move(1)
                c.swap(4,0,5,2,0,0,0,8)
                c.swap(4,0,5,2,3,3,3,5)
                c.swap(4,0,5,2,6,6,6,2)
            if s[i][1] == "2":
                c.clockwise_move(1)
                c.clockwise_move(1) 
                c.swap(4,2,5,0,0,8,0,0)
                c.swap(4,2,5,0,3,5,3,3)
                c.swap(4,2,5,0,6,2,6,6)
                c.swap(4,2,5,0,0,8,0,0)
                c.swap(4,2,5,0,3,5,3,3)
                c.swap(4,2,5,0,6,2,6,6)
        elif s[i][0] == 'F':
            #finalised
            if s[i][1] == '':
                c.clockwise_move(0) 
                c.swap(4,1,5,3,6,8,2,0)
                c.swap(4,1,5,3,7,5,1,3)
                c.swap(4,1,5,3,8,2,0,6)
            if s[i][1] == "'":
                c.anticlockwise_move(0)
                c.swap(4,3,5,1,8,6,0,2)
                c.swap(4,3,5,1,7,3,1,5)
                c.swap(4,3,5,1,6,0,2,8)
            if s[i][1] == "2":
                c.clockwise_move(0)
                c.clockwise_move(0)
                c.swap(4,1,5,3,6,8,2,0)
                c.swap(4,1,5,3,7,5,1,3)
                c.swap(4,1,5,3,8,2,0,6)
                c.swap(4,1,5,3,6,8,2,0)
                c.swap(4,1,5,3,7,5,1,3)
                c.swap(4,1,5,3,8,2,0,6)
        elif s[i][0] == 'B':
            #finalised
            if s[i][1] == '':
                c.clockwise_move(2) 
                c.swap(4,3,5,1,0,2,8,6)
                c.swap(4,3,5,1,1,5,7,3)
                c.swap(4,3,5,1,2,8,6,0)
            if s[i][1] == "'":
                c.anticlockwise_move(2)
                c.swap(4,1,5,3,2,0,6,8)
                c.swap(4,1,5,3,1,3,7,5)
                c.swap(4,1,5,3,0,6,8,2)
            if s[i][1] == "2":
                c.anticlockwise_move(2)
                c.anticlockwise_move(2)
                c.swap(4,3,5,1,0,2,8,6)
                c.swap(4,3,5,1,1,5,7,3)
                c.swap(4,3,5,1,2,8,6,0)
                c.swap(4,3,5,1,0,2,8,6)
                c.swap(4,3,5,1,1,5,7,3)
                c.swap(4,3,5,1,2,8,6,0)
    
    return c

#turns the cube into a string for display purposes
#also allows colour comparison for scramble map generation (in scramblemap.py, string cube is passed in to colour_to_BGR subroutine from colourscanning to turn letter into bgr colour value (ex: 'w' = (255,255,255)) )
def stringcube(current_cube):
    cube = current_cube
    y = cube.getcube()
    return y