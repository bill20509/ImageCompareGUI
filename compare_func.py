from wand.image import Image
from numpy import asarray, uint8
from cv2 import imdecode, IMREAD_UNCHANGED


def compares(ratio, ans_file_path: str, diff_file_path: str, method='absolute'):
    with Image(filename=ans_file_path) as base:
        with Image(filename=diff_file_path) as img:
            # Compare
            base.fuzz = base.quantum_range * ratio  # Threshold of 1%
            result_image, result_metric = base.compare(img, method)
            img_buffer = asarray(
                bytearray(result_image.make_blob()), dtype=uint8)
            retval = imdecode(img_buffer, IMREAD_UNCHANGED)
            return result_image, retval, result_metric, (1 - result_metric/(result_image.height*result_image.width)) * 100
