from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap, QRegExpValidator
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QRegExp
import cv2
import os
from screen import Ui_MainWindow
from enum import Enum
from PIL import Image
from PIL.ExifTags import TAGS
from compare_func import compares
import humanize


class FunctionMode(Enum):
    SLIDER = 0
    FILEDETAILS = 1
    DIFF = 2


class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMinimumSize(1200, 800)
        self.setup_control()

    def setup_control(self):
        self.amplify_ratio = 1
        self.function_mode = FunctionMode.FILEDETAILS
        self.file_a_path = ""
        self.file_b_path = ""
        self.ui.slider_button.clicked.connect(self.click_slider_button)
        self.ui.file_details_button.clicked.connect(
            self.click_file_details_button)
        self.ui.difference_button.clicked.connect(self.click_difference_button)
        self.ui.file_a_button.clicked.connect(self.click_file_a_button)
        self.ui.file_b_button.clicked.connect(self.click_file_b_button)

        self.ui.zoom_in_button.clicked.connect(self.func_zoom_in)
        self.ui.zoom_out_button.clicked.connect(self.func_zoom_out)
        self.ui.reset_button.clicked.connect(self.reset_button)

        self.ui.diff_label.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.ui.ratioSlider.valueChanged.connect(
            self.ratio_slider_value_changed)
        self.ui.ratioSlider.sliderReleased.connect(self.ratio_slider_released)
        reg_01 = QRegExp('^1|(0\.[0-9]{1}[1-9]{1})$')
        reg01_validator = QRegExpValidator()
        reg01_validator.setRegExp(reg_01)
        self.ui.ratio_lineEdit.setValidator(reg01_validator)
        self.ui.ratio_lineEdit.setText(str(self.ui.ratioSlider.value() / 100))
        self.ui.ratio_lineEdit.textChanged.connect(
            self.ratio_lineEdit_value_changed)
        self.ui.compare_slider.valueChanged.connect(
            self.slider_slider_value_changed)
        # self.pixmap = self.ui.test_label.pixmap().copy()

    def slider_slider_value_changed(self):
        pass
        # print(int(self.pixmap.width() * (self.ui.compare_slider.value()/100)))
        # self.ui.test_label.setPixmap(self.pixmap.copy(
        #     0, 0, int(self.pixmap.width() * (self.ui.compare_slider.value()/100)), self.pixmap.height()))

    def ratio_slider_released(self):
        self._compute()

    def ratio_lineEdit_value_changed(self):
        try:
            value = int(float(self.ui.ratio_lineEdit.text()) * 100)
            self.ui.ratioSlider.setValue(value)
            # self._compute()
        except:
            pass
        # self.ui.ratioSlider.setValue(int(self.ui.ratio_lineEdit.text() * 100))

    def ratio_slider_value_changed(self):
        try:
            self.ui.ratio_lineEdit.setText(
                str(self.ui.ratioSlider.value() / 100))

        except:
            pass

    def click_file_a_button(self):
        file_name = QFileDialog.getOpenFileName()[0]
        self.file_a_path = file_name
        self.ui.file_a_button.setText(os.path.basename(file_name) + '📁')
        self._compute()

    def click_file_b_button(self):
        file_name = QFileDialog.getOpenFileName()[0]
        self.file_b_path = file_name
        self.ui.file_b_button.setText(os.path.basename(file_name) + '📁')
        self._compute()

    def click_slider_button(self):
        self.function_mode = FunctionMode.SLIDER
        self.ui.function_stacked_page.setCurrentWidget(self.ui.slider_page)
        self._compute()

    def click_difference_button(self):
        self.function_mode = FunctionMode.DIFF
        self.ui.function_stacked_page.setCurrentWidget(self.ui.difference_page)
        self._compute()

    def click_file_details_button(self):
        self.function_mode = FunctionMode.FILEDETAILS
        self.ui.function_stacked_page.setCurrentWidget(
            self.ui.file_details_page)
        self._compute()

    def _compute(self):
        if self.file_a_path == "" or self.file_b_path == "":
            return
        if self.function_mode == FunctionMode.SLIDER:
            self._slider_compute()
        elif self.function_mode == FunctionMode.FILEDETAILS:
            print('good')
            self._file_details_compute()
        elif self.function_mode == FunctionMode.DIFF:
            self._diff_compute()

    def _slider_compute(self):
        pass

    def _info_parse(self, path) -> str:
        image = Image.open(path)
        file_size = humanize.naturalsize(os.path.getsize(path))
        info = """File type: {file_type}
Size: {image_size}
Height: {image_height}px
Width: {image_width}px
Mode: {image_mode}""".format(file_type=image.format, image_size=file_size, image_height=image.height, image_width=image.width, image_mode=image.mode)

        exifdata = image.getexif()
        image.close()
        for (tag, value) in exifdata.items():
            key = TAGS.get(tag, tag)
            info = info + '\n' + key + ': ' + str(value)
            print(key + ' = ' + str(value))

        print(info)
        return info

    def _file_details_compute(self):

        self.ui.file_a_label.setPixmap(
            QPixmap(self.file_a_path).scaledToHeight(300))
        self.ui.file_b_label.setPixmap(
            QPixmap(self.file_b_path).scaledToHeight(300))
        self.ui.file_a_info.setText(self._info_parse(self.file_a_path))
        self.ui.file_b_info.setText(self._info_parse(self.file_b_path))

    def _diff_compute(self):
        img, reuslt_metrict, similarity = compares(float(self.ui.ratio_lineEdit.text()),
                                                   self.file_a_path, self.file_b_path)

        height, width, channel = img.shape

        bytesPerline = channel * width
        image_format = QImage.Format_RGB888 if channel == 3 else QImage.Format_RGBA8888
        self.qimg = QImage(img, width, height,
                           bytesPerline, image_format).rgbSwapped()
        self.ui.diff_label.setPixmap(QPixmap.fromImage(self.qimg))
        self.ui.similarity_label.setText(
            'Similarity: ' + str(round(similarity, 2)) + "%")

    def func_zoom_out(self):
        try:
            self.amplify_ratio /= 2
            self.img_resize()
        except:
            pass

    def func_zoom_in(self):
        try:
            self.amplify_ratio *= 2
            self.img_resize()
        except:
            pass

    def reset_button(self):
        try:
            self.amplify_ratio = 1
            self.img_resize()
        except:
            pass

    def img_resize(self):
        qpixmap = QPixmap.fromImage(self.qimg)
        scaled_pixmap = qpixmap.scaledToHeight(
            qpixmap.height() * self.amplify_ratio)
        self.ui.amplify_ratio_label.setText(str(self.amplify_ratio*100) + '%')
        # print(
        #     f"current img shape = ({scaled_pixmap.width()}, {scaled_pixmap.height()})")
        # self.ui.resolution_label.setText(
        #     f"({scaled_pixmap.width()}, {scaled_pixmap.height()})")
        self.ui.diff_label.setPixmap(scaled_pixmap)
        # def display_img(self):
        #     self.img = cv2.imread(self.img_path)
        #     height, width, channel = self.img.shape
        #     bytesPerline = 3 * width
        #     self.qimg = QImage(self.img, width, height,
        #                        bytesPerline, QImage.Format_RGB888).rgbSwapped()
        #     self.qpixmap = QPixmap.fromImage(self.qimg)
        #     # self.qpixmap_height = self.qpixmap.height()
        #     self.ui.picture_label.setPixmap(QPixmap.fromImage(self.qimg))
