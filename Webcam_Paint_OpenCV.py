import numpy as np
import cv2
from collections import deque

blueLower = np.array([100, 60, 60])
blueUpper = np.array([140, 255, 255])

kernel = np.ones((5, 5), np.uint8)


bpoints = [deque(maxlen=512)]
gpoints = [deque(maxlen=512)]
rpoints = [deque(maxlen=512)]
ypoints = [deque(maxlen=512)]

bindex = 0
gindex = 0
rindex = 0
yindex = 0

color = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
colorIndex = 0

brushSize = 2  # Initial brush size

# Setup the Paint interface
paintWindow = np.zeros((471, 636, 3)) + 255
paintWindow = cv2.rectangle(paintWindow, (40, 1), (140, 65), (0, 0, 0), 2)
paintWindow = cv2.rectangle(paintWindow, (160, 1), (255, 65), color[0], -1)
paintWindow = cv2.rectangle(paintWindow, (275, 1), (370, 65), color[1], -1)
paintWindow = cv2.rectangle(paintWindow, (390, 1), (485, 65), color[2], -1)
paintWindow = cv2.rectangle(paintWindow, (505, 1), (600, 65), color[3], -1)
cv2.putText(paintWindow, "CLEAR ALL", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 150, 150), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "Brush Size: {}".format(brushSize), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)

cv2.namedWindow('Paint', cv2.WINDOW_AUTOSIZE)

camera = cv2.VideoCapture(0)

