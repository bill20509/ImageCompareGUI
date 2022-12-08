from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap, QRegExpValidator, QPainter, QColor
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QRegExp
import os
from screen import Ui_MainWindow
from enum import Enum
from PIL import Image
from PIL.ExifTags import TAGS
from compare_func import compares
import humanize
import threading
from wand.image import Image as WandImage


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
        self.function_mode = FunctionMode.DIFF
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
        reg_01 = QRegExp('^1|(0\.[0-9]{1}[1-9]{1})$')
        reg01_validator = QRegExpValidator()
        reg01_validator.setRegExp(reg_01)
        self.ui.ratio_lineEdit.setValidator(reg01_validator)
        self.ui.ratio_lineEdit.setText(str(self.ui.ratioSlider.value() / 100))
        self.ui.ratio_lineEdit.textChanged.connect(
            self.ratio_lineEdit_value_changed)
        self.ui.compare_slider.valueChanged.connect(
            self.slider_slider_value_changed)
        self.file_a_pixmap = QPixmap()
        self.file_b_pixmap = QPixmap()
        self.slider_result_pixmap = QPixmap()
        self.diff_img = WandImage()
        self.ui.slider_zoom_in_button.clicked.connect(
            self.click_slider_zoom_in)
        self.ui.slider_zoom_out_button.clicked.connect(
            self.click_slider_zoom_out)
        self.ui.save_button.clicked.connect(self.click_save_button)
        # This slider reset button anyway..
        self.ui.pushButton_7.clicked.connect(self.slider_reset_button)

    def click_save_button(self):
        if self.file_a_path == "" or self.file_b_path == "":
            return
        name, extension = QFileDialog.getSaveFileName(
            self, 'Save File', os.path.basename(self.file_a_path).split('.')[0] + '_diff', filter=self.tr("Image(*.jpg;*.png)"))

        if name != '':
            self.diff_img.save(filename=name)

    def click_slider_zoom_out(self):
        try:
            if self.file_a_path == "" or self.file_b_path == "":
                return
            self.amplify_ratio /= 2
            self.slider_img_resize()
        except Exception as e:
            print(e)
            pass

    def click_slider_zoom_in(self):
        try:
            if self.file_a_path == "" or self.file_b_path == "":
                return
            self.amplify_ratio *= 2
            self.slider_img_resize()
        except Exception as e:
            print(e)
            pass

    def slider_reset_button(self):
        try:
            if self.file_a_path == "" or self.file_b_path == "":
                return
            self.amplify_ratio = 1
            self.slider_img_resize()
        except Exception as e:
            print(e)
            pass

    def slider_img_resize(self):
        # scaled_pixmap = self.slider_result_pixmap.scaledToHeight(
        #     self.slider_result_pixmap.height() * self.amplify_ratio)
        self.ui.slider_amplify_button.setText(
            str(self.amplify_ratio*100) + '%')
        self._compute()
        # self.ui.slide_a_label.setPixmap(scaled_pixmap)

    def slider_slider_value_changed(self):
        self._compute()

    def ratio_lineEdit_value_changed(self):
        try:
            value = int(float(self.ui.ratio_lineEdit.text()) * 100)
            self.ui.ratioSlider.setValue(value)
            t = threading.Thread(target=self._compute)
            t.start()
            # self._compute()
        except Exception as e:
            print(e)
            pass

    def ratio_slider_value_changed(self):
        try:
            self.ui.ratio_lineEdit.setText(
                str(self.ui.ratioSlider.value() / 100))

        except Exception as e:
            print(e)
            pass

    def click_file_a_button(self):
        file_name = QFileDialog.getOpenFileName(
            filter=self.tr("Image(*.jpg;*.png)"))[0]
        if file_name != '':
            self.file_a_path = file_name
            self.file_a_pixmap = QPixmap(self.file_a_path).copy()
            self.ui.file_a_button.setText(os.path.basename(file_name) + '📁')
            self._compute()

    def click_file_b_button(self):
        file_name = QFileDialog.getOpenFileName(
            filter=self.tr("Image(*.jpg;*.png)"))[0]
        if file_name != '':
            self.file_b_path = file_name
            self.file_b_pixmap = QPixmap(self.file_b_path).copy()
            self.ui.file_b_button.setText(os.path.basename(file_name) + '📁')
            self._compute()

    def click_slider_button(self):
        self.function_mode = FunctionMode.SLIDER
        self.ui.function_stacked_page.setCurrentWidget(self.ui.slider_page)
        self.ui.slider_amplify_button.setText(
            str(self.amplify_ratio*100) + '%')
        self._compute()

    def click_difference_button(self):
        self.function_mode = FunctionMode.DIFF
        self.ui.function_stacked_page.setCurrentWidget(self.ui.difference_page)
        self.ui.amplify_ratio_label.setText(str(self.amplify_ratio*100) + '%')
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
            self._file_details_compute()
        elif self.function_mode == FunctionMode.DIFF:
            self._diff_compute()

    def _slider_compute(self):
        pmap = self.file_a_pixmap.scaledToHeight(
            int(self.file_a_pixmap.height() * self.amplify_ratio)).copy()
        p = QPainter(pmap)
        p.setPen(QColor(255, 0, 0))
        w = int(pmap.width() *
                (self.ui.compare_slider.value()/1000))
        if self.ui.compare_slider.value() == 0:
            p.drawPixmap(0, 0, pmap.copy())
        else:
            p.drawPixmap(0, 0, self.file_b_pixmap.scaledToHeight(
                int(self.file_b_pixmap.height() * self.amplify_ratio)).copy(
                0, 0, w, self.file_a_pixmap.height()))
        p.drawLine(w, 0, w, pmap.height())
        p.end()
        # a = self.file_a_pixmap.
        self.slider_result_pixmap = pmap
        self.ui.slide_a_label.setPixmap(pmap)

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

        return info

    def _file_details_compute(self):

        self.ui.file_a_label.setPixmap(
            QPixmap(self.file_a_path).scaledToHeight(300))
        self.ui.file_b_label.setPixmap(
            QPixmap(self.file_b_path).scaledToHeight(300))
        self.ui.file_a_info.setText(self._info_parse(self.file_a_path))
        self.ui.file_b_info.setText(self._info_parse(self.file_b_path))

    def _diff_compute(self):
        wand_img, img, reuslt_metrict, similarity = compares(float(self.ui.ratio_lineEdit.text()),
                                                             self.file_a_path, self.file_b_path)
        height, width, channel = img.shape
        bytesPerline = channel * width
        image_format = QImage.Format_RGB888 if channel == 3 else QImage.Format_RGBA8888
        self.qimg = QImage(img, width, height,
                           bytesPerline, image_format).rgbSwapped()

        new_pixmap = QPixmap.fromImage(self.qimg).scaledToHeight(
            int(height * self.amplify_ratio))
        self.ui.diff_label.setPixmap(new_pixmap)
        # self.ui.diff_label.setPixmap(QPixmap.fromImage(self.qimg).scaledToHeight(
        #     int(height * self.amplify_ratio)))
        self.ui.similarity_label.setText(
            'Similarity: ' + str(round(similarity, 2)) + "%")
        self.diff_img = wand_img

    def func_zoom_out(self):
        try:
            if self.file_a_path == "" or self.file_b_path == "":
                return
            self.amplify_ratio /= 2
            self.img_resize()
        except Exception as e:
            print(e)
            pass

    def func_zoom_in(self):
        try:
            if self.file_a_path == "" or self.file_b_path == "":
                return
            self.amplify_ratio *= 2
            self.img_resize()
        except Exception as e:
            print(e)
            pass

    def reset_button(self):
        try:
            if self.file_a_path == "" or self.file_b_path == "":
                return
            self.amplify_ratio = 1
            self.img_resize()
        except Exception as e:
            print(e)
            pass

    def img_resize(self):
        qpixmap = QPixmap.fromImage(self.qimg)
        scaled_pixmap = qpixmap.scaledToHeight(
            qpixmap.height() * self.amplify_ratio)
        self.ui.amplify_ratio_label.setText(str(self.amplify_ratio*100) + '%')
        self.ui.diff_label.setPixmap(scaled_pixmap)
