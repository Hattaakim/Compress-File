# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowWWDkdB.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QFrame, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(570, 680)
        MainWindow.setMinimumSize(QSize(570, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_23 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_12.addWidget(self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.label_2)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.stepOneNumber = QPushButton(self.centralwidget)
        self.stepOneNumber.setObjectName(u"stepOneNumber")
        self.stepOneNumber.setMinimumSize(QSize(50, 50))
        self.stepOneNumber.setMaximumSize(QSize(50, 50))
        self.stepOneNumber.setFont(font)
        self.stepOneNumber.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 177, 255), stop:1 rgba(255, 116, 255, 255)); border-radius: 25px\n"
"")
        self.stepOneNumber.setFlat(False)

        self.horizontalLayout.addWidget(self.stepOneNumber)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.stepOneTitle = QPushButton(self.centralwidget)
        self.stepOneTitle.setObjectName(u"stepOneTitle")
        self.stepOneTitle.setFlat(True)

        self.verticalLayout.addWidget(self.stepOneTitle)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.stepTwoNumber = QPushButton(self.centralwidget)
        self.stepTwoNumber.setObjectName(u"stepTwoNumber")
        self.stepTwoNumber.setMinimumSize(QSize(50, 50))
        self.stepTwoNumber.setMaximumSize(QSize(50, 50))
        self.stepTwoNumber.setFont(font)
        self.stepTwoNumber.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 177, 255), stop:1 rgba(255, 116, 255, 255)); border-radius: 25px\n"
"")
        self.stepTwoNumber.setFlat(False)

        self.horizontalLayout_2.addWidget(self.stepTwoNumber)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.stepTwoTitle = QPushButton(self.centralwidget)
        self.stepTwoTitle.setObjectName(u"stepTwoTitle")
        self.stepTwoTitle.setFlat(True)

        self.verticalLayout_2.addWidget(self.stepTwoTitle)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.stepThreeNumber = QPushButton(self.centralwidget)
        self.stepThreeNumber.setObjectName(u"stepThreeNumber")
        self.stepThreeNumber.setMinimumSize(QSize(50, 50))
        self.stepThreeNumber.setMaximumSize(QSize(50, 50))
        self.stepThreeNumber.setFont(font)
        self.stepThreeNumber.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 177, 255), stop:1 rgba(255, 116, 255, 255)); border-radius: 25px\n"
"")
        self.stepThreeNumber.setFlat(False)

        self.horizontalLayout_3.addWidget(self.stepThreeNumber)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.stepThreeTitle = QPushButton(self.centralwidget)
        self.stepThreeTitle.setObjectName(u"stepThreeTitle")
        self.stepThreeTitle.setFlat(True)

        self.verticalLayout_3.addWidget(self.stepThreeTitle)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.stepFourNumber = QPushButton(self.centralwidget)
        self.stepFourNumber.setObjectName(u"stepFourNumber")
        self.stepFourNumber.setMinimumSize(QSize(50, 50))
        self.stepFourNumber.setMaximumSize(QSize(50, 50))
        self.stepFourNumber.setFont(font)
        self.stepFourNumber.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 177, 255), stop:1 rgba(255, 116, 255, 255)); border-radius: 25px\n"
