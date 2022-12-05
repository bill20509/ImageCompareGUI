from wand.image import Image
import re
import os
import numpy
import cv2


def compares(ratio, ans_file_path: str, diff_file_path: str, method='absolute'):
    metric_threshold = 0

    with Image(filename=ans_file_path) as base:
        with Image(filename=diff_file_path) as img:

            # Compare
            base.fuzz = base.quantum_range * ratio  # Threshold of 1%
            result_image, result_metric = base.compare(img, method)
            result_image.save(filename='save.png')
            img_buffer = numpy.asarray(
                bytearray(result_image.make_blob()), dtype=numpy.uint8)
            retval = cv2.imdecode(img_buffer, cv2.IMREAD_UNCHANGED)
            return retval
            # if img_buffer is not None:
            #     retval = cv2.imdecode(img_buffer, cv2.IMREAD_UNCHANGED)
            #     return retval
            # if result_metric == metric_threshold:
            #     result = "PASS: {0}".format(diff_file_path)
            #     print(result)
            #     return "PASS", result_metric
            # else:
            #     result = "FAIL: {0} result_metric = {1}".format(
            #         diff_file_path, result_metric)
            #     print(result)
            #     return "FAIL", result_metric
