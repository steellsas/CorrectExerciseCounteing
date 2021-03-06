import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
mp_drawing_styles = mp.solutions.drawing_styles

cap = cv2.VideoCapture('exercise1.mp4')

if (cap.isOpened() == False):
    print('some error with video')


# Read until video is completed
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:

    while(cap.isOpened()):
        ret, frame = cap.read()

        if ret:

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

            # Display the resulting frame
            cv2.imshow('Mediapipe Feed', image)
            if cv2.waitKey(25) & 0xFF == ord('q'):

                break
        else:
            break


