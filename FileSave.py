import numpy as np
import pandas as pd
from asammdf import MDF, Signal
import  dataframe_image as dfi
import os
import time
from PIL import Image

import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt, Signal, Slot

class windget(QWidget): #windget 자식 Class에 QtWidgets 모듈의 QWidget Class라는 부모 Class를 상속
    ok = Signal(str) #QtCore 모듈의 Class로 ok 객체 선언(ok 객체란 Signal() Class의 인스턴스) / 사용자 정의 Signal
    fname = []

    def __init__(self):
        super().__init__() #부모 Class인 QWidget Class의 생성자를 상속함.

        self.pushButton = QPushButton("File Open") #QPushButton은 QAbstractButton 부모 Class로부터 상속 받음, 즉, QAbstarctButton Class 사용가능
        self.pushButton.clicked.connect(self.buttonClicked)

        layout = QVBoxLayout() #QtWidgets 모듈의 QVBoxLayout Class layout 객체 선언
        layout.addWidget(self.pushButton)

        # QWidget.setLayout(layout)
        self.setLayout(layout) #상속된 QWidget Class 내 함수로 기본 창에 상기 PushButton을 위치시키기 위함.

    def buttonClicked(self):
        self.fname = QFileDialog.getSaveFileName(self,'Save File','.py',"python file (*.py)") #File 그 자체를 저장하는 것이 아니라 Save Dialog에서 User가 저장한 파일명이 저장 Button 시에 전달되는 것.
        self.ok.emit(self.fname) #Signal 발생
        # print(self.ok.emit())

    @Slot() # Custom Signal 생성 시,
    def datafile(self):
         print("signal1 emitted")

if __name__ == "__main__":
    app = QApplication(sys.argv) # GUI App Roop Start
    w = windget()
    w.resize(400, 240)
    w.ok.connect(w.datafile)  # GUI Root Exit
    # w.ok.connect(app.exit) # GUI Root Exit
    w.show()

    app.exec_() #이벤트 루프 생성 Root End

    print(w.fname)


