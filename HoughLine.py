import cv2     # import libraries of python OpenCV where its functionality resides
import numpy as np   # np is an alias pointing to numpy library

video = cv2.VideoCapture("project_video.mp4")

while True:
    ret, orig_frame = video.read()        # reads frames from a camera
    if not ret:
        video = cv2.VideoCapture("project_video.mp4")  # capture frames from a camera
        continue

    frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #low_yellow = np.array([18, 94, 140])      # define range of colors
    #up_yellow = np.array([48, 255, 255])
    #mask = cv2.inRange(hsv, low_yellow, up_yellow)       # creating a color boundary
    #edges = cv2.Canny(mask, 75, 150)   # finds edges in the input and marks them in the output edges


    # white color mask
    lower = np.uint8([200, 200, 200])
    upper = np.uint8([255, 255, 255])
    white_mask = cv2.inRange(orig_frame, lower, upper)

    # yellow color mask
    lower = np.uint8([18, 94, 140])
    upper = np.uint8([48, 255, 255])
    yellow_mask = cv2.inRange(orig_frame, lower, upper)

    # combine the mask
 #   mask = cv2.bitwise_or(white_mask, yellow_mask)
  #  masked = cv2.bitwise_and(orig_frame, orig_frame, mask = mask)
   # edges = cv2.Canny(masked, 70, 150)

    # Filter white pixels
 #   white_threshold = 200
  #  lower_white = np.uint8([white_threshold, white_threshold, white_threshold])
   # upper_white = np.uint8([255, 255, 255])
    #white_mask = cv2.inRange(orig_frame, lower_white, upper_white)
    white_image = cv2.bitwise_and(orig_frame, orig_frame, mask=white_mask)

    # Filter yellow pixels
#    lower_yellow = np.uint8([90, 100, 100])
 #   upper_yellow = np.uint8([110, 255, 255])
  #  yellow_mask = cv2.inRange(orig_frame, lower_yellow, upper_yellow)
    yellow_image = cv2.bitwise_and(orig_frame, orig_frame, mask=yellow_mask)

    # Combine the two above images
  #  edges = cv2.addWeighted(white_image, 1., yellow_image, 1., 0.)
    mask = cv2.bitwise_or(white_mask, yellow_mask)
    masked = cv2.bitwise_and(orig_frame, orig_frame, mask = mask)
    edges = cv2.Canny(masked, 75, 150)


    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow("frame", frame)        # Display the original video
    cv2.imshow("edges", edges)

    key = cv2.waitKey(25)       # Wait for Esc key to stop
    if key == 27:
        break

video.release()   # Close the window
cv2.destroyAllWindows()
