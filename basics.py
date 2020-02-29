import cv2
import glob

img = glob.glob('*.jpg')
print(img)

# img = [cv2.imread('myimg.jpg',1),cv2.imread('bk2.jpg',1),cv2.imread('backup.jpg',1)]


#print(type(img))
#print(img)
#print(img.shape)

for i in img:
    print(i)
    python_img = cv2.imread(i,0)
    resized_img = cv2.resize(python_img,(1600,900))
    # resized_python_img=cv2.resize(python_img,(resized_img))
    name = "new" + i + ".jpg"
#resized_img = cv2.resize(img,(1600,900))    #(img.shape[1]//3,img.shape[0]//3))
    cv2.imwrite(name,resized_img)


#resized_img1 = cv2.resize(img1,(1600,900))   
#cv2.imwrite('Resized_image1.jpg',resized_img1)

#resized_img2 = cv2.resize(img2,(1600,900))  
#cv2.imwrite('Resized_image2.jpg',resized_img2)

#cv2.imshow('My Image',resized_img1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

