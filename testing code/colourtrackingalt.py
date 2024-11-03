import cv2
def colour_detect(hsv):
    h = hsv[0]
    s = hsv[1]
    v = hsv[2]
    #hsv[0] = the hue value
    #hsv[1] = the saturation value
    #hsv[2] = the brightness value
    if h < 5 or (h < 180 and h > 170) and s > 5:
        return (0,0,255) #red
    elif h <10 and h>=3:
        return (0,115,255) #orange
    elif h <= 40 and h>20:
        return (0,255,255) #yellow
    elif h>=65 and h<= 85 and s>160 and v<170:
        return (0,255,0) #green
    elif h <= 130 and s>70:
        return (255,0,0) #blue
    elif h <= 10 and s<=20 and v<180:
        return (255,255,255) #white
    return (255,255,255)

vid = cv2.VideoCapture(0)

while True:
    _, frame = vid.read()
    height, width, _ = frame.shape
    print('height',height)
    print('width', width)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.rectangle(frame, (712,216), (784,288), (255,255,255), 1) 
    cv2.rectangle(frame, (792,216), (864,288), (255,255,255), 1)
    cv2.rectangle(frame, (872,216),(944,288), (255,255,255), 1)
    cv2.rectangle(frame, (712,296), (784,368), (255,255,255), 1) 
    cv2.rectangle(frame, (792,296), (864,368), (255,255,255), 1)
    cv2.rectangle(frame, (872,296),(944,368), (255,255,255), 1)
    cv2.rectangle(frame, (712,376), (784,448), (255,255,255), 1)
    cv2.rectangle(frame, (792,376), (864,448), (255,255,255), 1)
    cv2.rectangle(frame, (872,376),(944,448), (255,255,255), 1)
    #Colour tracking
    cv2.circle(frame, (748,252), 5, (255,255,255),2)
    cv2.circle(frame, (748,332), 5, (255,255,255),2)
    cv2.circle(frame, (748,412), 5, (255,255,255),2)
    cv2.circle(frame, (828,252), 5, (255,255,255),2)
    cv2.circle(frame, (828,332), 5, (255,255,255),2)
    cv2.circle(frame, (828,412), 5, (255,255,255),2)
    cv2.circle(frame, (908,252), 5, (255,255,255),2)
    cv2.circle(frame, (908,332), 5, (255,255,255),2)
    cv2.circle(frame, (908,412), 5, (255,255,255),2)

    top_left = hsv[252,748]
    mid_left = hsv[332,748]
    bot_left = hsv[412,748]
    top_mid = hsv[252,828]
    mid = hsv[332,828]
    bot_mid = hsv[412,828]
    top_right = hsv[252,908]
    mid_right = hsv[332,908]
    bot_right = hsv[412,908]
    print("current colour",mid)
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
    cv2.rectangle(frame, (954,216), (1026,288), TL, -1) #TL
    cv2.rectangle(frame, (1034,216), (1106,288), TM, -1) #TM
    cv2.rectangle(frame, (1114,216), (1186,288),TR, -1) #TR
    cv2.rectangle(frame, (954,296), (1026,368), ML, -1) #ML
    cv2.rectangle(frame, (1034,296), (1106,368), M, -1) #M
    cv2.rectangle(frame, (1114,296), (1186,368), MR, -1) #MR
    cv2.rectangle(frame, (954,376), (1026,448), BL, -1) #BL
    cv2.rectangle(frame, (1034,376), (1106,448), BM, -1) #BM
    cv2.rectangle(frame, (1114,376), (1186,448), BR, -1) #BR

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow('test', frame)
vid.release()
cv2.destroyAllWindows()