import cv2
import face_recognition

img = cv2.imread("images\\Bill Gates66_600.jpg")
rgb_img =  cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]


img1 = cv2.imread("images\\Bill Gates68_602.jpg")
rgb_img1 =  cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img_encoding1 = face_recognition.face_encodings(rgb_img1)[0]

read_img = face_recognition.compare_faces([img_encoding],img_encoding1)
print("Image",read_img)

cv2.imshow("Img",img)
cv2.imshow("Img2",img1)
cv2.waitKey(0)
