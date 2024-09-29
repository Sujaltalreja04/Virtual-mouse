Virtual Mouse Using Hand Gestures
Overview
The Virtual Mouse project enables users to control their computer cursor using hand gestures. By leveraging computer vision techniques with OpenCV and Mediapipe, this application tracks specific hand movements to simulate mouse actions like moving the cursor, clicking, double-clicking, right-clicking, and dragging files.

This project serves as an innovative interface for users, enhancing accessibility and user experience by allowing hands-free interaction with their devices.

Features
Cursor Movement: Smooth tracking of the cursor based on the position of the index finger.
Single & Double Clicks: Perform single and double clicks through pinch gestures between the thumb and index/middle fingers.
Right Clicks: Execute right-click actions using the ring finger and thumb pinch.
Drag-and-Drop: Enable drag-and-drop functionality by maintaining a pinch gesture while moving the cursor.
Smoothing Factor: Implemented to ensure stable and fluid cursor movement, minimizing abrupt jumps.
User-Friendly Interface: Real-time visual feedback displaying hand landmarks on the video feed.
Technologies Used
Python: Programming language used for the implementation.
OpenCV: Open-source computer vision library used for image processing.
Mediapipe: Framework for building multimodal applied machine learning pipelines, specifically for hand tracking in this project.
PyAutoGUI: Python library for programmatically controlling the mouse and keyboard.
Requirements
Before running the project, ensure you have the following libraries installed:

Python 3.x
OpenCV
Mediapipe
PyAutoGUI
NumPy
You can install the required libraries using pip:

bash
Copy code
pip install opencv-python mediapipe pyautogui numpy
Setup and Usage
Clone the Repository: Clone this repository to your local machine using:

bash
Copy code
git clone https://github.com/yourusername/virtual-mouse.git
Navigate to the Project Directory: Change to the project directory:

bash
Copy code
cd virtual-mouse
Run the Application: Execute the main script:

bash
Copy code
python virtual_mouse.py
Usage Instructions:

Cursor Movement: Move your index finger to control the cursor.
Left Click: Pinch your thumb and index finger together.
Double Click: Pinch your thumb and middle finger together quickly.
Right Click: Pinch your thumb and ring finger together.
Drag and Drop: Pinch your thumb and index finger, move to the desired location, and release to drop.
Exit the Application: Press q on your keyboard to close the application.

Troubleshooting
Ensure your camera is functioning and not used by another application.
Adjust lighting conditions for better hand detection performance.
Keep hands visible to the camera and maintain a clear background for optimal results.
Future Enhancements
Implement additional gestures for more mouse functionalities (e.g., scrolling, zooming).
Improve hand detection algorithms to work in various lighting conditions and backgrounds.
Create a graphical user interface (GUI) for easier settings adjustments.
Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Thanks to the creators of OpenCV and Mediapipe for providing powerful tools for computer vision and machine learning.
Inspired by the need for more accessible computing solutions.
