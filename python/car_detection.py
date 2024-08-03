import cv2
import serial

# Load pre-trained car detection Haar cascade
cascade_path = r'# Path to the downloaded XML file haarcascade_car.xml'  # Path to the downloaded XML file haarcascade_car.xml
car_cascade = cv2.CascadeClassifier(cascade_path)

# Open the video file
video_path = r'# Path to your video file cars_video.mp4'  # Path to your video file cars_video.mp4
cap = cv2.VideoCapture(video_path)

# Initialize serial connection with Arduino
ser = serial.Serial('COM5', 9600)  # Adjust port as needed, eg., COM5

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error reading frame. Exiting...")
        break

    # Convert frame to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cars in the frame
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=2, minSize=(40, 40))

    # Determine the lane of each car and send lane information to Arduino
    for (x, y, w, h) in cars:
        lane = "left" if x < frame.shape[1] / 2 else "right"
        ser.write(bytes(lane + '\n', 'utf-8'))

    # Draw rectangles around the detected cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Show the frame with car detections
    cv2.imshow('Incoming Car Detection', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()