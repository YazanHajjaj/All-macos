import cv2

# Define a video capture object
vid = cv2.VideoCapture(0)

while True:
    # Capture the video frame by frame
    ret, frame = vid.read()

    if not ret:
        # If the frame is not successfully captured, break the loop
        break   

    # Add text to the frame
    text = "Intro to EEE and CoE"
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50, 50)
    fontScale = 0.5
    color = (255, 0, 0)
    thickness = 2
    frame = cv2.putText(frame, text, org, font, fontScale, color, thickness, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('ESP32-CAM', frame)

    # Check for the 'q' button to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop, release the capture object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()
