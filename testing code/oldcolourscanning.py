import cv2
import time
#from ._scramblegen import *
#text_scramble = stringscramble(current_scramble)
#takes in HSV values and assigns colour
def video_frame(text_scramble):
    def colour_detect(hsv): 
        h = hsv[0] #hue
        s = hsv[1] #saturation
        v = hsv[2] #brightness
        #DO NOT CHANGE - WORKED PERFECTLY AT 6PM
        if (h < 5 or (h >= 150 and h <= 180)) and s > 150 and v <= 220:
            return 'r'  # red
        elif h >= 3 and h < 10 and s >= 130:
            return 'o'  # orange
        elif h >= 20 and h <= 40:
            return 'y'  # yellow
        elif h >= 65 and h <= 85 and s > 160 and v < 170:
            return 'g'  # green
        elif h <= 130 and s > 70:
            return 'b'  # blue
        elif (h <= 172 and s <= 100) or (h <=20 and s <= 30) and v > 150: 
            return 'w'  # white
        else:
            return ''
        # else:
        #     return ''
        # if (h < 5 or (h >= 150 and h <= 180)) and s > 150 and v <= 220:
        #     return 'r'  # red
        # elif h >= 3 and h < 10:
        #     return 'o'  # orange
        # elif h >= 20 and h <= 40:
        #     return 'y'  # yellow
        # elif h >= 65 and h <= 85 and s > 160 and v < 170:
        #     return 'g'  # green
        # elif h <= 130 and s > 70:
        #     return 'b'  # blue
        # # Updated white range to include lower saturation and higher value, and a wider range of hues
        # elif ((h <= 10 or h >= 170) and s <= 100 and v > 180) or (s <= 40 and v > 220):  
        #     return 'w'  # white
        # else:
        #     return ''
    #converts colour assigned to bgr value for display
    def colour_to_BGR(colour): 
        if colour == 'r':
            return (0,0,255)
        elif colour == 'o':
            return (0,115,255)
        elif colour == 'y':
            return (0,255,255)
        elif colour == 'g':
            return (0,255,0)
        elif colour == 'b':
            return (255,0,0)
        elif colour == 'w':
            return (255,255,255)
        else:
            return (66, 61, 59)
        
    #returns full name for display purposes
    def full_colour_name(side): 
        if side == 'g':
            return 'green'
        elif side == 'o':
            return 'orange'
        elif side == 'r':
            return 'red'
        elif side == 'y':
            return 'yellow'
        elif side == 'b':
            return 'blue'
        elif side == 'w':
            return 'white'
        else:
            return 'Done!'

    vid = cv2.VideoCapture(0)
    scanned_cube = []
    face_num = 0
    text_showing = False
    while True:
        _, frame = vid.read()
        height, width, _ = frame.shape
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #creates second hsv frame
        cv2.rectangle(frame, (712,216), (784,288), (255,255,255), 1) 
        cv2.rectangle(frame, (792,216), (864,288), (255,255,255), 1)
        cv2.rectangle(frame, (872,216),(944,288), (255,255,255), 1)
        cv2.rectangle(frame, (712,296), (784,368), (255,255,255), 1) 
        cv2.rectangle(frame, (792,296), (864,368), (255,255,255), 1)
        cv2.rectangle(frame, (872,296),(944,368), (255,255,255), 1)
        cv2.rectangle(frame, (712,376), (784,448), (255,255,255), 1)
        cv2.rectangle(frame, (792,376), (864,448), (255,255,255), 1)
        cv2.rectangle(frame, (872,376),(944,448), (255,255,255), 1)
        #Colour tracking pixels display
        cv2.circle(frame, (748,252), 5, (255,255,255),2)
        cv2.circle(frame, (748,332), 5, (255,255,255),2)
        cv2.circle(frame, (748,412), 5, (255,255,255),2)
        cv2.circle(frame, (828,252), 5, (255,255,255),2)
        cv2.circle(frame, (828,332), 5, (255,255,255),2)
        cv2.circle(frame, (828,412), 5, (255,255,255),2)
        cv2.circle(frame, (908,252), 5, (255,255,255),2)
        cv2.circle(frame, (908,332), 5, (255,255,255),2)
        cv2.circle(frame, (908,412), 5, (255,255,255),2)
        #Putting informational text
        cv2.rectangle(frame, (0, 0), (1280, 130), (92,33,11), -1)
        #cv2.putText(frame, 'Scramble Verification', (128, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,255,255), 6, cv2.LINE_AA)
        cv2.putText(frame, text_scramble, (15, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
        cv2.putText(frame, 'Follow the instructions detailed on the left side of the screen', (125, 190), cv2.FONT_HERSHEY_SIMPLEX, 1, (92,33,11), 2, cv2.LINE_AA)
        cv2.putText(frame, 'Press "Q" to exit', (530, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        if face_num <=5:
            cv2.putText(frame, 'Press the "S" key to scan the', (180, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
            cv2.putText(frame, 'coloured face', (300, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)

        #getting the HSV frames of each corner
        top_left = hsv[252,748]
        mid_left = hsv[332,748]
        bot_left = hsv[412,748]
        top_mid = hsv[252,828]
        mid = hsv[332,828]
        bot_mid = hsv[412,828]
        top_right = hsv[252,908]
        mid_right = hsv[332,908]
        bot_right = hsv[412,908]
        # TL = top_left[0]
        # ML = mid_left[0]
        # BL = bot_left[0]
        # TM = top_mid[0]
        # M = mid[0]
        # BM = bot_mid[0]
        # TR = top_right[0]
        # MR = mid_right[0]
        # BR = bot_right[0]

        # corner = [TL, ML, BL, TM, M, BM, TR, MR, BR]
        # for i in range(0,len(corner)):
        #     colourlist = [(0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0)]
        #     if  corner[i] < 5: #red
        #         colourlist[i]= (0,0,255)
        #     elif corner[i] < 10: #orange
        #         colourlist[i]= (0,115,255)
        #     elif corner[i] < 23: #white
        #         colourlist[i]= (255,255,255)
        #     elif corner[i] < 30: #yellow
        #         colourlist[i]= (0,255,255)
        #     elif corner[i] < 78: #green
        #         colourlist[i]= (0,255,0)
        #     elif corner[i] < 131: #blue
        #         colourlist[i]= (255,0,0)
        #     else:
                # pass
        #detecting colour of each corner using their hsv frame
        TL = colour_detect(top_left)
        ML = colour_detect(mid_left)
        BL = colour_detect(bot_left)
        TM = colour_detect(top_mid)
        M = colour_detect(mid)
        BM = colour_detect(bot_mid)
        TR = colour_detect(top_right)
        MR = colour_detect(mid_right)
        BR = colour_detect(bot_right)

        #Showing user current colours
        cv2.rectangle(frame, (954,216), (1026,288), colour_to_BGR(TL), -1) #TL
        cv2.rectangle(frame, (1034,216), (1106,288), colour_to_BGR(TM), -1) #TM
        cv2.rectangle(frame, (1114,216), (1186,288), colour_to_BGR(TR), -1) #TR
        cv2.rectangle(frame, (954,296), (1026,368), colour_to_BGR(ML), -1) #ML
        cv2.rectangle(frame, (1034,296), (1106,368), colour_to_BGR(M), -1) #M
        cv2.rectangle(frame, (1114,296), (1186,368), colour_to_BGR(MR), -1) #MR
        cv2.rectangle(frame, (954,376), (1026,448), colour_to_BGR(BL), -1) #BL
        cv2.rectangle(frame, (1034,376), (1106,448), colour_to_BGR(BM), -1) #BM
        cv2.rectangle(frame, (1114,376), (1186,448), colour_to_BGR(BR), -1) #BR

        corner = [TL, TM, TR, ML, M, MR, BL, BM, BR]
        sides = ['g', 'o', 'b', 'r', 'w', 'y', 'f'] #f = finished
        #displaying the side that has to be scanned next
        cv2.putText(frame, full_colour_name(sides[face_num]), (300, 330), cv2.FONT_HERSHEY_SIMPLEX, 3, colour_to_BGR(sides[face_num]), 4, cv2.LINE_AA)
        #scanning the cube when s pressed, only allows scanning for 5 faces
        if cv2.waitKey(1) & 0xFF == ord('s') and (face_num <= 5):
            face = []
            print('current middle colour: ', M)
            print('colour it is supposed to be: ', sides[face_num])
            if M == sides[face_num]:
                for i in corner:
                    current = i
                    face.append(current)
                scanned_cube.append(face)
                print('scanned face: ',face)
                face_num = face_num + 1
            else:
                print('Wrong side try again')
                #in order to show error message for 3 seconds
                text_showing = True
                error_start_time = time.time() #marking start time
        if text_showing == True:
            cv2.rectangle(frame, (130, 250), (1150, 500), (0,0,255), -1)
            cv2.putText(frame, 'Wrong coloured face', (150, 350), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,255,255), 4, cv2.LINE_AA)
            cv2.putText(frame, 'Try Again', (400, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,255,255), 5, cv2.LINE_AA)
            if (time.time() - error_start_time) >= 3: #using start time to calculate how long text has been displayed for
                text_showing = False 
        if face_num == 6: #new
            cv2.putText(frame, )

        #terminating program when q pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        #cv2.imshow('test', frame)
        #cv2.imshow('hsv', hsv)
        ret,buffer=cv2.imencode('.jpg',frame)
        frame=buffer.tobytes()
        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    vid.release()
    cv2.destroyAllWindows()
    for i in range(len(scanned_cube)):
        print(full_colour_name(scanned_cube[i][4]),':', scanned_cube[i])