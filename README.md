VI. Real-Time Video Stream with CV
1. Webcam Video Capture
The app uses cv2.VideoCapture(0) to connect to your default webcam.
This continuously captures live video frames.

2. Display Live Video
Streamlit’s st.image() is used to show the video frames in real-time inside the app.
The video is displayed using a frame_placeholder, which gets updated every frame.

3. Apply Real-Time Filters or Detection
You can choose a video filter from a sidebar dropdown:
None: No change.
Grayscale: Converts the frame to black and white.
Canny Edge: Detects edges in the frame (with adjustable thresholds).
Face Detection: Detects faces using a pre-trained Haar Cascade model.

4. Filter Threshold Sliders
For the Canny Edge filter, users can adjust two threshold values using sliders in the sidebar to fine-tune edge detection.

5. Take a Snapshot
A 📸 Take Snapshot button allows users to capture a single frame.
Once clicked, the current frame is saved and displayed below the live video with a success message.

6. Face Detection
Uses a built-in OpenCV face detection model (haarcascade_frontalface_default.xml) to draw green rectangles around detected faces in the frame.
How It Works Internally:
Each frame is processed inside a while loop.
Based on the selected filter, the frame is modified before being shown.
If a snapshot is requested, the loop stops and displays the captured image.
The video stream is released (capture.release()) after processing.

Extra Touches:
The video is flipped horizontally (cv2.flip) for a mirror effect.
A small delay (time.sleep(0.03)) is added to reduce CPU usage

![image](https://github.com/user-attachments/assets/746a8476-c872-42bf-8934-87a24c90674e)

![image](https://github.com/user-attachments/assets/5f46a31a-2b84-400d-8f84-cc5026853174)
![image](https://github.com/user-attachments/assets/f4762061-16f3-4a80-b21c-50842e6df757)