"")
        self.stepFourNumber.setFlat(False)

        self.horizontalLayout_4.addWidget(self.stepFourNumber)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.stepFourTitle = QPushButton(self.centralwidget)
        self.stepFourTitle.setObjectName(u"stepFourTitle")
        self.stepFourTitle.setFlat(True)

        self.verticalLayout_4.addWidget(self.stepFourTitle)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_12.addLayout(self.horizontalLayout_5)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_4)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_10 = QVBoxLayout(self.page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.menu1ScrollArea = QScrollArea(self.page)
        self.menu1ScrollArea.setObjectName(u"menu1ScrollArea")
        self.menu1ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 306, 319))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.opsiFolder = QRadioButton(self.scrollAreaWidgetContents)
        self.opsiFolder.setObjectName(u"opsiFolder")

        self.verticalLayout_6.addWidget(self.opsiFolder)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.folderBerisiFile = QLineEdit(self.groupBox)
        self.folderBerisiFile.setObjectName(u"folderBerisiFile")

        self.horizontalLayout_6.addWidget(self.folderBerisiFile)

        self.pilihFolderFile = QPushButton(self.groupBox)
        self.pilihFolderFile.setObjectName(u"pilihFolderFile")

        self.horizontalLayout_6.addWidget(self.pilihFolderFile)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_6.addWidget(self.line)

        self.opsiFile = QRadioButton(self.scrollAreaWidgetContents)
        self.opsiFile.setObjectName(u"opsiFile")

        self.verticalLayout_6.addWidget(self.opsiFile)

        self.fileTable = QTableView(self.scrollAreaWidgetContents)
        self.fileTable.setObjectName(u"fileTable")

        self.verticalLayout_6.addWidget(self.fileTable)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tambahFile = QPushButton(self.scrollAreaWidgetContents)
        self.tambahFile.setObjectName(u"tambahFile")

        self.horizontalLayout_7.addWidget(self.tambahFile)

        self.hapusFile = QPushButton(self.scrollAreaWidgetContents)
        self.hapusFile.setObjectName(u"hapusFile")

        self.horizontalLayout_7.addWidget(self.hapusFile)

        self.resetTable = QPushButton(self.scrollAreaWidgetContents)
        self.resetTable.setObjectName(u"resetTable")

        self.horizontalLayout_7.addWidget(self.resetTable)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Shadow.Plain)
        self.line_2.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_6.addWidget(self.line_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.pageOneLanjut = QPushButton(self.scrollAreaWidgetContents)
        self.pageOneLanjut.setObjectName(u"pageOneLanjut")

        self.horizontalLayout_8.addWidget(self.pageOneLanjut)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.menu1ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.menu1ScrollArea)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_11 = QVBoxLayout(self.page_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scrollArea = QScrollArea(self.page_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -91, 516, 547))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_3)

        self.startVerify = QPushButton(self.scrollAreaWidgetContents_2)
        self.startVerify.setObjectName(u"startVerify")

        self.verticalLayout_8.addWidget(self.startVerify)

        self.line_8 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShadow(QFrame.Shadow.Plain)
        self.line_8.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_8.addWidget(self.line_8)

        self.tabelVerifikasi = QTableView(self.scrollAreaWidgetContents_2)
        self.tabelVerifikasi.setObjectName(u"tabelVerifikasi")

        self.verticalLayout_8.addWidget(self.tabelVerifikasi)

        self.fileVerifyProgress = QLabel(self.scrollAreaWidgetContents_2)
        self.fileVerifyProgress.setObjectName(u"fileVerifyProgress")
        font2 = QFont()
        font2.setPointSize(12)
        self.fileVerifyProgress.setFont(font2)
        self.fileVerifyProgress.setStyleSheet(u"color: rgb(94, 92, 100) ")

        self.verticalLayout_8.addWidget(self.fileVerifyProgress)

        self.line_10 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShadow(QFrame.Shadow.Plain)
        self.line_10.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_8.addWidget(self.line_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)

        self.pageTwoLanjut = QPushButton(self.scrollAreaWidgetContents_2)
        self.pageTwoLanjut.setObjectName(u"pageTwoLanjut")

        self.horizontalLayout_9.addWidget(self.pageTwoLanjut)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_11.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_19 = QVBoxLayout(self.page_3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.scrollArea_2 = QScrollArea(self.page_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 530, 456))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_8)

        self.line_5 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.imgMpx = QComboBox(self.groupBox_2)
        self.imgMpx.addItem("")
        self.imgMpx.addItem("")
        self.imgMpx.addItem("")
        self.imgMpx.addItem("")
        self.imgMpx.addItem("")
        self.imgMpx.setObjectName(u"imgMpx")

        self.verticalLayout_17.addWidget(self.imgMpx)


        self.horizontalLayout_10.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_24 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.imgCompress = QSpinBox(self.groupBox_4)
        self.imgCompress.setObjectName(u"imgCompress")
        self.imgCompress.setMinimum(1)
        self.imgCompress.setMaximum(100)
        self.imgCompress.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.imgCompress.setValue(85)

        self.verticalLayout_24.addWidget(self.imgCompress)


        self.horizontalLayout_10.addWidget(self.groupBox_4)


        self.verticalLayout_13.addLayout(self.horizontalLayout_10)

        self.compressionTips = QLabel(self.scrollAreaWidgetContents_3)
        self.compressionTips.setObjectName(u"compressionTips")
        font3 = QFont()
        font3.setFamilies([u"Ubuntu"])
        font3.setPointSize(10)
        font3.setWeight(QFont.Thin)
        self.compressionTips.setFont(font3)

        self.verticalLayout_13.addWidget(self.compressionTips)

        self.line_6 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_6)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.dirTujuan = QLineEdit(self.groupBox_3)
        self.dirTujuan.setObjectName(u"dirTujuan")

        self.horizontalLayout_11.addWidget(self.dirTujuan)

        self.pilihFolder = QPushButton(self.groupBox_3)
        self.pilihFolder.setObjectName(u"pilihFolder")

        self.horizontalLayout_11.addWidget(self.pilihFolder)


        self.verticalLayout_13.addWidget(self.groupBox_3)

        self.hapusFIleAsli = QCheckBox(self.scrollAreaWidgetContents_3)
        self.hapusFIleAsli.setObjectName(u"hapusFIleAsli")

        self.verticalLayout_13.addWidget(self.hapusFIleAsli)

        self.line_9 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_9)

        self.dataSummary = QLabel(self.scrollAreaWidgetContents_3)
        self.dataSummary.setObjectName(u"dataSummary")
        self.dataSummary.setFont(font3)

        self.verticalLayout_13.addWidget(self.dataSummary)

        self.line_11 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_11)

        self.pageThreeNext = QPushButton(self.scrollAreaWidgetContents_3)
        self.pageThreeNext.setObjectName(u"pageThreeNext")

        self.horizontalLayout_12.addWidget(self.pageThreeNext)


        self.verticalLayout_13.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)


        self.verticalLayout_18.addLayout(self.verticalLayout_13)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_19.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_22 = QVBoxLayout(self.page_4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.scrollArea_3 = QScrollArea(self.page_4)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, -145, 516, 601))
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.label_9)

        self.line_7 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_14.addWidget(self.line_7)

        self.startCompression = QPushButton(self.scrollAreaWidgetContents_4)
        self.startCompression.setObjectName(u"startCompression")

        self.verticalLayout_14.addWidget(self.startCompression)

        self.fileCompressionTable = QTableView(self.scrollAreaWidgetContents_4)
        self.fileCompressionTable.setObjectName(u"fileCompressionTable")

        self.verticalLayout_14.addWidget(self.fileCompressionTable)

        self.fileCompressionProgress = QLabel(self.scrollAreaWidgetContents_4)
        self.fileCompressionProgress.setObjectName(u"fileCompressionProgress")
        self.fileCompressionProgress.setFont(font2)
        self.fileCompressionProgress.setStyleSheet(u"color: rgb(94, 92, 100) ")

        self.verticalLayout_14.addWidget(self.fileCompressionProgress)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)


        self.verticalLayout_21.addLayout(self.verticalLayout_14)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_22.addWidget(self.scrollArea_3)

        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_12.addWidget(self.stackedWidget)


        self.verticalLayout_23.addLayout(self.verticalLayout_12)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.imgMpx.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Compress Image", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">Aplikasi yang digunakan untuk mengompresi berkas foto dengan ukuran besar menjadi ukuran kecil, tanpa menurunkan kualitasnya secara signifikan</p></body></html>", None))
        self.stepOneNumber.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.stepOneTitle.setText(QCoreApplication.translate("MainWindow", u"Pilih Folder/File", None))
        self.stepTwoNumber.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.stepTwoTitle.setText(QCoreApplication.translate("MainWindow", u"Verifikasi Sistem", None))
        self.stepThreeNumber.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.stepThreeTitle.setText(QCoreApplication.translate("MainWindow", u"Opsi Kompresi", None))
        self.stepFourNumber.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.stepFourTitle.setText(QCoreApplication.translate("MainWindow", u"Proses dan Hasil", None))
        self.opsiFolder.setText(QCoreApplication.translate("MainWindow", u"Gunakan Folder berisi File", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Direktori Folder (Otomatis)", None))
        self.folderBerisiFile.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Klik pilih folder untuk melanjutkan!", None))
        self.pilihFolderFile.setText(QCoreApplication.translate("MainWindow", u"Pilih Folder", None))
        self.opsiFile.setText(QCoreApplication.translate("MainWindow", u"Pilih File (Mendukung Drag and Drop)", None))
        self.tambahFile.setText(QCoreApplication.translate("MainWindow", u"Tambah File", None))
        self.hapusFile.setText(QCoreApplication.translate("MainWindow", u"Hapus File", None))
        self.resetTable.setText(QCoreApplication.translate("MainWindow", u"Reset Tabel", None))
        self.pageOneLanjut.setText(QCoreApplication.translate("MainWindow", u"Lanjut", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu Sans';\">Sistem akan melakukan verifikasi data untuk setiap file yang Anda masukkan demi kelancaran proses selanjutnya. Anda harus memperhatikan notasi pada 3 kolom untuk mengetahui lulus/tidaknya file yang ingin dikompresi dari proses verifikasi. 3 kolom yang dimaksud adalah [File Didukung] [Integritas File] dan [File Aman], dengan notasi:<br />&q"
                        "uot;!&quot; -&gt; Proses verifikasi dilewatkan karena file rusak atau mengandung virus<br />&quot;</span><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Avenir Next','Avenir','Helvetica','sans-serif'; font-size:14px\">\u2717&quot; </span><span style=\" font-family:'Ubuntu Sans';\">-&gt; File tidak didukung, rusak, ataupun terdeteksi mengandung virus<br />&quot;</span><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Avenir Next','Avenir','Helvetica','sans-serif'; font-size:14px;\">\u2714&quot; </span><span style=\" font-family:'Ubuntu Sans';\">-&gt; File siap untuk diproses<br />&quot;?&quot; -&gt; Notasi khusus ketika terjadinya kesalahan pada sistem pengecekan<br /><br />Silahkan mulai proses verifikasi dengan menekan tombol dibawah ini:<br /></span></p></body></html>", None))
        self.startVerify.setText(QCoreApplication.translate("MainWindow", u"Mulai Verifikasi", None))
        self.fileVerifyProgress.setText(QCoreApplication.translate("MainWindow", u"n/n File Diproses", None))
        self.pageTwoLanjut.setText(QCoreApplication.translate("MainWindow", u"Lanjutkan", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">Sebagai referensi, Google Foto menetapkan kompresi 12Mp bagi gambar yang Anda unggah untuk menghemat penyimpanan Anda. Anda direkomendasikan untuk memilih pengaturan dengan tingkat Megapiksel <span style=\" font-weight:700;\">12Mp</span> dan Kualitas Gambar <span style=\" font-weight:700;\">85%</span> agar kualitas dari gambar Anda tidak menurun secara drastis.</p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Megapiksel Gambar", None))
        self.imgMpx.setItemText(0, QCoreApplication.translate("MainWindow", u"20Mp", None))
        self.imgMpx.setItemText(1, QCoreApplication.translate("MainWindow", u"12Mp", None))
        self.imgMpx.setItemText(2, QCoreApplication.translate("MainWindow", u"10Mp", None))
        self.imgMpx.setItemText(3, QCoreApplication.translate("MainWindow", u"8Mp", None))
        self.imgMpx.setItemText(4, QCoreApplication.translate("MainWindow", u"6Mp", None))

        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Kualitas Gambar", None))
        self.imgCompress.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.compressionTips.setText(QCoreApplication.translate("MainWindow", u"Saran: Semua terlihat baik!", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Lokasi Penyimpanan File", None))
        self.dirTujuan.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Klik pilih folder untuk memilih lokasi", None))
        self.pilihFolder.setText(QCoreApplication.translate("MainWindow", u"Pilih Folder", None))
        self.hapusFIleAsli.setText(QCoreApplication.translate("MainWindow", u"Hapus File Asli (Tidak Direkomendasikan)", None))
        self.dataSummary.setText(QCoreApplication.translate("MainWindow", u"Ringkasan Kompresi:", None))
        self.pageThreeNext.setText(QCoreApplication.translate("MainWindow", u"Lanjut", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">Kompresi tidak berjalan secara otomatis. Anda menjalankannya secara manual menekan tombol Mulai. Waktu yang digunakan untuk proses kompresi tergantung dari seberapa cepat dan banyaknya utas pada prosesor perangkat Anda. Silahkan tunggu proses kompresi hingga selesai. Tabel di bawah ini akan menunjukkan proses waktu nyata ketika kompresi sedang berlangsung. </p><p align=\"justify\"><span style=\" font-weight:700;\">Kepala Tabel:</span><br/>[Size Akhir] -&gt; Menunjukkan ukuran foto setelah dikompresi<br/>[Dihemat] -&gt; Taraf penghematan ukuran oleh algoritma kompresi<br/>[Status] -&gt; Progres kompresi (<span style=\" font-weight:700;\">Parameter Simbol</span><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Avenir Next','Avenir','Helvetica','sans-serif';\">)</span><br/>[Disimpan Di] -&gt; Lokasi penyimpanan untuk setiap foto hasil kompresi<br/>[Di Hapus] -&gt; Berlaku saat Hapus File Asli menyala (<span style=\" font-weight:700;\">Parameter Simbol)<br/><b"
                        "r/>Parameter Simbol: </span><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Avenir Next','Avenir','Helvetica','sans-serif';\">\u2714 = Sukses | \u2717 = Gagal | - = Tidak Dimulai</span></p></body></html>", None))
        self.startCompression.setText(QCoreApplication.translate("MainWindow", u"Mulai", None))
        self.fileCompressionProgress.setText(QCoreApplication.translate("MainWindow", u"Kompresi belum dimulai. Sistem sudah siap!", None))
    # retranslateUi

