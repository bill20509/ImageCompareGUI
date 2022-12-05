import cv2
import numpy as np
from wand.image import Image
# img = cv2.imread('bill.jpg')
# cv2.imshow('test', img)
# cv2.waitKey(0)
with Image(filename='bill.jpg') as base:
    img_buffer = np.asarray(bytearray(base.make_blob()), dtype=np.uint8)
    retval = cv2.imdecode(img_buffer, cv2.IMREAD_UNCHANGED)
    cv2.imshow('test', retval)
    cv2.waitKey(0)
