'''
Python에서 맥주소를 가져오기!
'''
import sys,os, urllib.request
from PyQt4.QtGui import *
def getMacAddress():
    arrinfo = {}
    isdevice = 0
    mk = 0
    if sys.platform=='win32':
        for line in os.popen("ipconfig /all"):
            if line.lstrip().startswith('호스트'):
                host = line.split(':')[1].strip()
                arrinfo["host"] =  host
            else:
                if line.lstrip().startswith('터널'):
                    isdevice = 0
                if line.lstrip().startswith('이더넷'):
                    isdevice = 1
                if line.lstrip().startswith('무선'):
                    isdevice = 1
                if isdevice == 1:
                    if line.lstrip().startswith('미디어 상태'):
                        desc = line.split(':')[1].strip()
                        if desc == '미디어 연결 끊김':
                            isdevice = 0
                    if line.lstrip().startswith('설명'):
                        desc = line.split(':')[1].strip()
                        if desc.lstrip().startswith('Bluetooth'):
                            isdevice = 0
                    if line.lstrip().startswith('물리적'):
                        #mac = line.split(':')[1].strip().replace('-',':')
                        mac = line.split(':')[1].strip()
                        arrinfo[mk] =  mac
                        isdevice = 0
                        mk+=1
    else:
        for line in os.popen("/sbin/ifconfig"):
            if line.find('Ether') >-1:
                mac=line.split()[4]
                arrinfo[mk] =  mac
                isdevice = 0
                mk+=1
    return arrinfo
class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        lblName = QLabel("Name")
        self.editName = QLineEdit()
        self.txtEdit = QTextEdit()
        btnOk = QPushButton("Mac Address")
        layout = QVBoxLayout()
        layout.addWidget(lblName)
        layout.addWidget(self.txtEdit)
        layout.addWidget(self.editName)
        layout.addWidget(btnOk)
        self.setLayout(layout)
        btnOk.clicked.connect(self.btnOkClicked)
    def btnOkClicked(self):
        #name = self.editName.text()
        arrinfo = getMacAddress()
        self.txtEdit.setText("HOST : "+arrinfo['host']
                +"\n"+"MAC 1 : "+arrinfo[0]
                +"\nMAC 2 : "+arrinfo[1]
                +"\nMAC 3 : "+arrinfo[2])
        #QMessageBox.information(self, "Info", arrinfo[0]+arrinfo[1])
app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()

