from PyQt5 import QtCore, QtGui, QtWidgets ,QtPrintSupport
from PyQt5.QtGui import QIcon,QPixmap
from pyqtgraph import PlotWidget
from scipy.io import wavfile
from scipy.fft import rfft, rfftfreq,fft, fftfreq,ifft
import os
import matplotlib.pyplot as plt
import numpy as np
import scipy
import wave
import math
import contextlib
from PyQt5.QtWidgets import QFileDialog , QLabel
import pyqtgraph as pg
import sys
import sounddevice as sd
from matplotlib.backends.backend_pdf import PdfPages
from operator import add, sub


zoomIn_scale=0.5
zoomOut_scale=2

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.children = []
        self.ui.actionNew.triggered.connect(self.show_child)
    def show_child(self):
        child = ApplicationWindow()
        child.show()
        self.children.append(child)


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1225, 907)
        MainWindow.setStyleSheet("background-color: #FFFFFF")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 591, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = PlotWidget(self.verticalLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setBackground('w')
        self.verticalLayout.addWidget(self.graphicsView)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(610, 310, 601, 281))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        # self.graphicsView_3 = PlotWidget(self.verticalLayoutWidget_4)
        # self.graphicsView_3.setObjectName("graphicsView_3")
        # self.graphicsView.setStyleSheet("background-color: White")
        #self.graphicsView_3.setBackground('w')
        #self.verticalLayout_4.addWidget(self.graphicsView_3)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 310, 591, 281))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.graphicsView_2 = PlotWidget(self.verticalLayoutWidget_3)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_2.setBackground('w')
        self.verticalLayout_3.addWidget(self.graphicsView_2)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(610, 150, 601, 400))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 620, 1191, 201))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.slider1 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.slider1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.slider1.setMinimum(0)
        self.slider1.setMaximum(5)
        self.slider1.setSliderPosition(1)
        self.slider1.setOrientation(QtCore.Qt.Vertical)
        self.slider1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider1.setObjectName("slider1")
        self.horizontalLayout.addWidget(self.slider1)
        

        # ----------------------

        self.slider2 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.slider2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.slider2.setMinimum(0)
        self.slider2.setMaximum(5)
        self.slider2.setSliderPosition(1)
        self.slider2.setOrientation(QtCore.Qt.Vertical)
        self.slider2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider2.setObjectName("slider2")
        self.horizontalLayout.addWidget(self.slider2)


        self.slider3 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.slider3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.slider3.setMinimum(0)
        self.slider3.setMaximum(5)
        self.slider3.setSliderPosition(1)
        self.slider3.setOrientation(QtCore.Qt.Vertical)
        self.slider3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider3.setObjectName("slider3")
        self.horizontalLayout.addWidget(self.slider3)

        self.slider4 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.slider4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.slider4.setMinimum(0)
        self.slider4.setMaximum(5)
        self.slider4.setSliderPosition(1)
        self.slider4.setOrientation(QtCore.Qt.Vertical)
        self.slider4.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider4.setObjectName("slider4")
        self.horizontalLayout.addWidget(self.slider4)
        

        self.slider5 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.slider5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.slider5.setMinimum(0)
        self.slider5.setMaximum(5)
        self.slider5.setSliderPosition(1)
        self.slider5.setOrientation(QtCore.Qt.Vertical)
        self.slider5.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider5.setObjectName("slider5")
        self.horizontalLayout.addWidget(self.slider5)
        

        self.slider6 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.slider6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.slider6.setMinimum(0)
        self.slider6.setMaximum(5)
        self.slider6.setSliderPosition(1)
        self.slider6.setOrientation(QtCore.Qt.Vertical)
        self.slider6.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider6.setObjectName("slider6")
        self.horizontalLayout.addWidget(self.slider6)
        

        self.slider7 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.slider7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.slider7.setMinimum(0)
        self.slider7.setMaximum(5)
        self.slider7.setSliderPosition(1)
        self.slider7.setOrientation(QtCore.Qt.Vertical)
        self.slider7.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider7.setObjectName("slider7")
        self.horizontalLayout.addWidget(self.slider7)
        

        self.slider8 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.slider8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.slider8.setMinimum(0)
        self.slider8.setMaximum(5)
        self.slider8.setSliderPosition(1)
        self.slider8.setOrientation(QtCore.Qt.Vertical)
        self.slider8.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider8.setObjectName("slider8")
        self.horizontalLayout.addWidget(self.slider8)
        

        self.slider9 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.slider9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.slider9.setMinimum(0)
        self.slider9.setMaximum(5)
        self.slider9.setSliderPosition(1)
        self.slider9.setOrientation(QtCore.Qt.Vertical)
        self.slider9.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider9.setObjectName("slider9")
        self.horizontalLayout.addWidget(self.slider9)
        

        self.slider10 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.slider10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.slider10.setMinimum(0)
        self.slider10.setMaximum(5)
        self.slider10.setSliderPosition(1)
        self.slider10.setOrientation(QtCore.Qt.Vertical)
        self.slider10.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider10.setObjectName("slider10")
        self.horizontalLayout.addWidget(self.slider10)


        self.min_slider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.min_slider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.min_slider.setMinimum(0)
        self.min_slider.setMaximum(100)
        self.min_slider.setOrientation(QtCore.Qt.Vertical)
        self.min_slider.setObjectName("min_slider")
        self.horizontalLayout.addWidget(self.min_slider)


        self.max_slider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.max_slider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.max_slider.setValue(100)
        self.max_slider.setMinimum(0)
        self.max_slider.setMaximum(100)
        self.max_slider.setOrientation(QtCore.Qt.Vertical)
        self.max_slider.setObjectName("max_slider")
        self.horizontalLayout.addWidget(self.max_slider)
        
        self.yf=[]
        self.time=[]
        self.data=[]
        self.new=[]
  
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1238, 26))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet("background-color: White")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen_signal = QtWidgets.QMenu(self.menuFile)
        self.menuOpen_signal.setObjectName("menuOpen_signal")
        self.menuPlay_Navigate = QtWidgets.QMenu(self.menubar)
        self.menuPlay_Navigate.setObjectName("menuPlay_Navigate")
        self.menu3D_Tools = QtWidgets.QMenu(self.menubar)
        self.menu3D_Tools.setObjectName("menu3D_Tools")
        self.menuSpectrogram = QtWidgets.QMenu(self.menu3D_Tools)
        self.menuSpectrogram.setObjectName("menuSpectrogram")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        self.toolBar.setStyleSheet("background-color: White")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        
        self.actionleft = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionleft.setIcon(icon6)
        self.actionright = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()

        icon7.addPixmap(QtGui.QPixmap("right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionright.setIcon(icon7)
        self.actionup = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("speedup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionup.setIcon(icon8)
        self.actiondown = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("speedddown.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiondown.setIcon(icon9)
        self.actionopensignal = QtWidgets.QAction(MainWindow)
        self.actionopensignal.setObjectName("actionopensignal")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionPlay_Soundbefore = QtWidgets.QAction(MainWindow)
        self.actionPlay_Soundbefore.setObjectName("actionPlay_Soundbefore")
        self.actionPlay_Soundafter = QtWidgets.QAction(MainWindow)
        self.actionPlay_Soundafter.setObjectName("actionPlay_Soundafter")
        self.actionStop_Sound = QtWidgets.QAction(MainWindow)
        self.actionStop_Sound.setObjectName("actionStop_Sound")
        self.actionzoomIn = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("zoomin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("zoom.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionzoomIn.setIcon(icon)
        self.actionzoomIn.setObjectName("actionzoomIn")
        self.actionplay = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("plau.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("play.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionplay.setIcon(icon1)
        self.actionplay.setObjectName("actionplay")
        self.actionstop = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pause.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("pause.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionstop.setIcon(icon2)
        self.actionstop.setObjectName("actionstop")
        self.actionopen_signal = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("open.jfif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("open.jfif"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionopen_signal.setIcon(icon3)
        self.actionopen_signal.setObjectName("actionopen_signal")
        self.actionzoomOut = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("zoomout.png"), QtGui.QIcon.Normal, QtGui.QIcon.On) 
        self.actionzoomOut.setIcon(icon4)
        self.actionzoomOut.setObjectName("actionzoomOut")
        self.actionspect = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("spec.jfif"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionspect.setIcon(icon5)
        self.actionspect.setObjectName("actionspect")
        self.actionChannel_1 = QtWidgets.QAction(MainWindow)
        self.actionChannel_1.setObjectName("actionChannel_1")
        self.actionChannel_4 = QtWidgets.QAction(MainWindow)
        self.actionChannel_4.setObjectName("actionChannel_4")
        self.actionChannel_5 = QtWidgets.QAction(MainWindow)
        self.actionChannel_5.setObjectName("actionChannel_5")
        self.actionChannel_2 = QtWidgets.QAction(MainWindow)
        self.actionChannel_2.setObjectName("actionChannel_2")
        self.actionChannel_3 = QtWidgets.QAction(MainWindow)
        self.actionChannel_3.setObjectName("actionChannel_3")
        self.menuFile.addAction(self.actionopensignal)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave_As)
        self.menuPlay_Navigate.addAction(self.actionPlay_Soundbefore)
        self.menuPlay_Navigate.addAction(self.actionPlay_Soundafter)
        self.menuPlay_Navigate.addAction(self.actionStop_Sound)
        self.menuSpectrogram.addAction(self.actionChannel_1)
        self.menuSpectrogram.addAction(self.actionChannel_4)
        self.menuSpectrogram.addAction(self.actionChannel_5)
        self.menuSpectrogram.addAction(self.actionChannel_2)
        self.menuSpectrogram.addAction(self.actionChannel_3)
        self.menu3D_Tools.addAction(self.menuSpectrogram.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPlay_Navigate.menuAction())
        self.menubar.addAction(self.menu3D_Tools.menuAction())
        self.toolBar.addAction(self.actionopen_signal)
        self.toolBar.addAction(self.actionplay)
        self.toolBar.addAction(self.actionstop)
        self.toolBar.addAction(self.actionzoomIn)
        self.toolBar.addAction(self.actionzoomOut)
        self.toolBar.addAction(self.actionspect)
        self.toolBar.addAction(self.actionleft)
        self.toolBar.addAction(self.actionright)
        self.toolBar.addAction(self.actionup)
        self.toolBar.addAction(self.actiondown)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionplay.triggered.connect(lambda:self.play())
        self.actionstop.triggered.connect(lambda:self.pause_btn())
        self.actionopensignal.triggered.connect(self.open)
        self.actionopen_signal.triggered.connect(self.open)
        self.actionzoomIn.triggered.connect(lambda:self.zoom(zoomIn_scale))
        self.actionzoomOut.triggered.connect(lambda:self.zoom(zoomOut_scale))
        self.actionspect.triggered.connect(lambda:self.spectrogram())
        self.actionNew.triggered.connect(self.show_child)
        self.actionPlay_Soundbefore.triggered.connect(self.play_soundbefore)
        self.actionPlay_Soundafter.triggered.connect(self.play_soundafter)
        self.actionStop_Sound.triggered.connect(self.stop_sound)
        self.actionSave_As.triggered.connect(lambda:self.Save_As_Pdf())
        self.actionleft.triggered.connect(lambda: self.scroll(add))
        self.actionright.triggered.connect(lambda: self.scroll(sub))
        self.actionup.triggered.connect(self.SpeedUp)
        self.actiondown.triggered.connect(self.SpeedDown)

        
        self.actionChannel_1.triggered.connect(lambda: self.palette(1))
        self.actionChannel_4.triggered.connect(lambda: self.palette(2))
        self.actionChannel_5.triggered.connect(lambda: self.palette(3))
        self.actionChannel_2.triggered.connect(lambda: self.palette(4))
        self.actionChannel_3.triggered.connect(lambda: self.palette(5))

        self.xmax_scale=10
        self.xmin_scale=0
        self.pen2=pg.mkPen((0,0,255))
        self.widgets=[self.graphicsView,self.graphicsView_2]
        self.data=[]

        self.sliders=[self.slider1,self.slider2,
        self.slider3,self.slider4,self.slider5,self.slider6,self.slider7,self.slider8,self.slider9,self.slider10]
           
        for i in range(10):
            self.sliders[i].valueChanged.connect(lambda: self.gain(i))

    
        self.min_slider.valueChanged.connect(lambda: self.specslider())
        self.max_slider.valueChanged.connect(lambda: self.specslider())
        
        self.cmap=None
        self.speed=1000
        self.specdata=[]
        
    
    def show_child(self):
        child = Ui_MainWindow()
        child.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuPlay_Navigate.setTitle(_translate("MainWindow", "Play"))
        self.menu3D_Tools.setTitle(_translate("MainWindow", "3D Tools"))
        self.menuSpectrogram.setTitle(_translate("MainWindow", "Spectrogram"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionopensignal.setText(_translate("MainWindow", "Open Signal"))
        self.actionopensignal.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As PDF"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionPlay_Soundbefore.setText(_translate("MainWindow", "Play Original Sound"))
        self.actionPlay_Soundbefore.setShortcut(_translate("MainWindow", "Ctrl+b"))
        self.actionPlay_Soundafter.setText(_translate("MainWindow", "Play Edited Sound"))
        self.actionPlay_Soundafter.setShortcut(_translate("MainWindow", "Ctrl+f"))
        self.actionStop_Sound.setText(_translate("MainWindow", "Stop"))
        self.actionStop_Sound.setShortcut(_translate("MainWindow", "Ctrl+t"))
        self.actionChannel_1.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.actionChannel_4.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.actionChannel_5.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.actionChannel_2.setShortcut(_translate("MainWindow", "Ctrl+4"))
        self.actionChannel_3.setShortcut(_translate("MainWindow", "Ctrl+5"))
        self.actionzoomIn.setText(_translate("MainWindow", "zoomIn"))
        self.actionzoomIn.setToolTip(_translate("MainWindow", "zoomIn"))
        self.actionzoomIn.setShortcut(_translate("MainWindow", "Ctrl++"))
        self.actionzoomOut.setText(_translate("MainWindow", "zoomOut"))
        self.actionzoomOut.setToolTip(_translate("MainWindow", "zoomOut"))
        self.actionzoomOut.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.actionplay.setText(_translate("MainWindow", "play"))
        self.actionplay.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionstop.setText(_translate("MainWindow", "stop"))
        self.actionstop.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionopen_signal.setText(_translate("MainWindow", "open_signal"))
        self.actionzoomOut.setText(_translate("MainWindow", "zoomOut"))
        self.actionzoomOut.setToolTip(_translate("MainWindow", "zoomOut"))
        self.actionspect.setText(_translate("MainWindow", "spect"))
        self.actionspect.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionleft.setToolTip(_translate("MainWindow", "Scroll_Left"))
        self.actionleft.setText(_translate("MainWindow", "Scroll_Left"))
        self.actionleft.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionright.setToolTip(_translate("MainWindow", "Scroll_Right"))
        self.actionright.setText(_translate("MainWindow", "Scroll_Right"))
        self.actionright.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionup.setToolTip(_translate("MainWindow", "Speed Up"))
        self.actionup.setText(_translate("MainWindow", "Speed Up"))
        self.actionup.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actiondown.setToolTip(_translate("MainWindow", "Speed Down"))
        self.actiondown.setText(_translate("MainWindow", "Speed Down"))
        self.actiondown.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionChannel_1.setText(_translate("MainWindow", "Palette 1"))
        self.actionChannel_4.setText(_translate("MainWindow", "Palette 2"))
        self.actionChannel_5.setText(_translate("MainWindow", "Palette 3"))
        self.actionChannel_2.setText(_translate("MainWindow", "Palette 4"))
        self.actionChannel_3.setText(_translate("MainWindow", "Palette 5"))

    def open(self):
        options = QFileDialog.Options()
        self.filename, _ = QFileDialog.getOpenFileName(None,"Open File","*.WAV", options=options)
        with contextlib.closing(wave.open(self.filename,'r')) as f:
            self.frames = f.getnframes()
            self.rate = f.getframerate()
            duration = self.frames / float(self.rate)
        self.samplingfrequency,self.signalData=wavfile.read(self.filename)
        self.array=np.asarray(self.signalData)
        if len(self.array.shape) == 2:
            for i in range(len(self.signalData)):
                self.data.append(self.signalData[i][0])
        else:
            for i in range(len(self.signalData)):
                self.data.append(self.signalData[i])
        self.time = np.arange(0,duration,1/self.samplingfrequency)
        self.widgets[0].plot(self.time,self.data,pen=self.pen2)
        self.widgets[0].setXRange(self.xmin_scale,self.xmax_scale)
        self.widgets[1].plot(self.time,self.data,pen=self.pen2)
        self.widgets[1].setXRange(self.xmin_scale,self.xmax_scale)
        self.x_range=self.widgets[0].getViewBox().state['viewRange'][0]
        self.widgets[0].setYRange(min(self.data),max(self.data))
        self.bands()
        self.specdata = self.data
        self.fft(self.data)
        self.minvalue=0
        self.maxvalue=self.freq_max
        self.spectrogram()

    def play_soundbefore(self):
        sd.play(self.data, blocking=False)
    
    def play_soundafter(self):
        sd.play(np.real(self.yt), blocking=False)

    def stop_sound(self):
        sd.stop()

    def fft(self,signal):
        self.yf = fft(signal)
        self.xf =fftfreq(self.frames, 1/self.samplingfrequency) 
        self.freq_max=max(self.xf)
        # self.widgets[2].clear()  
        # self.widgets[2].plot(self.xf,np.abs(self.yf),pen=self.pen2) 
        # self.widgets[2].setYRange(0,max(np.abs(self.yf)))
        
    def recover_signal(self):
        self.yt=ifft(np.multiply(np.array(self.after_rq),np.exp(1j*self.phase)))
        print(len(self.yt))
        self.widgets[1].clear()
        self.widgets[1].plot(self.time,np.real(self.yt),pen=self.pen2)
        self.widgets[1].setXRange(self.x_range[0],self.x_range[1])
        self.widgets[1].setYRange(min(np.real(self.yt)),max(np.real(self.yt)))
        scipy.io.wavfile.write("processed.wav",self.rate,np.real(self.yt))
       
    def spectrogram(self):
            plt.clf()
            plt.specgram(self.specdata,NFFT=len(self.specdata),Fs=self.samplingfrequency ,detrend='mean', mode='psd',cmap=self.cmap)
            plt.ylim(self.minvalue,self.maxvalue)
            plt.colorbar()
            plt.savefig('image.png')
            self.pixmap= QPixmap('image.png')
            self.pixmap1=self.pixmap.scaled(600,300)
            self.label = QLabel()
            self.label.setPixmap(self.pixmap1)
            self.label.setFixedSize(600,300)
            self.verticalLayout_6.addWidget(self.label)
            self.verticalLayout_6.removeWidget(self.label)
    
    def specslider(self):
        self.minvalue= (float(self.min_slider.value())/100)*self.freq_max
        self.maxvalue= (float(self.max_slider.value())/100)*self.freq_max
        self.new.clear()
        for x in range(len(self.xf)):
            if (self.xf[x] > self.minvalue) and (self.xf[x] < self.maxvalue):
                self.new.append(self.yf[x])
            else:
                self.new.append(0)
        self.newphase=np.angle(self.new)
        self.specdata=np.real(ifft(np.multiply(np.array(self.new),np.exp(1j*self.newphase))))
        self.spectrogram()

    def bands(self):
        self.bands_list=[]
        self.yf2=fft(self.data)
        self.mag=np.abs(self.yf2)
        self.phase=np.angle(self.yf2)
        BW=math.ceil(len(self.yf2)/10)

        for i in range(10):
            self.bands_list.append(self.mag[i*BW:(i+1)*BW])
        self.eq_bands=self.bands_list.copy()
    def gain(self,i):
        self.after_rq=[]
        for i in range(10):
                self.eq_bands[i]=self.bands_list[i]*self.sliders[i].value()
                #self.eq_bands[20-i-1]=self.bands_list[20-i-1]*self.sliders[i].value()
        
        for sublist in self.eq_bands :
            for x in sublist:
                    self.after_rq.append(x)
    
        self.recover_signal()
        recover=np.array(self.yt)
        self.fft(recover)
        self.specdata = np.real(recover)
        self.spectrogram()


    def zoom(self,val):
        self.x_range[1]=self.x_range[1]*val
        if val==zoomIn_scale:
            self.x_range[0]=self.x_range[0]*val
        else:
            self.x_range[0]=self.x_range[0]/val
        if self.x_range[1] >= np.max(self.time):
            self.x_range[1]=np.max(self.time)
        if self.x_range[0] <=  0:
            self.x_range[0]= 0
        self.graphicsView.setXRange(self.x_range[0],self.x_range[1])
        self.graphicsView_2.setXRange(self.x_range[0],self.x_range[1])
            
    def scroll(self,op):
        if op(self.x_range[1],2) >= np.max(self.time):
            self.x_range[0]= op(self.x_range[0],(np.max(self.time)-self.x_range[1]))
            self.x_range[1] = np.max(self.time)
        elif op(self.x_range[0],2) <= 0:
            self.x_range[1]= op(self.x_range[1],self.x_range[0])
            self.x_range[0]=0
        else:
            self.x_range[1]= op(self.x_range[1],2)
            self.x_range[0]= op(self.x_range[0],2)
        self.graphicsView.setXRange(self.x_range[0],self.x_range[1])
        self.graphicsView_2.setXRange(self.x_range[0],self.x_range[1])

    def palette(self,flag):
        if flag==1:
            self.cmap="jet"
        elif flag==2:
            self.cmap="cool"
        elif flag==3:
            self.cmap="plasma"
        elif flag==4:
            self.cmap="pink"
        else:
            self.cmap="PuOr_r"
        self.spectrogram()

    def pause_btn(self):
        self.timer.stop()
    
    def update(self):
            if self.x_range[1] < np.max(self.time):
                self.x_range[0]=self.x_range[0]+2
                self.x_range[1]=self.x_range[1]+2
                self.widgets[0].setXRange(self.x_range[0],self.x_range[1])
                self.widgets[1].setXRange(self.x_range[0],self.x_range[1])

    def play(self):
        self.timer =pg.QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update)
        self.timer.start(self.speed)

    def SpeedUp(self):
        if self.speed != 0:
            self.speed-=100
            

    def SpeedDown(self):
        self.speed +=100
        

    def Save_As_Pdf(self):
        plt.plot(self.time,self.data)
        plt.title('Original Sound')
        plt.xlabel('Time (sec)')
        plot1=plt.figure('1.png')
        plt.clf()
        plt.plot(self.time,np.real(self.yt))
        plt.title('Edited Sound')
        plt.xlabel('Time (sec)')
        plot2=plt.figure('2.png')
        plt.clf()
        plt.specgram(self.data,NFFT=len(self.data),Fs=self.samplingfrequency ,detrend='mean', mode='psd',cmap=self.cmap)
        plt.title('Original Sound Spectogram')
        plt.xlabel('Time (sec)')
        plt.ylabel('Frequency (Hz)')
        plt.colorbar()
        plot3=plt.figure('3.png')
        plt.clf()
        plt.specgram(np.real(self.yt),NFFT=len(np.real(self.yt)),Fs=self.samplingfrequency ,detrend='mean', mode='psd',cmap=self.cmap)
        plt.title('Edited Sound Spectrogram')
        plt.xlabel('Time (sec)')
        plt.ylabel('Frequency (Hz)')
        plt.colorbar()
        plot4=plt.figure('4.png')
        plt.clf()
        plt.plot(self.time,self.data)
        plt.title('Original Sound')
        plt.xlabel('Time')
        plot5=plt.figure('5.png')
        pp = PdfPages('Equalizer.pdf')
        pp.savefig(plot4)
        pp.savefig(plot1)
        pp.savefig(plot2)
        pp.savefig(plot3)
        pp.savefig(plot5)
        pp.close()
app = QtWidgets.QApplication(sys.argv)
application = ApplicationWindow()
application.show()
app.exec_()
