# import the necessary packages
try:
    import cv2
    print('All modules are loaded..!')
except Exception as e:
    print('The following modules are missing {}'.format(e))

# to detect faces we need a classifier from cv2 site-packages
face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
'''
# to read and detect face from video(webcam)
video = cv2.VideoCapture(0, cv2.CAP_DSHOW) # 0-default camera, if we want use external camera we need to give the port number
while True:
    check, frame = video.read() # it helps us to store single frame. so we are writing inside while to store all frames in webcam video
    faces = face_data.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=10)
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow('livecam', frame)
    key = cv2.waitKey(1)
    if key ==  ord('q'):
        break
'''

# to read and detect faces from the given image
img = cv2.imread('RandomPeople.webp', 1) # returns color image if you give any other values then it returns Grayscale
faces = face_data.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5) # returns 2D-array with rows=no of faces available. 4 cols (x-coord,y-coord width, height)
print(faces)
for x,y,w,h in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2) # we are making rectangle on each face with green color (b,g,r) with border:2px
cv2.imshow('window', img)
cv2.waitKey(0) # window waits until we press any key

# to close all windows
cv2.destroyAllWindows()