import cv2

# Load the pre-trained Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Access the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame. Exiting...")
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply binary thresholding
    _, bw_frame = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw bounding boxes around detected faces
    face_frame = frame.copy()  # Create a copy of the frame to draw bounding boxes
    for (x, y, w, h) in faces:
        cv2.rectangle(face_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(face_frame, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the different views
    cv2.imshow('Color Feed', frame)
    cv2.imshow('Grayscale Feed', gray_frame)
    cv2.imshow('Black and White Feed', bw_frame)
    cv2.imshow('Face Detection', face_frame)

    # Keyboard controls
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Quit
        break
    elif key == ord(' '):  # Pause
        print("Paused. Press any key to resume...")
        cv2.waitKey(0)

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
