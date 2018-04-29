import numpy
import cv2
import sys
imagePath = sys.argv[1]
cascPath = sys.argv[2]

#Creat Cascade
faceCascade = cv2.CascadeClassifier(cascPath)

#Read Image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Detect Face; Return A List
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor =1.1,
    minNeighbors =5,
    minSize =(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)

print("Detected {0} Faces".format(len(faces)))
# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found" ,image)
cv2.waitKey(0)