import cv2, time

# load the pretrained cascade from file 
CASCADE_DIR = cv2.__path__[0] + '/data/'
faceCascade = cv2.CascadeClassifier(CASCADE_DIR+'haarcascade_frontalface_default.xml')

# init camera
cap = cv2.VideoCapture(0)
time.sleep(2.0)

# for fps computation
t0 = time.time()
nframes = 0

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    scale = 400/frame.shape[1]

    # Resize to fit into 400x300, convert to grayscale to feed to the cascade
    frame_small = cv2.resize(frame, (0,0), fx=scale, fy=scale)
    gray = cv2.cvtColor(frame_small, cv2.COLOR_BGR2GRAY)

    # Run through the Haar cascade to get the faces array
    faces = faceCascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame_small, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Compute fps and put text over the frame
    nframes += 1
    t1 = time.time()
    avg_fps = nframes / (t1-t0)
    msg = "{:.1f} fps on average -- press 'q' to exit".format(avg_fps)
    cv2.putText(frame_small, msg, (30, 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Detection Test', frame_small)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When done, release the capture and close the window
cap.release()
cv2.destroyWindow('Face Detection Test')

