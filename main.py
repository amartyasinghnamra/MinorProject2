# ============================================================
# ANTRIX - Camera Based Emotion Analysis System
# ============================================================
# Author      : Amartya Singh Namra
# Language    : Python
# Libraries   : OpenCV, DeepFace
#
# DESCRIPTION:
# Real-time AI emotion detection using webcam.
#
# FEATURES:
# ✔ Dynamic resizable window
# ✔ Proper application closing
# ✔ Safe error handling
# ✔ Real-time emotion detection
# ✔ Modular functions
# ✔ Beginner friendly structure
#
# EXIT:
# Press Q to close application completely
# ============================================================


# =========================
# IMPORT MODULES
# =========================

import cv2
from deepface import DeepFace
from datetime import datetime
import time
import sys


# =========================
# CONFIGURATION VARIABLES
# =========================

WINDOW_NAME = "ANTRIX Emotion Detection System"

CAMERA_INDEX = 0

FONT = cv2.FONT_HERSHEY_SIMPLEX

TEXT_THICKNESS = 2


# =========================
# INITIALIZE CAMERA
# =========================

def initialize_camera():
    """
    Initialize webcam safely.
    """

    print("\nInitializing webcam...\n")
    import platform

    if platform.system() == "Windows":
        camera = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)
    else:
        camera = cv2.VideoCapture(CAMERA_INDEX)

    # Allow camera startup time
    time.sleep(2)

    if not camera.isOpened():

        print("ERROR: Webcam could not be opened.")

        print("\nPossible Fixes:")
        print("1. Close Zoom / Teams / Discord")
        print("2. Check webcam permissions")
        print("3. Restart laptop")
        print("4. Try changing CAMERA_INDEX")

        sys.exit()

    print("Webcam initialized successfully.\n")

    return camera


# =========================
# CREATE DYNAMIC WINDOW
# =========================

def create_window():
    """
    Create resizable OpenCV window.
    """

    # WINDOW_NORMAL enables resizing
    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)

    # Initial size
    cv2.resizeWindow(WINDOW_NAME, 1000, 700)


# =========================
# READ FRAME SAFELY
# =========================

def get_frame(camera):
    """
    Read webcam frame safely.
    """

    success, frame = camera.read()

    if not success or frame is None:

        print("ERROR: Failed to capture frame.")

        return None

    # Ensure frame is valid
    if frame.shape[0] == 0 or frame.shape[1] == 0:

        print("ERROR: Empty frame detected.")

        return None

    return frame


# =========================
# DETECT EMOTION
# =========================

def detect_emotion(frame):
    """
    Detect emotion from webcam frame.
    """

    try:

        result = DeepFace.analyze(
            frame,
            actions=['emotion'],
            enforce_detection=False,
            silent=True
        )

        emotion = result[0]['dominant_emotion']

        return emotion.capitalize()

    except Exception as error:

        print("Emotion Detection Error:", error)

        return "Unknown"


# =========================
# DRAW TEXT ON FRAME
# =========================

def draw_information(frame, emotion):
    """
    Draw information on webcam frame.
    """

    # Project Title
    cv2.putText(
        frame,
        "ANTRIX AI SYSTEM",
        (20, 40),
        FONT,
        1,
        (255, 0, 0),
        TEXT_THICKNESS
    )

    # Emotion
    cv2.putText(
        frame,
        f"Emotion: {emotion}",
        (20, 90),
        FONT,
        0.9,
        (0, 255, 0),
        TEXT_THICKNESS
    )

    # Time
    current_time = datetime.now().strftime("%H:%M:%S")

    cv2.putText(
        frame,
        f"Time: {current_time}",
        (20, 140),
        FONT,
        0.7,
        (255, 255, 255),
        2
    )

    # Exit info
    cv2.putText(
        frame,
        "Press Q to Exit",
        (20, 190),
        FONT,
        0.7,
        (255, 255, 255),
        2
    )


# =========================
# DISPLAY FRAME
# =========================

def display_frame(frame):
    """
    Display frame safely.
    """

    try:

        cv2.imshow(WINDOW_NAME, frame)

    except Exception as error:

        print("Display Error:", error)


# =========================
# CLEAN APPLICATION EXIT
# =========================

def close_application(camera):
    """
    Release all resources properly.
    """

    print("\nClosing ANTRIX System...\n")

    try:

        if camera is not None:

            camera.release()

        cv2.destroyAllWindows()

        # Extra cleanup for Windows
        cv2.waitKey(1)

    except Exception as error:

        print("Cleanup Error:", error)

    print("Application closed successfully.")

    sys.exit()


# =========================
# MAIN APPLICATION LOOP
# =========================

def run_antrix_system():
    """
    Main system execution.
    """

    print("================================================")
    print("         ANTRIX EMOTION ANALYSIS SYSTEM")
    print("================================================")

    # Initialize components
    camera = initialize_camera()

    create_window()

    print("System started successfully.")
    print("Press Q to exit.\n")

    while True:

        # -------------------------
        # Capture webcam frame
        # -------------------------

        frame = get_frame(camera)

        if frame is None:

            continue

        # -------------------------
        # Detect emotion
        # -------------------------

        emotion = detect_emotion(frame)

        # -------------------------
        # Draw information
        # -------------------------

        draw_information(frame, emotion)

        # -------------------------
        # Show frame
        # -------------------------

        display_frame(frame)

        # -------------------------
        # Detect window close button
        # -------------------------

        window_status = cv2.getWindowProperty(
            WINDOW_NAME,
            cv2.WND_PROP_VISIBLE
        )

        # If user clicks X button
        if window_status < 1:

            close_application(camera)

        # -------------------------
        # Keyboard input
        # -------------------------

        key = cv2.waitKey(1) & 0xFF

        # Press Q to exit
        if key == ord('q') or key == ord('Q'):

            close_application(camera)


# =========================
# PROGRAM ENTRY POINT
# =========================

if __name__ == "__main__":

    try:

        run_antrix_system()

    except KeyboardInterrupt:

        print("\nProgram interrupted by user.")

        cv2.destroyAllWindows()

        sys.exit()

    except Exception as error:

        print("\nUnexpected System Error:")
        print(error)

        cv2.destroyAllWindows()

        sys.exit()