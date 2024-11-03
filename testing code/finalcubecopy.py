
#s = gen()
s = [['U','2'], ['B','2'], ['F',"2"], ["L",''],["U","2"], ['L','2'], ['F','2'], ['R',"'"],['U','2'],['R',"'"],["D", ""],['R',"'"],["U","2"], ['L',''], ['B',"'"], ["D","'"], ['F',''], ['D','2'], ['U',"'"], ['B','2']]
#'w', 'w', 'w','w', 'w', 'w','w', 'w', 'w'
#'y', 'y', 'y','y', 'y', 'y','y', 'y', 'y'
#'1', '2', '3','4', '5', '6','7', '8', '9'
class Cube:
    def __init__(self):
        self.cube = [['w', 'w', 'w','w', 'w', 'w','w', 'w', 'w'],
                     ['o', 'o', 'o','o', 'o', 'o','o', 'o', 'o'],
                     ['g', 'g', 'g','g', 'g', 'g','g', 'g', 'g'],
                     ['r', 'r', 'r','r', 'r', 'r','r', 'r', 'r'],
                     ['b', 'b', 'b','b', 'b', 'b','b', 'b', 'b'],
                     ['y', 'y', 'y','y', 'y', 'y','y', 'y', 'y']]
        
    def clockwise_move(self,y): #will be used for all normal moves
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
        #Rotating the matrix (rows are turned into columns), 1st value of ori = last value of new sublist, 2nd value of ori = last value of next sublist etc..
        for i in range(3):
            for x in range(3):
                temp[x][2-i] = tempcube[i][x]
                pass
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
        
    def swap(self,x1, x2, x3, x4, y1, y2, y3, y4):
        self.cube[x1][y1], self.cube[x2][y2], self.cube[x3][y3], self.cube[x4][y4] = self.cube[x2][y2], self.cube[x3][y3], self.cube[x4][y4], self.cube[x1][y1]
        return self.cube
    
    def getcube(self):
        return self.cube
    
