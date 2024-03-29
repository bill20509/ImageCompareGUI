# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(604, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setStyleSheet("QPushButton {\n"
                                 "    color: #333;\n"
                                 "    border: 2px solid #888;\n"
                                 "    border-radius: 10px;\n"
                                 "   background-color: #888;\n"
                                 "    padding: 5px;\n"
                                 "    }\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "    background: qradialgradient(\n"
                                 "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                 "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                 "        );\n"
                                 "    }\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    border-style: inset;\n"
                                 "    background: qradialgradient(\n"
                                 "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                 "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                 "        );\n"
                                 "    }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalFrame_2 = QtWidgets.QFrame(self.horizontalFrame)
        self.verticalFrame_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.verticalFrame_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.verticalFrame_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalFrame_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.verticalFrame_2)
        self.line = QtWidgets.QFrame(self.horizontalFrame)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalFrame = QtWidgets.QFrame(self.horizontalFrame)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.verticalFrame)
        self.stackedWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalFrame_4 = QtWidgets.QFrame(self.page)
        self.horizontalFrame_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.horizontalFrame_4.setObjectName("horizontalFrame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalFrame_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.slider_button = QtWidgets.QPushButton(self.horizontalFrame_4)
        self.slider_button.setObjectName("slider_button")
        self.horizontalLayout_6.addWidget(self.slider_button)
        self.difference_button = QtWidgets.QPushButton(self.horizontalFrame_4)
        self.difference_button.setObjectName("difference_button")
        self.horizontalLayout_6.addWidget(self.difference_button)
        self.file_details_button = QtWidgets.QPushButton(
            self.horizontalFrame_4)
        self.file_details_button.setObjectName("file_details_button")
        self.horizontalLayout_6.addWidget(self.file_details_button)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_4.addWidget(self.horizontalFrame_4)
        self.horizontalFrame_2 = QtWidgets.QFrame(self.page)
        self.horizontalFrame_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.file_a_button = QtWidgets.QPushButton(self.horizontalFrame_2)
        self.file_a_button.setObjectName("file_a_button")
        self.horizontalLayout_4.addWidget(self.file_a_button)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.file_b_button = QtWidgets.QPushButton(self.horizontalFrame_2)
        self.file_b_button.setObjectName("file_b_button")
        self.horizontalLayout_4.addWidget(self.file_b_button)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_4.addWidget(self.horizontalFrame_2)
        self.horizontalFrame_5 = QtWidgets.QFrame(self.page)
        self.horizontalFrame_5.setObjectName("horizontalFrame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.function_stacked_page = QtWidgets.QStackedWidget(
            self.horizontalFrame_5)
        self.function_stacked_page.setObjectName("function_stacked_page")
        self.slider_page = QtWidgets.QWidget()
        self.slider_page.setObjectName("slider_page")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.slider_page)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalFrame_7 = QtWidgets.QFrame(self.slider_page)
        self.horizontalFrame_7.setMaximumSize(QtCore.QSize(16777215, 100))
        self.horizontalFrame_7.setObjectName("horizontalFrame_7")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(
            self.horizontalFrame_7)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.slider_zoom_out_button = QtWidgets.QPushButton(
            self.horizontalFrame_7)
        self.slider_zoom_out_button.setObjectName("slider_zoom_out_button")
        self.slider_zoom_out_button.setMinimumSize(QtCore.QSize(30, 0))
        self.slider_zoom_out_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.horizontalLayout_12.addWidget(self.slider_zoom_out_button)
        self.slider_amplify_button = QtWidgets.QLabel(self.horizontalFrame_7)
        self.slider_amplify_button.setObjectName("slider_amplify_button")
        self.horizontalLayout_12.addWidget(self.slider_amplify_button)
        self.slider_zoom_in_button = QtWidgets.QPushButton(
            self.horizontalFrame_7)
        self.slider_zoom_in_button.setObjectName("slider_zoom_in_button")
        self.slider_zoom_in_button.setMinimumSize(QtCore.QSize(30, 0))
        self.slider_zoom_in_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.horizontalLayout_12.addWidget(self.slider_zoom_in_button)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_12)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalFrame_7)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_11.addWidget(self.pushButton_7)
        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.verticalLayout_8.addWidget(self.horizontalFrame_7)
        self.compare_slider = QtWidgets.QSlider(self.slider_page)
        self.compare_slider.setOrientation(QtCore.Qt.Horizontal)
        self.compare_slider.setObjectName("compare_slider")
        self.compare_slider.setValue(50)
        self.compare_slider.setRange(0, 1000)
        self.verticalLayout_8.addWidget(self.compare_slider)

        self.scrollArea_3 = QtWidgets.QScrollArea(self.slider_page)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        # self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents_3.setGeometry(
        #     QtCore.QRect(0, 0, 439, 52))
        # self.scrollAreaWidgetContents_3.setObjectName(
        #     "scrollAreaWidgetContents_3")
        self.slide_a_label = QtWidgets.QLabel()
        self.slide_a_label.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.slide_a_label.setObjectName("slide_a_label")
        self.slide_a_label.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        # self.slide_b_label = QtWidgets.QLabel(self.slider_stack)
        # self.slide_b_label.setGeometry(QtCore.QRect(0, 0, 0, 0))
        # self.slide_b_label.setObjectName("slide_b_label")
        self.scrollArea_3.setWidget(self.slide_a_label)
        self.verticalLayout_8.addWidget(self.scrollArea_3)
        self.horizontalLayout_13.addLayout(self.verticalLayout_8)
        self.function_stacked_page.addWidget(self.slider_page)
        self.difference_page = QtWidgets.QWidget()
        self.difference_page.setObjectName("difference_page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.difference_page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalFrame_3 = QtWidgets.QFrame(self.difference_page)
        self.horizontalFrame_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.horizontalFrame_3.setObjectName("horizontalFrame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem8 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.zoom_out_button = QtWidgets.QPushButton(self.horizontalFrame_3)
        self.zoom_out_button.setMinimumSize(QtCore.QSize(30, 0))
        self.zoom_out_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.zoom_out_button.setObjectName("zoom_out_button")
        self.horizontalLayout_3.addWidget(self.zoom_out_button)
        self.amplify_ratio_label = QtWidgets.QLabel(self.horizontalFrame_3)
        self.amplify_ratio_label.setObjectName("amplify_ratio_label")
        self.horizontalLayout_3.addWidget(self.amplify_ratio_label)
        self.zoom_in_button = QtWidgets.QPushButton(self.horizontalFrame_3)
        self.zoom_in_button.setMinimumSize(QtCore.QSize(30, 0))
        self.zoom_in_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.zoom_in_button.setObjectName("zoom_in_button")
        self.horizontalLayout_3.addWidget(self.zoom_in_button)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.reset_button = QtWidgets.QPushButton(self.horizontalFrame_3)
        self.reset_button.setObjectName("reset_button")
        self.horizontalLayout_5.addWidget(self.reset_button)
        self.similarity_label = QtWidgets.QLabel(self.horizontalFrame_3)
        self.similarity_label.setObjectName("similarity_label")
        self.horizontalLayout_5.addWidget(self.similarity_label)
        self.ratioSlider = QtWidgets.QSlider(self.horizontalFrame_3)
        self.ratioSlider.setMinimum(0)
        self.ratioSlider.setMaximum(100)
        self.ratioSlider.setSingleStep(1)
        self.ratioSlider.setProperty("value", 1)
        self.ratioSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ratioSlider.setObjectName("ratioSlider")
        self.horizontalLayout_5.addWidget(self.ratioSlider)
        self.ratio_lineEdit = QtWidgets.QLineEdit(self.horizontalFrame_3)
        self.ratio_lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ratio_lineEdit.setObjectName("ratio_lineEdit")
        self.horizontalLayout_5.addWidget(self.ratio_lineEdit)
        self.save_button = QtWidgets.QPushButton(self.horizontalFrame_3)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_5.addWidget(self.save_button)
        self.verticalLayout_5.addWidget(self.horizontalFrame_3)
        self.scrollArea = QtWidgets.QScrollArea(self.difference_page)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 457, 302))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.diff_label = QtWidgets.QLabel()
        self.diff_label.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.diff_label.setObjectName("diff_label")
        self.scrollArea.setWidget(self.diff_label)
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.function_stacked_page.addWidget(self.difference_page)
        self.file_details_page = QtWidgets.QWidget()
        self.file_details_page.setObjectName("file_details_page")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.file_details_page)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.file_a_label = QtWidgets.QLabel(self.file_details_page)

        self.file_a_label.setMinimumSize(QtCore.QSize(300, 300))
        self.file_a_label.setMaximumSize(QtCore.QSize(300, 300))
        self.file_a_label.setText("")
        self.file_a_label.setAlignment(QtCore.Qt.AlignCenter)
        self.file_a_label.setObjectName("file_a_label")
        self.verticalLayout_9.addWidget(
            self.file_a_label, 0, QtCore.Qt.AlignHCenter)
        self.scrollArea_4 = QtWidgets.QScrollArea(self.file_details_page)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        # self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents_5.setGeometry(
        #     QtCore.QRect(0, 0, 223, 52))
        # self.scrollAreaWidgetContents_5.setObjectName(
        #     "scrollAreaWidgetContents_5")
        self.file_a_info = QtWidgets.QLabel()
        self.file_a_info.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.file_a_info.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.file_a_info.setObjectName("")
        self.file_a_info.setFont(QtGui.QFont('Arial', 14))
        self.scrollArea_4.setWidget(self.file_a_info)
        self.verticalLayout_9.addWidget(self.scrollArea_4)
        self.horizontalLayout_8.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.file_b_label = QtWidgets.QLabel(self.file_details_page)
        self.file_b_label.setMinimumSize(QtCore.QSize(300, 300))
        self.file_b_label.setMaximumSize(QtCore.QSize(300, 300))
        self.file_b_label.setText("")
        self.file_b_label.setAlignment(QtCore.Qt.AlignCenter)
        self.file_b_label.setObjectName("file_b_label")
        self.verticalLayout_10.addWidget(self.file_b_label)
        self.scrollArea_5 = QtWidgets.QScrollArea(self.file_details_page)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        # self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents_6.setGeometry(
        #     QtCore.QRect(0, 0, 223, 52))
        # self.scrollAreaWidgetContents_6.setObjectName(
        #     "scrollAreaWidgetContents_6")
        self.file_b_info = QtWidgets.QLabel()
        self.file_b_info.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.file_b_info.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.file_b_info.setObjectName("")
        self.file_b_info.setFont(QtGui.QFont('Arial', 14))
        self.scrollArea_5.setWidget(self.file_b_info)
        self.verticalLayout_10.addWidget(self.scrollArea_5)
        self.horizontalLayout_8.addLayout(self.verticalLayout_10)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)
        self.function_stacked_page.addWidget(self.file_details_page)
        self.horizontalLayout_2.addWidget(self.function_stacked_page)
        self.verticalLayout_4.addWidget(self.horizontalFrame_5)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(180, 200, 35, 10))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.verticalFrame)
        self.verticalLayout_2.addWidget(self.horizontalFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.function_stacked_page.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Compare Tool"))
        self.pushButton.setText(_translate("MainWindow", "DiffChecker"))
        self.pushButton_2.setText(_translate("MainWindow", "Mask Compare"))
        self.slider_button.setText(_translate("MainWindow", "Slider"))
        self.difference_button.setText(_translate("MainWindow", "Difference"))
        self.file_details_button.setText(
            _translate("MainWindow", "File Details"))
        self.file_a_button.setText(_translate("MainWindow", "Original image📁"))
        self.file_b_button.setText(_translate("MainWindow", "Change image📁"))
        self.slider_zoom_out_button.setText(_translate("MainWindow", "-"))
        self.slider_amplify_button.setText(_translate("MainWindow", "100%"))
        self.slider_zoom_in_button.setText(_translate("MainWindow", "+"))
        self.pushButton_7.setText(_translate("MainWindow", "Reset"))
        self.zoom_out_button.setText(_translate("MainWindow", "-"))
        self.amplify_ratio_label.setText(_translate("MainWindow", "100%"))
        self.zoom_in_button.setText(_translate("MainWindow", "+"))
        self.reset_button.setText(_translate("MainWindow", "Reset"))
        self.similarity_label.setText(_translate("MainWindow", "Similarity: "))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.diff_label.setText(_translate("MainWindow", ""))
        self.file_a_info.setText(_translate("MainWindow", ""))
        self.file_b_info.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", "施工中"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
