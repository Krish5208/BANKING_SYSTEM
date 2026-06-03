import cv2
import os


# Realtime Face Detection
# No database / no image saving

def detect_live_face():

    camera = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        'haarcascade_frontalface_default.xml'
    )

    print('\nScanning Face...')
    print('Press ESC to cancel')

    while True:

        ret, frame = camera.read()

        if not ret:
            print('Camera Error')
            return False

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5
        )

        for (x, y, w, h) in faces:

            cv2.rectangle(
                frame,
                (x, y),
                (x+w, y+h),
                (255, 0, 0),
                2
            )

            cv2.putText(
                frame,
                'Face Detected',
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

            cv2.imshow('Realtime Face Authentication', frame)

            print('\nLive Face Detected Successfully')

            camera.release()
            cv2.destroyAllWindows()
 
            return True

        cv2.imshow('Realtime Face Authentication', frame)

        key = cv2.waitKey(1)

        if key == 27:
            break

    camera.release()
    cv2.destroyAllWindows()

    return False

def windows_hello_auth():

    print('\nStarting Windows Hello Authentication...')

    print(
        'Use your fingerprint or face using Windows Hello.'
    )

    # Opens Windows Sign-In Settings
    os.system('start ms-settings:signinoptions')

    # Since direct fingerprint APIs are restricted,
    # we simulate successful Windows verification.

    response = input(
        '\nDid Windows Hello verify successfully? (yes/no): '
    )

    if response.lower() == 'yes':

        print('Windows Hello Authentication Successful')

        return True

    else:

        print('Windows Hello Authentication Failed')

        return False

