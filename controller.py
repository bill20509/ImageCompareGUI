from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
import cv2
import os
from screen import Ui_MainWindow
from enum import Enum
from PIL import Image
from PIL.ExifTags import TAGS


class FunctionMode(Enum):
    SLIDER = 0
    FILEDETAILS = 1
    DIFF = 2


class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.img_path = 'bill.jpg'
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
        # self.ui.zoom_in_button.clicked.connect(self.func_zoom_in)
        # self.ui.zoom_out_button.clicked.connect(self.func_zoom_out)
        # self.ui.scrollArea.setWidgetResizable(True)
        # self.ui.picture_label.setAlignment(
        #     QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        # self.ui.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) # 將圖片置中
    #     self.display_img()

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

    def _file_details_compute(self):
        # image = Image.open(self.file_a_path)
        # info_dict = {
        #     "Image Size": image.size,
        #     "Image Height": image.height,
        #     "Image Width": image.width,
        #     "Image Format": image.format,
        #     "Image Mode": image.mode,
        # }
        # image.close()
        self.ui.file_a_info.setText(self.file_a_path)
        self.ui.file_b_info.setText(self.file_b_path)

    def _diff_compute(self):
        pass
        # def display_img(self):
        #     self.img = cv2.imread(self.img_path)
        #     height, width, channel = self.img.shape
        #     bytesPerline = 3 * width
        #     self.qimg = QImage(self.img, width, height,
        #                        bytesPerline, QImage.Format_RGB888).rgbSwapped()
        #     self.qpixmap = QPixmap.fromImage(self.qimg)
        #     # self.qpixmap_height = self.qpixmap.height()
        #     self.ui.picture_label.setPixmap(QPixmap.fromImage(self.qimg))

        # def func_zoom_in(self):
        #     self.amplify_ratio *= 2
        #     self.img_resize()

        # def func_zoom_out(self):
        #     self.amplify_ratio /= 2
        #     self.img_resize()

        # def img_resize(self):
        #     scaled_pixmap = self.qpixmap.scaledToHeight(
        #         self.qpixmap.height() * self.amplify_ratio)
        #     print(
        #         f"current img shape = ({scaled_pixmap.width()}, {scaled_pixmap.height()})")
        #     self.ui.resolution_label.setText(
        #         f"current img shape = ({scaled_pixmap.width()}, {scaled_pixmap.height()})")
        #     self.ui.picture_label.setPixmap(scaled_pixmap)