def scramble(s):
    c = Cube()
    for i in range(len(s)):
        if s[i][0] == 'U':
        #finalised
            if s[i][1] == '':
                c.clockwise_move(0)
                c.swap(2,3,4,1,0,0,0,0)
                c.swap(2,3,4,1,1,1,1,1)
                c.swap(2,3,4,1,2,2,2,2)
            if s[i][1] == "'":
                c.anticlockwise_move(0)
                c.swap(2,1,4,3,0,0,0,0)
                c.swap(2,1,4,3,1,1,1,1)
                c.swap(2,1,4,3,2,2,2,2)
            if s[i][1] == "2":
                c.clockwise_move(0)
                c.clockwise_move(0)
                c.swap(2,3,4,1,0,0,0,0)
                c.swap(2,3,4,1,1,1,1,1)
                c.swap(2,3,4,1,2,2,2,2)
                c.swap(2,3,4,1,0,0,0,0)
                c.swap(2,3,4,1,1,1,1,1)
                c.swap(2,3,4,1,2,2,2,2)
        elif s[i][0] == 'D':
            #finalised
            if s[i][1] == '':
                c.clockwise_move(5) 
                c.swap(2,1,4,3,8,8,8,8)
                c.swap(2,1,4,3,7,7,7,7)
                c.swap(2,1,4,3,6,6,6,6)
            if s[i][1] == "'":
                c.anticlockwise_move(5)
                c.swap(2,3,4,1,8,8,8,8)
                c.swap(2,3,4,1,7,7,7,7)
                c.swap(2,3,4,1,6,6,6,6)
            if s[i][1] == "2":
                c.clockwise_move(5)
                c.clockwise_move(5)
                c.swap(2,1,4,3,8,8,8,8)
                c.swap(2,1,4,3,7,7,7,7)
                c.swap(2,1,4,3,6,6,6,6)
                c.swap(2,1,4,3,8,8,8,8)
                c.swap(2,1,4,3,7,7,7,7)
                c.swap(2,1,4,3,6,6,6,6)
        elif s[i][0] == 'R':
            #finalised
            if s[i][1] == '':
                c.clockwise_move(3)
                c.swap(0,2,5,4,2,2,2,6)
                c.swap(0,2,5,4,5,5,5,3)
                c.swap(0,2,5,4,8,8,8,0)
            if s[i][1] == "'":
                c.anticlockwise_move(3)
                c.swap(0,4,5,2,2,6,2,2)
                c.swap(0,4,5,2,5,3,5,5)
                c.swap(0,4,5,2,8,0,8,8)
            if s[i][1] == "2":
                c.clockwise_move(3)
                c.clockwise_move(3)
                c.swap(0,2,5,4,2,2,2,6)
                c.swap(0,2,5,4,5,5,5,3)
                c.swap(0,2,5,4,8,8,8,0)
                c.swap(0,2,5,4,2,2,2,6)
                c.swap(0,2,5,4,5,5,5,3)
                c.swap(0,2,5,4,8,8,8,0)
        elif s[i][0] == 'L':
            #finalised
            if s[i][1] == '':
                c.clockwise_move(1) 
                c.swap(0,4,5,2,0,8,0,0)
                c.swap(0,4,5,2,3,5,3,3)
                c.swap(0,4,5,2,6,2,6,6)
            if s[i][1] == "'":
                c.anticlockwise_move(1)
                c.swap(0,2,5,4,0,0,0,8)
                c.swap(0,2,5,4,3,3,3,5)
                c.swap(0,2,5,4,6,6,6,2)
            if s[i][1] == "2":
                c.clockwise_move(1)
                c.clockwise_move(1) 
                c.swap(0,4,5,2,0,8,0,0)
                c.swap(0,4,5,2,3,5,3,3)
                c.swap(0,4,5,2,6,2,6,6)
                c.swap(0,4,5,2,0,8,0,0)
                c.swap(0,4,5,2,3,5,3,3)
                c.swap(0,4,5,2,6,2,6,6)
        elif s[i][0] == 'F':
            #finalised
            if s[i][1] == '':
                c.clockwise_move(2) 
                c.swap(0,1,5,3,6,8,2,0)
                c.swap(0,1,5,3,7,5,1,3)
                c.swap(0,1,5,3,8,2,0,6)
            if s[i][1] == "'":
                c.anticlockwise_move(2)
                c.swap(0,3,5,1,8,6,0,2)
                c.swap(0,3,5,1,7,3,1,5)
                c.swap(0,3,5,1,6,0,2,8)
            if s[i][1] == "2":
                c.clockwise_move(2)
                c.clockwise_move(2)
                c.swap(0,1,5,3,6,8,2,0)
                c.swap(0,1,5,3,7,5,1,3)
                c.swap(0,1,5,3,8,2,0,6)
                c.swap(0,1,5,3,6,8,2,0)
                c.swap(0,1,5,3,7,5,1,3)
                c.swap(0,1,5,3,8,2,0,6)
        elif s[i][0] == 'B':
            #finalised
            if s[i][1] == '':
                c.clockwise_move(4) #colour to be moved = blue hence 4
                c.swap(0,3,5,1,0,2,8,6)
                c.swap(0,3,5,1,1,5,7,3)
                c.swap(0,3,5,1,2,8,6,0)
            if s[i][1] == "'":
                c.anticlockwise_move(4)
                c.swap(0,1,5,3,2,0,6,8)
                c.swap(0,1,5,3,1,3,7,5)
                c.swap(0,1,5,3,0,6,8,2)
            if s[i][1] == "2":
                c.anticlockwise_move(4)
                c.anticlockwise_move(4)
                c.swap(0,3,5,1,0,2,8,6)
                c.swap(0,3,5,1,1,5,7,3)
                c.swap(0,3,5,1,2,8,6,0)
                c.swap(0,3,5,1,0,2,8,6)
                c.swap(0,3,5,1,1,5,7,3)
                c.swap(0,3,5,1,2,8,6,0)
    y = c.getcube()
    for row in y:
        print(row)
    return c 