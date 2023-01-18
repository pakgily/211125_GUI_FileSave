import sys
import os
from PySide2.QtWidgets import QWidget, QMainWindow, QApplication, QFileDialog
from PySide2.QtGui import QPalette, QPainter, QPixmap, QScreen
from PySide2.QtCore import Signal,Qt, QRect, QPointF
from loadUi import Ui_MainWindow

import export_excel

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.ImportFile)
        self.pushButton_2.clicked.connect(self.ReportSave)
        self.pushButton_3.clicked.connect(self.ReportOpen)

    def ImportFile(self):
        self.fname = QFileDialog.getOpenFileNames(self, 'File Open',r"C:\Users\Administrator\Desktop",'MeasurQScreen grabwindow pythone File(*.dat)')  # FileDialog Fime Name을 File Open으로 함./r"" Default 경로 지정
        self.textEdit.setText(self.fname[0][0])
        # if self.fname[0][0] != "":
        #     os.system(self.fname[0][0]) # 선택한 파일을 Open 하는 명령어
        #     print(self.fname[0][0])

        print(self.winId())
        print(type(self.winId()))
        # QScreen.grabWindow(self.winId())
        img = QPixmap.grabWindow(self.winId())
        # img = QPixmap.grabWindow(0)
        # QPixmap.grabWidget(self.centralwidget) #지원 중단 경고
        # QPixmap.grabWidget()
        print(img)
        img.save("png.jpg")

    def ReportSave(self):
        self.sname = QFileDialog.getSaveFileName(self, 'Save File','.xlsx',"excel file (*.xlsx)")  # File 그 자체를 저장하는 것이 아니라 Save Dialog에서 User가 저장한 파일명이 저장 Button 시에 전달되는 것.
        print(self.sname[0])
        Result = export_excel.run(self.sname[0])
        if Result == 1:
            self.textEdit_2.setText("분석 및 저장완료")
            # os.system((self.sname[0]))

    def ReportOpen(self):
        # QFileDialog.getOpenFileName(self, 'Report File Confirm',self.sname[0])
        # QFileDialog.getOpenFileName(self, 'Report File Confirm', './')
        os.system((self.sname[0]))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
