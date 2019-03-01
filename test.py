import cv2
import numpy as np

video = cv2.VideoCapture("project_video.mp4")

while True:
    ret, orig_frame = video.read()
    if not ret:
        video = cv2.VideoCapture("project_video.mp4")
        continue

    frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # white color mask
    lower = np.uint8([200, 200, 200])
    upper = np.uint8([255, 255, 255])
    white_mask = cv2.inRange(hsv, lower, upper)

    # yellow color mask
    lower = np.uint8([18, 94, 140])
    upper = np.uint8([48, 255, 255])
    yellow_mask = cv2.inRange(hsv, lower, upper)

    # Combine the two above images
    mask = cv2.bitwise_or(white_mask, yellow_mask)
    masked = cv2.bitwise_and(hsv, hsv, mask=mask)
    edges = cv2.Canny(masked, 70, 150)

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow("frame", frame)
    cv2.imshow("edges", edges)

    key = cv2.waitKey(25)
    if key == 27:
        break
video.release()
cv2.destroyAllWindows()