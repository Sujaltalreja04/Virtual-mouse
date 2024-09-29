import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# Initialize camera, Mediapipe Hands, and drawing utilities
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

# Variables to track state
index_x, index_y = 0, 0
thumb_x, thumb_y = 0, 0
click_threshold = 20  # Threshold distance for clicking
dragging = False
prev_index_x, prev_index_y = 0, 0

# Time tracking for double-clicking
double_click_timeout = 0.3  # Maximum time between clicks for double-click
last_click_time = 0

# Smoothing factor for cursor movement
smoothing_factor = 10  # Increased smoothing for more stable cursor

# Delay between consecutive clicks to avoid rapid clicks
click_delay = 0.5  # 500ms delay between clicks
last_click_time_single = 0  # To track time for single clicks
last_click_time_right = 0  # To track time for right-clicks

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Mirror the frame
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand_landmarks in hands:
            drawing_utils.draw_landmarks(frame, hand_landmarks)  # Draw hand landmarks
            landmarks = hand_landmarks.landmark

            # Variables to track finger tips
            index_x, index_y, thumb_x, thumb_y, middle_x, middle_y, ring_x, ring_y = None, None, None, None, None, None, None, None

            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                # Track the Index Finger Tip (ID = 8)
                if id == 8:
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))

                # Track the Thumb Tip (ID = 4)
                if id == 4:
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 0))

                # Track the Middle Finger Tip (ID = 12) for Double Click
                if id == 12:
                    middle_x = screen_width / frame_width * x
                    middle_y = screen_height / frame_height * y
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(255, 0, 0))

                # Track the Ring Finger Tip (ID = 16) for Right Click
                if id == 16:
                    ring_x = screen_width / frame_width * x
                    ring_y = screen_height / frame_height * y
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 0, 255))

            # Cursor movement with smoothing
            if index_x and index_y:
                # Use moving average to smooth cursor movement
                index_x = prev_index_x + (index_x - prev_index_x) / smoothing_factor
                index_y = prev_index_y + (index_y - prev_index_y) / smoothing_factor
                prev_index_x, prev_index_y = index_x, index_y

                # Ensure cursor stays within screen bounds
                index_x = np.clip(index_x, 0, screen_width)
                index_y = np.clip(index_y, 0, screen_height)

                # Move the mouse cursor
                pyautogui.moveTo(index_x, index_y)

            # Left Click (Index and Thumb Pinch)
            if thumb_x and index_x:
                distance = np.linalg.norm(np.array([index_x, index_y]) - np.array([thumb_x, thumb_y]))
                current_time = time.time()
                if distance < click_threshold:  # Pinch detected
                    if not dragging and current_time - last_click_time_single > click_delay:  # Click once if not already dragging
                        pyautogui.click()
                        dragging = True  # Prevent multiple clicks
                        last_click_time_single = current_time  # Update last click time for single click
                else:
                    dragging = False  # Reset dragging state when fingers separate

            # Double Click (Middle and Thumb Pinch)
            if middle_x and thumb_x:
                distance = np.linalg.norm(np.array([middle_x, middle_y]) - np.array([thumb_x, thumb_y]))
                current_time = time.time()
                if distance < click_threshold:
                    if current_time - last_click_time < double_click_timeout:
                        pyautogui.doubleClick()  # Perform double click
                    last_click_time = current_time  # Update last click time

            # Right Click (Ring Finger and Thumb Pinch)
            if ring_x and thumb_x:
                distance = np.linalg.norm(np.array([ring_x, ring_y]) - np.array([thumb_x, thumb_y]))
                current_time = time.time()
                if distance < click_threshold and current_time - last_click_time_right > click_delay:
                    pyautogui.rightClick()
                    last_click_time_right = current_time  # Update last right-click time

            # Drag-and-Drop (Index and Thumb Pinch while moving)
            if thumb_x and index_x:
                distance = np.linalg.norm(np.array([index_x, index_y]) - np.array([thumb_x, thumb_y]))
                if distance < click_threshold:
                    if not dragging:
                        pyautogui.mouseDown()  # Start dragging
                        dragging = True
                    pyautogui.moveTo(index_x, index_y)
                else:
                    if dragging:
                        pyautogui.mouseUp()  # Stop dragging
                        dragging = False

    # Display the frame with landmarks
    cv2.imshow('Virtual Mouse', frame)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
