import cv2

img = cv2.imread('myimage.jpg')
img_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # преобразуем изображение в ч/б
cv2.imwrite('myimage_bw.jpg', img_bw)
