import cv2

relative_path = 'test_pics/pic0.jpg'
img = cv2.imread(relative_path)
cv2.imshow('image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()

