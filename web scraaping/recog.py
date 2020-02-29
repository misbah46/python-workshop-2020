import cv2

face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(r'faceDetection.mp4')
while True:
    check,frame = video.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,scaleFactor =3,minNeighbors = 5)

    for x,y,w,h in faces:
        rectangle = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,235,59),3) 

#print(type(video))

    cv2.imshow('Gray Image',frame)
    cv2.waitKey(1)
cv2.destroyAllWindows()
video.release    

'''img = cv2.imread("photo2.jpg",1)  
img1 = cv2.imread("photo.jpg",1)
img2 = cv2.imread("photo3.jpg",1)   

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,scaleFactor =5,minNeighbors = 5)
print(faces)

faces1 = face_cascade.detectMultiScale(gray_img1,scaleFactor = 1.05,minNeighbors = 5)
print(faces1)

faces2 = face_cascade.detectMultiScale(gray_img2,scaleFactor = 1.05,minNeighbors = 5)
print(faces2)

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,235,59),3)

cv2.imshow('Gray Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

