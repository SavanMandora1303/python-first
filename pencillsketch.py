import cv2
image = cv2.imread("image.jpg")
cv2.imshow("my image",image)
cv2.waitKey(0)

grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("grey image", grey_image)
cv2.waitKey(0)

inverted_image = 255 - grey_image
cv2.imshow("inverted image", inverted_image)
cv2.waitKey(0)

blurred = cv2.GaussianBlur(inverted_image, (21,21), 0)
inverted_blurred = 255 - blurred
pencill_sketch = cv2.divide(grey_image, inverted_blurred, scale=256.0)
cv2.imshow("pencill sketch",pencill_sketch)
cv2.waitKey(0)
cv2.imshow("original image",image)
cv2.imshow("pencill sketch image",pencill_sketch)
cv2.waitKey(0)

