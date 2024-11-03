#class structure

#Class Cube --> Main Class
#scrambles are applied to the cube and list is formed
#Class Coloured Cube --> Inherits from Scanned Cube
#used to make the opencv map of the cube once it is scanned. 
#It will use the second list that is made from the users scan to generate a coloured map. 
#Class Scanned Cube --> Inherits from Cube
#used to make the second list from the colours that user has scanned from own cube

#OR

#Class Cube --> Main Class
#scrambles are applied to the cueb and list is formed. 
#Class Face --> Main Class
#Each colour will be represented as it's own 2D list. 
#Class Draw Face --> Inherits from Face
#Draws the colours scanned from each face one at a time
#Class Scanned Face --> Inherits from Face
#Use to make a 1D list for each face scanned and append colours to it
#Scanned Cube would then become a for loop, 
#cube = []
#f = Scanned_Face()
# # getscannedface will be a bunch of if statements which will return the colour based on the i thing passed in
#must follow same colour convention of white = 0, orange = 1 etc. 
#for i in range(6):
#cube.append(f.getscannedface(i))

