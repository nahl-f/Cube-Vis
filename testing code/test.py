import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #returns image that frame
    #cv2.imshow('frame', frame)
    #width = int(cap.get(3))
    #height = int(cap.get(4))
    # top left = 0,0
    #img = cv2.line(frame, (0,0) , (width,height), (255,0,0), 10)
    # source image, start, end, colour, line thickness (-1 to fill it in)
    #img = cv2.rectangle(img, (0,0), (width//2, height//2), (255,128,128), 5)
    #font = cv2.FONT_ITALIC
    # source, text, coordinate, font,scale, colour, thickness
    #img = cv2.putText(frame, 'CubeVis', (450,100), font, 4, (250, 250, 250), 7, cv2.LINE_AA)
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(img, 9, 0.2, 10)
    corners = np.int0(corners)
    for corner in corners:
        x,y = corner.ravel()
        cv2.circle(frame, (x,y), 5, (255,0,0), (7))
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


'''
def frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
        yield(b'--frame \r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
'''
