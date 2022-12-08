from wand.image import Image
import numpy
import cv2


def compares(ratio, ans_file_path: str, diff_file_path: str, method='absolute'):
    with Image(filename=ans_file_path) as base:
        with Image(filename=diff_file_path) as img:
            # Compare
            base.fuzz = base.quantum_range * ratio  # Threshold of 1%
            result_image, result_metric = base.compare(img, method)
            img_buffer = numpy.asarray(
                bytearray(result_image.make_blob()), dtype=numpy.uint8)
            retval = cv2.imdecode(img_buffer, cv2.IMREAD_UNCHANGED)
            return result_image, retval, result_metric, (1 - result_metric/(result_image.height*result_image.width)) * 100
