# Hand_Gesture_Based_Mouse_Control
This project uses computer vision and hand tracking to control the mouse cursor using hand gestures. By detecting specific hand landmarks, it can simulate mouse movements, left-click, and right-click actions without physical contact.

# Features
Mouse Movement: Moves the cursor based on the position of your index and middle fingers.
Left Click: Simulates a left-click when the thumb and index fingers are close together.
Right Click: Simulates a right-click when the index and middle fingers are close together.

# Requirements
Python 3.6+
OpenCV
Mediapipe
PyAutoGUI

# To install the dependencies, run:
pip install opencv-python mediapipe pyautogui

# How It Works
Hand Detection: Uses Mediapipe to detect hand landmarks.
Landmark Tracking:
Index Finger (ID: 8): Used to track cursor movement.
Middle Finger (ID: 12): When close to the index finger, it simulates a right-click.
Thumb (ID: 4): When close to the index finger, it simulates a left-click.
Mouse Control: Uses PyAutoGUI to move the cursor and perform click actions based on the finger positions.

# Usage
Run the script:
python main.py
A video feed window will open, showing real-time hand tracking.
Use gestures to control the mouse:
Move the index finger to control the cursor.
Bring the thumb close to the index finger for a left-click.
Bring the middle finger close to the index finger for a right-click.
Press 'q' to exit.

# Customization
You can adjust the distance thresholds for clicks or modify which gestures perform specific actions by tweaking the code in main.py.

# Troubleshooting
Ensure the camera is connected and working properly.
Run the script in a well-lit environment for better hand detection.
If gestures are not recognized correctly, try adjusting the threshold values in the code.
