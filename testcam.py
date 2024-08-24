import cv2
import face_recognition
import numpy 

capture=cv2.VideoCapture(0)#0 for internal camera, 1 for external camera

while True:  #creat an infite loop
     # Capture frame-by-frame
    ret,frame=capture.read()
    #ret: A boolean value that indicates whether the frame was successfully captured. 
    # It will be True if the frame was read correctly, and False otherwise 
    # (e.g., if the camera is not connected or there are no more frames to read from a video file).

    #resize a small frame to process fast and recogzie imediate
    samll_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = numpy.ascontiguousarray(samll_frame[:, :, ::-1])
    
    face_location=face_recognition.face_locations(rgb_small_frame)
    face_encodings=face_recognition.face_encodings(rgb_small_frame, face_location)
    for top, right, bottom, left in face_location:
        top*=4
        right*=4 
        bottom*=4 
        left*=4

        cv2.rectangle(frame,(left,top),(right ,bottom), (255,100.100),2)
     # Display the frame
    cv2.imshow('Camera',frame) #opeing camera 
    # Wait for 10 milliseconds for a key press, this happens every 10 millsec bascialy because the infinit loop above 
    k = cv2.waitKey(10)

    if k%256==27:# If the 'Esc' key is pressed, exit the loop ,ascii code 27 
        #If the 'Esc' key is pressed, exit the loop
        print('closing')
        break 

# Release the camera meaing freeing all resources used and close all windows todo a clean exit 
capture.release()
cv2.destroyAllWindows()