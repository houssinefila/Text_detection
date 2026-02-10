import matplotlib.pyplot as plt 
import cv2
import easyocr 

cap = cv2.VideoCapture(1) 
reader = easyocr.Reader(['en'], gpu=True)

while True:
    success, img = cap.read()
    result = reader.readtext(img)
    for t in result:
        bbox , text, score = t
        cv2.rectangle(img, (int(bbox[0][0]), int(bbox[0][1])), (int(bbox[2][0]), int(bbox[2][1])), (255, 0, 255), 2)
        cv2.putText(img, text, (int(bbox[0][0]), int(bbox[0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
    cv2.imshow('Text Detection', img)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()