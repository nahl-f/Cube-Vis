import cv2
# capturing the video from the users webcam
vid = cv2.VideoCapture(0)

while True:
    _, frame = vid.read()
    # making the HSV frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape
    cx = int(width//2)
    cy = int(height//2)
    # placing the scan circle margin in the middle of the frame
    cv2.circle(frame, (cx,cy), 10, (255,0,0), 3)
    # reading the colour from the middle of the HSV frame
    readcolour = hsv[cy,cx]
    print('Current colour HSV value', readcolour)
    cv2.imshow('colour radius', readcolour)
    colour = readcolour[0] 
    if colour < 5:
        cv2.putText(frame,'red',(144,549), cv2.FONT_HERSHEY_SIMPLEX, 4,(0,0,255),2,cv2.LINE_AA)
    elif colour < 10:
        cv2.putText(frame,'orange',(144,549), cv2.FONT_HERSHEY_SIMPLEX, 4,(0,128,255),2,cv2.LINE_AA)
    elif colour < 23:
        cv2.putText(frame,'white',(144,549), cv2.FONT_HERSHEY_SIMPLEX, 4,(255,255,255),2,cv2.LINE_AA)
    elif colour < 30:
        cv2.putText(frame,'yellow',(144,549), cv2.FONT_HERSHEY_SIMPLEX, 4,(255,255,0),2,cv2.LINE_AA)
    elif colour < 78:
        cv2.putText(frame,'green',(144,549), cv2.FONT_HERSHEY_SIMPLEX, 4,(0,255,0),2,cv2.LINE_AA)
    elif colour < 131:
        cv2.putText(frame,'blue',(144,549), cv2.FONT_HERSHEY_SIMPLEX, 4,(255,0,0),2,cv2.LINE_AA)
    else:
        pass
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
