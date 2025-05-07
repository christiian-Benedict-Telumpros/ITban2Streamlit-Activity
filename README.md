
IV. Fetch and Display API Data
In this task, we demonstrate how to integrate live data from a public API—specifically, COVID-19 statistics—from the disease.sh API and visualize the information interactively using Streamlit widgets and data charts.
Steps and Features Implemented:

1. API Integration with requests:
A GET request is made to fetch country-wise COVID-19 statistics.
The JSON response is parsed into a Python dictionary and then converted to a Pandas DataFrame.

2.Data Cleaning & Preparation:
Key columns such as cases, deaths, recovered, etc., are selected.
Null values are filled, and all data types are coerced into numeric formats to prevent visualization issues.

3.Sidebar Filters:
Users can select one or more countries from a multiselect widget to filter the data.
If no countries are selected or the selected ones aren’t found, a fallback to default countries ensures continuity.

4. Interactive Data Display:
The filtered DataFrame is shown in a scrollable table using st.dataframe.
![image](https://github.com/user-attachments/assets/858bb644-8730-4efa-a292-f7e6d4b5e6fb)

V. Data Pipeline with Database (MySQL Integration)
1. Connect to a MySQL Database
The app uses SQLAlchemy to establish a connection to a MySQL database (task5telumpros).
Connection details like username, password, host, port, and database name are configured.

2. Fetch and Filter Data
A function (fetch_data) runs SQL queries to retrieve data from the database.
It supports using parameters (like filtering by username).

3. Display Data with st.dataframe
After a user logs in, their data is displayed using st.dataframe, which creates a table-like view in the Streamlit app.

4. Insert New Rows (Sign Up Form)
The sign-up form allows new users to register by entering a username, password, and email.
The password is hashed for security using the bcrypt library before it's stored in the database.

5. User Authentication (Bonus Feature)
Users can log in using their credentials.
The login process includes verifying that the password entered matches the hashed password stored in the database.
If the login is successful, the user is welcomed, and their data is shown.

6. View All Users
There's a "View Users" page that shows all usernames and emails from the users table.
![image](https://github.com/user-attachments/assets/f6dda7c1-9d89-4acb-be60-eab947a37574)
![image](https://github.com/user-attachments/assets/01f677d8-1660-4a8a-a931-badf67fb2f61)
![image](https://github.com/user-attachments/assets/a1e944fe-f77b-45e9-b850-ffa1dad160a6)

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
![image](https://github.com/user-attachments/assets/edb355b3-c815-4384-9da9-55a04ac96ee4)
![image](https://github.com/user-attachments/assets/23b1db7c-8f9a-46cf-a84b-8087c1d685b7)

