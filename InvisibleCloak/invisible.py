# import the necessary packages
try:
    import cv2
    import numpy as np
    import time
    print('All modules are loaded..!')
except Exception as e:
    print('The following modules are missing {}'.format(e))

# to use laptop default camera for video capturing pass '0' otherwise '1'
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
time.sleep(3)

for i in range(60):
    check, backgorund = video.read()

# because laptop camera default shows us flipped images
backgorund = np.flip(backgorund, axis=1)

while(video.isOpened()):
    check, img = video.read()
    if check == False:
        break
    img = np.flip(img, axis=1)
    # converting RGB to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # hue=0, saturation=120, Brightness=50
    lower_red = np.array([0,120,50])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red) # mask1 detects red color as white and remaining BG as black

    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red) # mask1 detects red color as black and BG as white

    mask1 = mask1 + mask2

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8)) # MORPH_DILATE helps to remove noise

    mask2 = cv2.bitwise_not(mask1)

    res1 = cv2.bitwise_and(img, img, mask=mask2) # it makes BG img visible and our red cloth mask as black
    res2 = cv2.bitwise_and(backgorund, backgorund, mask=mask1)  # it makes cloth portion stores the static img from vid as visible and BG as black

    final = cv2.addWeighted(res1, 1, res2, 1, 0) # we are giving same weights for both res1, res2 and 0 for gamma correction
    cv2.imshow('final', final)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# destroying all windows
video.release()
cv2.destroyAllWindows()


