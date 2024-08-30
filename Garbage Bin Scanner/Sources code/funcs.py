import cv2
import os
def func():
    gar_Cascade = cv2.CascadeClassifier("garbagebin.xml")
    garid_Cascade = cv2.CascadeClassifier("garbagebinid.xml")
    cap = cv2.VideoCapture(0)
    cimg = 0
# Check if camera opened successfully
    if not os.path.exists('data'):
        os.makedirs('data')
    if not cap.isOpened():
        print("Error opening video stream or file")
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gbin = gar_Cascade.detectMultiScale(frame, 1.1, 1)
            for (x, y, w, h) in gbin:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
                gbinid = garid_Cascade.detectMultiScale(frame, 1.1, 2)

                for (gx, gy, gw, gh) in gbinid:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)
                    if cv2.rectangle(frame, (gx, gy), (gx+gw, gy+gh), (0, 255, 0), 5) in frame:
                        cv2.imwrite('./data/frame'+str(cimg)+'.jpg', frame)
                        cimg += 1
                        break
        # Display the resulting frame
            cv2.imshow('Frame', frame)
        # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
    # Break the loop
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

