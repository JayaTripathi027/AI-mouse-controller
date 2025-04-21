import cv2
import mediapipe as mp
import pyautogui

# face_mesh = mp.solutions.face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks =True)
screen_w , screen_h =pyautogui.size()
while True:
    a, frame= cap.read()
    frame = cv2.flip(frame,1
                     )
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmarks_point = output.multi_face_landmarks
    frame_h , frame_w , _= frame.shape
    if landmarks_point:
        landmarks = landmarks_point[0].landmark
        for id, landmark in enumerate(landmarks[474 :478]):
            x = int(landmark.x*frame_w)
            y =  int(landmark.y*frame_h)
            cv2.circle(frame, (x,y),3,(0,255, 0))

            if id == 1:
                screen_x= screen_w / frame_w * x
                screen_y = screen_h/ frame_h* y
                # screen_y = int(landmark.y*screen_h)
                pyautogui.moveTo(screen_x , screen_y)
            # print(x,y)
        left = [landmarks[145],landmarks[159]]
        for landmark in left:
            x = int(landmark.x*frame_w)
            y =  int(landmark.y*frame_h)
            cv2.circle(frame, (x,y),3,(0,255, 255))
        if (left[0].y - left[1].y) <0.004:
            pyautogui.click()
            pyautogui.sleep(1)

            # print('click')   

    # print(landmarks_point)
    cv2.imshow('eye controller Mouse', frame)
    cv2.waitKey(1)

    cv2.imshow('Eye Controller Mouse', frame)
    
    # Check for the 'q' key press to break the loop and close the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