while True:

    (grabbed, frame) = camera.read()
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    rectangles = [
        ((40, 1), (140, 65)),
        ((160, 1), (255, 65)),
        ((275, 1), (370, 65)),
        ((390, 1), (485, 65)),
        ((505, 1), (600, 65))
    ]


    corner_radius = 10

    # Rectangle 1
    x1, y1 = rectangles[0][0]
    x2, y2 = rectangles[0][1]
    cv2.rectangle(frame, (x1 + corner_radius, y1), (x2 - corner_radius, y2), (122, 122, 122), -1)
    cv2.rectangle(frame, (x1, y1 + corner_radius), (x2, y2 - corner_radius), (122, 122, 122), -1)
    cv2.circle(frame, (x1 + corner_radius, y1 + corner_radius), corner_radius, (122, 122, 122), -1)
    cv2.circle(frame, (x2 - corner_radius, y1 + corner_radius), corner_radius, (122, 122, 122), -1)
    cv2.circle(frame, (x1 + corner_radius, y2 - corner_radius), corner_radius, (122, 122, 122), -1)
    cv2.circle(frame, (x2 - corner_radius, y2 - corner_radius), corner_radius, (122, 122, 122), -1)

    # Rectangle 2
    x1, y1 = rectangles[1][0]
    x2, y2 = rectangles[1][1]
    cv2.rectangle(frame, (x1 + corner_radius, y1), (x2 - corner_radius, y2), color[0], -1)
    cv2.rectangle(frame, (x1, y1 + corner_radius), (x2, y2 - corner_radius), color[0], -1)
    cv2.circle(frame, (x1 + corner_radius, y1 + corner_radius), corner_radius, color[0], -1)
    cv2.circle(frame, (x2 - corner_radius, y1 + corner_radius), corner_radius, color[0], -1)
    cv2.circle(frame, (x1 + corner_radius, y2 - corner_radius), corner_radius, color[0], -1)
    cv2.circle(frame, (x2 - corner_radius, y2 - corner_radius), corner_radius, color[0], -1)

    # Rectangle 3
    x1, y1 = rectangles[2][0]
    x2, y2 = rectangles[2][1]
    cv2.rectangle(frame, (x1 + corner_radius, y1), (x2 - corner_radius, y2), color[1], -1)
    cv2.rectangle(frame, (x1, y1 + corner_radius), (x2, y2 - corner_radius), color[1], -1)
    cv2.circle(frame, (x1 + corner_radius, y1 + corner_radius), corner_radius, color[1], -1)
    cv2.circle(frame, (x2 - corner_radius, y1 + corner_radius), corner_radius, color[1], -1)
    cv2.circle(frame, (x1 + corner_radius, y2 - corner_radius), corner_radius, color[1], -1)
    cv2.circle(frame, (x2 - corner_radius, y2 - corner_radius), corner_radius, color[1], -1)

    # Rectangle 4
    x1, y1 = rectangles[3][0]
    x2, y2 = rectangles[3][1]
    cv2.rectangle(frame, (x1 + corner_radius, y1), (x2 - corner_radius, y2), color[2], -1)
    cv2.rectangle(frame, (x1, y1 + corner_radius), (x2, y2 - corner_radius), color[2], -1)
    cv2.circle(frame, (x1 + corner_radius, y1 + corner_radius), corner_radius, color[2], -1)
    cv2.circle(frame, (x2 - corner_radius, y1 + corner_radius), corner_radius, color[2], -1)
    cv2.circle(frame, (x1 + corner_radius, y2 - corner_radius), corner_radius, color[2], -1)
    cv2.circle(frame, (x2 - corner_radius, y2 - corner_radius), corner_radius, color[2], -1)

    # Rectangle 5
    x1, y1 = rectangles[4][0]
    x2, y2 = rectangles[4][1]
    cv2.rectangle(frame, (x1 + corner_radius, y1), (x2 - corner_radius, y2), color[3], -1)
    cv2.rectangle(frame, (x1, y1 + corner_radius), (x2, y2 - corner_radius), color[3], -1)
    cv2.circle(frame, (x1 + corner_radius, y1 + corner_radius), corner_radius, color[3], -1)
    cv2.circle(frame, (x2 - corner_radius, y1 + corner_radius), corner_radius, color[3], -1)
    cv2.circle(frame, (x1 + corner_radius, y2 - corner_radius), corner_radius, color[3], -1)
    cv2.circle(frame, (x2 - corner_radius, y2 - corner_radius), corner_radius, color[3], -1)


    
    cv2.putText(frame, "CLEAR ALL", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 150, 150), 2, cv2.LINE_AA)
    cv2.putText(frame, "Brush Size: {}".format(brushSize), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

    if not grabbed:
        break

    blueMask = cv2.inRange(hsv, blueLower, blueUpper)
    blueMask = cv2.erode(blueMask, kernel, iterations=2)
    blueMask = cv2.morphologyEx(blueMask, cv2.MORPH_OPEN, kernel)
    blueMask = cv2.dilate(blueMask, kernel, iterations=1)

    
    cnts, _ = cv2.findContours(blueMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(cnts) > 0:
        # Sort the contours and find the largest one -- we
        # will assume this contour correspondes to the area of the bottle cap
        cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
        # Get the moments to calculate the center of the contour (in this case Circle)
        M = cv2.moments(cnt)
        center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))

        if center[1] <= 65:
            if 40 <= center[0] <= 140:  # Clear All
                bpoints = [deque(maxlen=512)]
                gpoints = [deque(maxlen=512)]
                rpoints = [deque(maxlen=512)]
                ypoints = [deque(maxlen=512)]

                bindex = 0
                gindex = 0
                rindex = 0
                yindex = 0

                paintWindow[67:, :, :] = 255
            elif 160 <= center[0] <= 255:
                colorIndex = 0  # Blue
            elif 275 <= center[0] <= 370:
                colorIndex = 1  # Green
            elif 390 <= center[0] <= 485:
                colorIndex = 2  # Red
            elif 505 <= center[0] <= 600:
                colorIndex = 3  # Yellow
        else:
            if colorIndex == 0:
                bpoints[bindex].appendleft(center)
            elif colorIndex == 1:
                gpoints[gindex].appendleft(center)
            elif colorIndex == 2:
                rpoints[rindex].appendleft(center)
            elif colorIndex == 3:
                ypoints[yindex].appendleft(center)
    
    else:
        bpoints.append(deque(maxlen=512))
        bindex += 1
        gpoints.append(deque(maxlen=512))
        gindex += 1
        rpoints.append(deque(maxlen=512))
        rindex += 1
        ypoints.append(deque(maxlen=512))
        yindex += 1

    points = [bpoints, gpoints, rpoints, ypoints]
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                cv2.line(frame, points[i][j][k - 1], points[i][j][k], color[i], brushSize)
                cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], color[i], brushSize)

    
    cv2.imshow("Tracking", frame)
    cv2.imshow("Paint", paintWindow)

    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    elif key == ord("+"):  
        brushSize += 1
    elif key == ord("-") and brushSize > 1:  
        brushSize -= 1

    if key == ord("s"):
        cv2.imwrite(r"C:\Users\gsoum\Downloads\webcam Pic\tracked_image.png", frame)

        print("Image saved as 'tracked_image.png'")
    
    
    if key == ord("z"):
        for i in range(len(points)):
            for j in range(len(points[i])):
                if len(points[i][j]) > 1:
                    points[i][j].pop()  # Remove the last point

        paintWindow[:] = 255  # Clear paint window
        for i in range(len(points)):
            for j in range(len(points[i])):
                for k in range(1, len(points[i][j])):
                    if points[i][j][k - 1] is not None and points[i][j][k] is not None:
                        cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], color[i], brushSize)

    cv2.putText(frame, "Press 'Z' to Undo", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)



camera.release()
cv2.destroyAllWindows()
