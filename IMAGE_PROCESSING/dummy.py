import cv2
import numpy as np
import imutils
import pytesseract


def ratio(percent,image):
    return (image.shape[1]*percent/100)


img= cv2.imread('/home/pi/Desktop/pic25.jpg')
print(img.shape)
value=ratio(10,img)
img=img[180:800,int(value):int(img.shape[1]-value)]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original',gray)
cv2.waitKey(0)
print(gray.shape)


im_2=cv2.GaussianBlur(gray,(1,1),0)
kernel = np.ones((2,2),np.uint8)
thresh = cv2.erode(im_2, kernel, iterations=1)
thresh = cv2.dilate(thresh, kernel, iterations=2)
edged = cv2.Canny(im_2, 30, 200)
cv2.imshow('Canny Edge',edged)
cv2.waitKey(0)

keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break
mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0,255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)

(x,y) = np.where(mask==255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
cropped_image = gray[x1:x2+1, y1:y2+1]
cv2.imshow('Final',cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
cv2.waitKey(0)


#Copy image

further=cropped_image.copy()

ret, thresh1 = cv2.threshold(further, 199, 200, cv2.THRESH_OTSU | cv2.THRESH_BINARY)

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
rect_kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

dilate = cv2.dilate(thresh1, rect_kernel, iterations = 1)
erode = cv2.erode(dilate, rect_kernel2, iterations = 1)

cv2.imshow('Erode',erode)
cv2.waitKey(0)

print(pytesseract.image_to_string(dilate))






