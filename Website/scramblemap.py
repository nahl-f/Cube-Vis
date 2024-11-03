import cv2
import numpy as np
from .cube import *
from .colourscanning import colour_to_BGR
from flask import make_response

def generate_scramble_map():
    print(stringscramble(current_scramble))
    current_cube = scramble(current_scramble)
    string_cube = stringcube(current_cube) 
    #making an image with width 720, height 558 and rgb colour depth (3), data type is an 8 bit np array
    scramble_map = np.zeros((558, 720, 3), dtype=np.uint8)
    
    cv2.rectangle(scramble_map, (0,0), (720,720), (92,33,11), -1)

    #grid
    cv2.line(scramble_map, (198,203), (198, 355), (255,255,255), 1)
    cv2.line(scramble_map, (360,203), (360, 355), (255,255,255), 1)
    cv2.line(scramble_map, (522,203), (522, 355), (255,255,255), 1)
    cv2.line(scramble_map, (203,198), (355, 198), (255,255,255), 1)
    cv2.line(scramble_map, (203,360), (355, 360), (255,255,255), 1)
    #orange face
    cv2.rectangle(scramble_map, (41, 203), (85,247), colour_to_BGR(string_cube[1][0]), -1)
    cv2.rectangle(scramble_map, (95, 203), (139,247), colour_to_BGR(string_cube[1][1]), -1)
    cv2.rectangle(scramble_map, (149,203), (193,247), colour_to_BGR(string_cube[1][2]), -1)
    cv2.rectangle(scramble_map, (41, 257), (85,301), colour_to_BGR(string_cube[1][3]), -1)
    cv2.rectangle(scramble_map, (95, 257), (139,301), colour_to_BGR(string_cube[1][4]), -1)
    cv2.rectangle(scramble_map, (149,257), (193,301), colour_to_BGR(string_cube[1][5]), -1)
    cv2.rectangle(scramble_map, (41, 311), (85,355), colour_to_BGR(string_cube[1][6]), -1)
    cv2.rectangle(scramble_map, (95, 311), (139,355), colour_to_BGR(string_cube[1][7]), -1)
    cv2.rectangle(scramble_map, (149,311), (193,355), colour_to_BGR(string_cube[1][8]), -1)

    #green face
    cv2.rectangle(scramble_map, (203, 203), (247,247), colour_to_BGR(string_cube[0][0]), -1)
    cv2.rectangle(scramble_map, (257, 203), (301,247), colour_to_BGR(string_cube[0][1]), -1)
    cv2.rectangle(scramble_map, (311, 203), (355,247), colour_to_BGR(string_cube[0][2]), -1)
    cv2.rectangle(scramble_map, (203, 257), (247,301), colour_to_BGR(string_cube[0][3]), -1)
    cv2.rectangle(scramble_map, (257, 257), (301,301), colour_to_BGR(string_cube[0][4]), -1)
    cv2.rectangle(scramble_map, (311, 257), (355,301), colour_to_BGR(string_cube[0][5]), -1)
    cv2.rectangle(scramble_map, (203, 311), (247,355), colour_to_BGR(string_cube[0][6]), -1)
    cv2.rectangle(scramble_map, (257, 311), (301,355), colour_to_BGR(string_cube[0][7]), -1)
    cv2.rectangle(scramble_map, (311, 311), (355,355), colour_to_BGR(string_cube[0][8]), -1)

    #red face
    cv2.rectangle(scramble_map, (365, 203), (409,247), colour_to_BGR(string_cube[3][0]), -1)
    cv2.rectangle(scramble_map, (419, 203), (463,247), colour_to_BGR(string_cube[3][1]), -1)
    cv2.rectangle(scramble_map, (473, 203), (517,247), colour_to_BGR(string_cube[3][2]), -1)
    cv2.rectangle(scramble_map, (365, 257), (409,301), colour_to_BGR(string_cube[3][3]), -1)
    cv2.rectangle(scramble_map, (419, 257), (463,301), colour_to_BGR(string_cube[3][4]), -1)
    cv2.rectangle(scramble_map, (473, 257), (517,301), colour_to_BGR(string_cube[3][5]), -1)
    cv2.rectangle(scramble_map, (365, 311), (409,355), colour_to_BGR(string_cube[3][6]), -1)
    cv2.rectangle(scramble_map, (419, 311), (463,355), colour_to_BGR(string_cube[3][7]), -1)
    cv2.rectangle(scramble_map, (473, 311), (517,355), colour_to_BGR(string_cube[3][8]), -1)

    #blue face
    cv2.rectangle(scramble_map, (527, 203), (571,247), colour_to_BGR(string_cube[2][0]), -1)
    cv2.rectangle(scramble_map, (581, 203), (625,247), colour_to_BGR(string_cube[2][1]), -1)
    cv2.rectangle(scramble_map, (635, 203), (679,247), colour_to_BGR(string_cube[2][2]), -1)
    cv2.rectangle(scramble_map, (527, 257), (571,301), colour_to_BGR(string_cube[2][3]), -1)
    cv2.rectangle(scramble_map, (581, 257), (625,301), colour_to_BGR(string_cube[2][4]), -1)
    cv2.rectangle(scramble_map, (635, 257), (679,301), colour_to_BGR(string_cube[2][5]), -1)
    cv2.rectangle(scramble_map, (527, 311), (571,355), colour_to_BGR(string_cube[2][6]), -1)
    cv2.rectangle(scramble_map, (581, 311), (625,355), colour_to_BGR(string_cube[2][7]), -1)
    cv2.rectangle(scramble_map, (635, 311), (679,355), colour_to_BGR(string_cube[2][8]), -1)

    #white face
    cv2.rectangle(scramble_map, (203, 41), (247,85), colour_to_BGR(string_cube[4][0]), -1)
    cv2.rectangle(scramble_map, (257, 41), (301,85), colour_to_BGR(string_cube[4][1]), -1)
    cv2.rectangle(scramble_map, (311, 41), (355,85), colour_to_BGR(string_cube[4][2]), -1)
    cv2.rectangle(scramble_map, (203, 95), (247,139), colour_to_BGR(string_cube[4][3]), -1)
    cv2.rectangle(scramble_map, (257, 95), (301,139), colour_to_BGR(string_cube[4][4]), -1)
    cv2.rectangle(scramble_map, (311, 95), (355,139), colour_to_BGR(string_cube[4][5]), -1)
    cv2.rectangle(scramble_map, (203, 149), (247,193), colour_to_BGR(string_cube[4][6]), -1)
    cv2.rectangle(scramble_map, (257, 149), (301,193), colour_to_BGR(string_cube[4][7]), -1)
    cv2.rectangle(scramble_map, (311, 149), (355,193), colour_to_BGR(string_cube[4][8]), -1)

    #yellow face
    cv2.rectangle(scramble_map, (203, 365), (247,409), colour_to_BGR(string_cube[5][0]), -1)
    cv2.rectangle(scramble_map, (257, 365), (301,409), colour_to_BGR(string_cube[5][1]), -1)
    cv2.rectangle(scramble_map, (311, 365), (355,409), colour_to_BGR(string_cube[5][2]), -1)
    cv2.rectangle(scramble_map, (203, 419), (247,463), colour_to_BGR(string_cube[5][3]), -1)
    cv2.rectangle(scramble_map, (257, 419), (301,463), colour_to_BGR(string_cube[5][4]), -1)
    cv2.rectangle(scramble_map, (311, 419), (355,463), colour_to_BGR(string_cube[5][5]), -1)
    cv2.rectangle(scramble_map, (203, 473), (247,517), colour_to_BGR(string_cube[5][6]), -1)
    cv2.rectangle(scramble_map, (257, 473), (301,517), colour_to_BGR(string_cube[5][7]), -1)
    cv2.rectangle(scramble_map, (311, 473), (355,517), colour_to_BGR(string_cube[5][8]), -1)
    
    return scramble_map

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()