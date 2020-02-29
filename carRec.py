import cv2

car_cascade = cv2.CascadeClassifier(r'car.xml')

video = cv2.VideoCapture(r'P1033666.mp4')
while True:
    check,frame = video.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray,scaleFactor =3,minNeighbors = 5)

    for x,y,w,h in cars :
        rectangle = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,235,59),3) 

#print(type(video))

    cv2.imshow('Gray Image',frame)
    cv2.waitKey(1)
cv2.destroyAllWindows()
video.release 