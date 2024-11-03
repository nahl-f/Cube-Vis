import cv2

vid = cv2.VideoCapture(0)
ScannedCube = []
def detect(corner, face): #subroutine that checks the colours on the face
        if corner < 5:
            cv2.putText(frame,'red',(144,549), cv2.FONT_HERSHEY_SIMPLEX, 4,(0,0,255),2,cv2.LINE_AA)
            face.append('r')
            return face
        elif corner < 10:
            cv2.putText(frame,'orange',(144,549), cv2.FONT_HERSHEY_SIMPLEX, 4,(0,128,255),2,cv2.LINE_AA)
            face.append('o')
            return face
        elif corner < 23:
            cv2.putText(frame,'white',(144,549), cv2.FONT_HERSHEY_SIMPLEX, 4,(255,255,255),2,cv2.LINE_AA)
            face.append('w')
            return face
        elif corner < 30:
            cv2.putText(frame,'yellow',(144,549), cv2.FONT_HERSHEY_SIMPLEX, 4,(255,255,0),2,cv2.LINE_AA)
            face.append('y')
            return face
        elif corner < 78:
            cv2.putText(frame,'green',(144,549), cv2.FONT_HERSHEY_SIMPLEX, 4,(0,255,0),2,cv2.LINE_AA)
            face.append('g')
            return face
        elif corner < 131:
            cv2.putText(frame,'blue',(144,549), cv2.FONT_HERSHEY_SIMPLEX, 4,(255,0,0),2,cv2.LINE_AA)
            face.append('b')
            return face
        else:
            pass

