import cv2
import mediapipe as face
import pyautogui as pg
cam = cv2.VideoCapture(0)
face_mesh = face.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_Width, screen_higth = pg.size()
while True:
   _, frame = cam.read()
   frame = cv2.flip(frame, 1)
   rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
   value = face_mesh.process(rgb_frame)
   points = value.multi_face_landmarks
   frame_hight, frame_width, _ = frame.shape
   if points:
      landmarks = points[0].landmark
      for id, landmark in enumerate(landmarks[474:478]):
         
         x = int (landmark.x*frame_hight)
         y = int (landmark.y*frame_width)
         cv2.circle(frame, (x,y), 3, (0,250,0))
         if id == 1:
            screen_x = 2*screen_Width/frame_width*x
            screen_y = 2*screen_higth/frame_hight*y
            pg.moveTo(screen_x, screen_y)
      left = [landmarks[145], landmarks[159]]
      for landmark in left:
         x = int (landmark.x*frame_hight)
         y = int (landmark.y*frame_width)
         cv2.circle(frame, (x,y), 3, (0,250,255))
      if(left[0].y - left[1].y) < 0.0068:
         print('click')
         pg.click()

   cv2.imshow('Awuse', frame)
   cv2.waitKey(1)