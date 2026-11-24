from ultralytics import YOLO
import cv2, time

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture("primer.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.5, verbose=False)[0]

    for box in results.boxes:
        if int(box.cls) == 0:  # samo osobe
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)

    cv2.imshow("Detekcija", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
