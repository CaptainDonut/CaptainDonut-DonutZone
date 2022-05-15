import numpy as np
import cv2

img_merge = cv2.imread('assets/merged.png',0)
img_line = cv2.imread('match/line.png',0)

h, w = img_line.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img_merge2 = img_merge.copy()

    result = cv2.matchTemplate(img_merge, img_line, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)    
    cv2.rectangle(img_merge2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img_merge2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()