def puttext(i,frame):
    if i == 'G':
        cv2.putText(frame, 'Scan the Green Face', (int(height//2),int(width//2)), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)  
    elif i == 'R':
        cv2.putText(frame, 'Scan the Red Face', (100,50), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)
    elif i == 'B':
        cv2.putText(frame, 'Scan the Blue Face', (100,50), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)
    elif i == 'O':
        cv2.putText(frame, 'Scan the Orange Face', (100,50), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)
    elif i == 'W':
        cv2.putText(frame, 'Scan the White Face', (100,50), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)
    elif i == 'Y':
        cv2.putText(frame, 'Scan the Yellow Face', (100,50), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)

face = 0
while True:
    _, frame = vid.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape
    cx = int(width//2)
    cy = int(height//2)
    # to draw the boundaries for the user to scan with
    cv2.circle(frame, (cx,cy), 10, (255,255,255), 3) # middle
    cv2.circle(frame, (cx,int(height//3)), 10, (255,255,255), 3) # top middle
    cv2.circle(frame, (cx, int(height//3)*2), 10, (255,255,255), 3) # bottom middle
    cv2.circle(frame, (int(width//3), cy), 10, (255,255,255), 3) #middle left
    cv2.circle(frame, (int(width//3)*2, cy), 10, (255,255,255), 3) #middle right
    cv2.circle(frame, (int(width//3), int(height//3)), 10, (255,255,255), 3) #top left
    cv2.circle(frame, (int(width//3)*2, int(height//3)), 10, (255,255,255), 3) # top right
    cv2.circle(frame, (int(width//3)*2, int(height//3)*2), 10, (255,255,255), 3) #bottom right
    cv2.circle(frame, (int(width//3),int(height//3)*2), 10, (255,255,255), 3) # bottom left
    
    # k = cv2.waitKey(1)
    # if k%256 == 32:

    top_left = hsv[int(height//3), int(width//3)]
    mid_left = hsv[cy, int(width//3)]
    bot_left = hsv[int(height//3)*2,int(width//3)]
    top_mid = hsv[int(height//3),cx]
    mid = hsv[cy,cx]
    bot_mid = [int(height//3)*2, cx]
    top_right = hsv[int(height//3),int(width//3)*2]
    mid_right = hsv[cy, int(width//3)*2]
    bot_right = hsv[int(height//3)*2,int(width//3)*2]

    #cv2.imshow('colour radius', top_left)
    # corner = [TL, ML, BL, TM, M, BM, TR, MR, BR]
    # for i in corner:
    #     print('corner',i)
    #     k = cv2.waitKey(1)
    #     if k%256 == 32:
    #         if  i < 5:
    #             cv2.putText(frame,'red',(144,549), cv2.FONT_HERSHEY_SIMPLEX, 4,(0,0,255),2,cv2.LINE_AA)
    #         elif i < 10:
    #             cv2.putText(frame,'orange',(144,549), cv2.FONT_HERSHEY_SIMPLEX, 4,(0,128,255),2,cv2.LINE_AA)
    #         elif i < 23:
    #             cv2.putText(frame,'white',(144,549), cv2.FONT_HERSHEY_SIMPLEX, 4,(255,255,255),2,cv2.LINE_AA)
    #         elif i < 30:
    #             cv2.putText(frame,'yellow',(144,549), cv2.FONT_HERSHEY_SIMPLEX, 4,(255,255,0),2,cv2.LINE_AA)
    #         elif i < 78:
    #             cv2.putText(frame,'green',(144,549), cv2.FONT_HERSHEY_SIMPLEX, 4,(0,255,0),2,cv2.LINE_AA)
    #         elif i < 131:
    #             cv2.putText(frame,'blue',(144,549), cv2.FONT_HERSHEY_SIMPLEX, 4,(255,0,0),2,cv2.LINE_AA)
    #         else:
    #             pass
    #     x = cv2.waitKey(10)
    #     if x == ord('n'):
    #         continue
    TL = top_left[0]
    ML = mid_left[0]
    BL = bot_left[0]
    TM = top_mid[0]
    M = mid[0]
    BM = bot_mid[0]
    TR = top_right[0]
    MR = mid_right[0]
    BR = bot_right[0]
    corner = [TL, TM, TR, ML, M, MR, BL, BM, BR]
    if cv2.waitKey(1) == ord('s') and (face < 6):
        f = []
        print('Test')
        centre = ['G', 'R', 'B', 'O', 'W', 'Y']
        cv2.circle(frame, (cx,cy), 5, (255,0,0), 5)
        cv2.putText(frame, 'Scan the Yellow Face', (int(height//2), int(width//2)), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        # i = centre[face]
        #puttext(centre[face], frame)
        # if i == 'G':
        #     cv2.putText(frame, 'Scan the Green Face', (int(height//2),int(width//2)), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)  
        # elif i == 'R':
        #     cv2.putText(frame, 'Scan the Red Face', (100,50), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)
        # elif i == 'B':
        #     cv2.putText(frame, 'Scan the Blue Face', (100,50), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)
        # elif i == 'O':
        #     cv2.putText(frame, 'Scan the Orange Face', (100,50), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)
        # elif i == 'W':
        #     cv2.putText(frame, 'Scan the White Face', (100,50), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)
        # elif i == 'Y':
        #     cv2.putText(frame, 'Scan the Yellow Face', (100,50), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)
        # print(centre[face])
        for i in corner:
            current = detect(i, f)
        ScannedCube.append(current)
        print(current)
        print(ScannedCube)
        print(centre[face])
        print("I have entered the if")
        face += 1

            # if i == 'G':
            #     f = []
            #     cv2.putText(frame, 'Scan the Green Face', (100,50), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)
            #     for i in corner:
            #         face = detect(i,f)
            #     ScannedCube.append(face)
            #     print(face)
            #     print(ScannedCube)
            # elif i == 'R':
            #     f = []
            #     cv2.putText(frame, 'Scan the Red Face', (100,50), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)
            #     for i in corner:
            #         face = detect(i,f)
            #     ScannedCube.append(face)
            #     print(face)
            #     print(ScannedCube)
            # elif i == 'B':
            #     f = []
            #     cv2.putText(frame, 'Scan the Blue Face', (100,50), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)
            #     for i in corner:
            #         face = detect(i,f)
            #     ScannedCube.append(face)
            #     print(face)
            #     print(ScannedCube)
            # elif i == 'O':
            #     f = []
            #     cv2.putText(frame, 'Scan the Orange Face', (100,50), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)
            #     for i in corner:
            #         face = detect(i,f)
            #     ScannedCube.append(face)
            #     print(face)
            #     print(ScannedCube)
            # elif i == 'W':
            #     f = []
            #     cv2.putText(frame, 'Scan the White Face', (100,50), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)
            #     for i in corner:
            #         face = detect(i,f)
            #     ScannedCube.append(face)
            #     print(face)
            #     print(ScannedCube)
            # elif i == 'Y':
            #     f = []
            #     cv2.putText(frame, 'Scan the Yellow Face', (100,50), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)
            #     for i in corner:
            #         face = detect(i,f)
            #     ScannedCube.append(face)
            #     print(face)
            #     print(ScannedCube)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    cv2.imshow('CubeVis',frame)
vid.release()
cv2.destroyAllWindows()
