import sys
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import subprocess
import os

class XML_Edit(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AVid Media Composer TXT to BDNXML Tools v0.0.1")
        self.setGeometry(100, 100, 634, 265)
        self.setFixedSize(634, 265)
        self.setWindowIcon(QIcon('C:\\Users\\48716\\Desktop\\AVid Media Composer TXT to BDNXML Tools v0.0.1\\ICO1.ico'))
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose)

        self.menuStrip = self.menuBar()
        aboutAction = self.menuStrip.addAction("About")
        aboutAction.triggered.connect(self.show_about_dialog)

        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QtWidgets.QVBoxLayout(central_widget)

        self.checkBox1 = QtWidgets.QCheckBox("In TC", self)
        self.checkBox1.setGeometry(12, 232, 54, 16)

        self.checkBox2 = QtWidgets.QCheckBox("Out TC", self)
        self.checkBox2.setGeometry(72, 232, 60, 16)

        self.checkBox3 = QtWidgets.QCheckBox("Width", self)
        self.checkBox3.setGeometry(143, 232, 54, 16)

        self.checkBox4 = QtWidgets.QCheckBox("Height", self)
        self.checkBox4.setGeometry(203, 232, 60, 16)

        self.checkBox5 = QtWidgets.QCheckBox("X", self)
        self.checkBox5.setGeometry(277, 232, 30, 16)

        self.checkBox6 = QtWidgets.QCheckBox("Y", self)
        self.checkBox6.setGeometry(337, 232, 30, 16)

        self.replace = QtWidgets.QPushButton("Replace", self)
        self.replace.setGeometry(373, 228, 249, 23)
        self.replace.clicked.connect(self.xml_to_xml)

        self.txt_btn = QtWidgets.QPushButton("Open AVid Media Composer .txt File", self)
        self.txt_btn.setGeometry(12, 35, 227, 23)
        self.txt_btn.clicked.connect(self.open_txt_file)

        self.go_sxml = QtWidgets.QPushButton("GO", self)
        self.go_sxml.setGeometry(597, 89, 25, 23)
        self.go_sxml.clicked.connect(self.run_cmd)

        self.go_scsv = QtWidgets.QPushButton("GO", self)
        self.go_scsv.setGeometry(597, 118, 25, 23)
        self.go_scsv.clicked.connect(self.csv_run)

        self.textBox_txt_open = QtWidgets.QLineEdit(self)
        self.textBox_txt_open.setGeometry(245, 35, 377, 23)

        self.xml_save = QtWidgets.QPushButton("Save BDN XML .xml File", self)
        self.xml_save.setGeometry(12, 89, 300, 23)
        self.xml_save.clicked.connect(self.save_xml_file)

        self.csv_save = QtWidgets.QPushButton("Save CSV Chapter .csv File", self)
        self.csv_save.setGeometry(12, 118, 300, 23)
        self.csv_save.clicked.connect(self.save_csv_file)

        self.fps = QtWidgets.QLabel("Frame Rate:", self)
        self.fps.setGeometry(13, 67, 71, 12)

        self.comboBox1 = QtWidgets.QComboBox(self)
        self.comboBox1.setGeometry(90, 64, 69, 20)
        self.comboBox1.addItems(["23.976", "24", "25", "29.97", "59.94"])
        self.comboBox1.setCurrentText("23.976")

        self.labe = QtWidgets.QLabel(self)
        self.labe.setGeometry(0, 146, 637, 13)
        self.labe.setText(
            "............................................................................................................................................................................................................................................................................................................................"
        )

        self.textBox_xml_1_open = QtWidgets.QLineEdit(self)
        self.textBox_xml_1_open.setGeometry(245, 172, 377, 21)

        self.textBox_xml_2_open = QtWidgets.QLineEdit(self)
        self.textBox_xml_2_open.setGeometry(245, 201, 377, 21)

        self.xml_open_master = QtWidgets.QPushButton(
            "Open Main BDN XML .xml File", self
        )
        self.xml_open_master.setGeometry(12, 171, 227, 23)
        self.xml_open_master.clicked.connect(self.open_xml_main_file)

        self.xml_open_up_to_master = QtWidgets.QPushButton(
            "Open To Main BDN XML .xml File", self
        )
        self.xml_open_up_to_master.setGeometry(12, 200, 227, 23)
        self.xml_open_up_to_master.clicked.connect(self.open_xml_to_main_file)

        self.textBox_xml_save = QtWidgets.QLineEdit(self)
        self.textBox_xml_save.setGeometry(318, 89, 273, 23)

        self.textBox_csv_save = QtWidgets.QLineEdit(self)
        self.textBox_csv_save.setGeometry(318, 118, 273, 23)

        self.center()

    def show_about_dialog(self):
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("About")

        dialog.setFixedSize(285, 150)

        parent_geometry = self.geometry()
        dialog_x = parent_geometry.x() + (parent_geometry.width() - dialog.width()) // 2
        dialog_y = parent_geometry.y() + (parent_geometry.height() - dialog.height()) // 2
        dialog.move(dialog_x, dialog_y)
        
        layout = QtWidgets.QVBoxLayout(dialog)
        
        label = QtWidgets.QLabel("Avid Media Composer\nTXT to BDNXML Tools v0.0.1\nCopyright (C) 2024 by@KSSW")
        font = QtGui.QFont("Arial, Bold", 14)
        label.setFont(font)
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(label)

        dialog.setLayout(layout)
        dialog.exec()

    def center(self):
        screen = QtWidgets.QApplication.primaryScreen().size()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

    def open_txt_file(self):
        txt_file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Open AVid Media Composer .txt File",
            "",
            "AVid Media Composer Text File (*.txt)",
        )
        if txt_file:
            self.textBox_txt_open.setText(txt_file)

    def save_xml_file(self):
        xml_file, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save BDN XML .xml File", "", "BDN XML .xml File (*.xml)"
        )
        if xml_file:
            self.textBox_xml_save.setText(xml_file)

    def save_csv_file(self):
        csv_file, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save CSV Chapter .csv File", "", "CSV Chapter .csv File (*.csv)"
        )
        if csv_file:
            self.textBox_csv_save.setText(csv_file)

    def open_xml_main_file(self):
        
        xml_main_file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open Main BDN XML File", "", "BDN XML File (*.xml)"
        )
        if xml_main_file:
            
            self.textBox_xml_1_open.setText(xml_main_file)

    def open_xml_to_main_file(self):
        xml_to_main_file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open To Main BDN XML File", "", "BDN XML File (*.xml)"
        )
        if xml_to_main_file:
            self.textBox_xml_2_open.setText(xml_to_main_file)

    def run_cmd(self):
        fps = self.comboBox1.currentText()
        finput_txt = self.textBox_txt_open.text().strip()
        foutput_xml = self.textBox_xml_save.text().strip()

        
        if not finput_txt or not foutput_xml:
            msg_box = QMessageBox(self)
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setWindowIcon(QIcon('C:\\Users\\48716\\Desktop\\AVid Media Composer TXT to BDNXML Tools v0.0.1\\ICO1.ico'))
            msg_box.setWindowFlags(
                Qt.WindowType.Dialog
                | Qt.WindowType.WindowTitleHint
                | Qt.WindowType.WindowCloseButtonHint
            )
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please input txt file and save xml file.")
            msg_box.setStandardButtons(
                QMessageBox.StandardButton.Ok
            ) 
            msg_box.exec()
            return

        
        command = f"Tools/BDN XML.exe"
        args = [finput_txt, "-o", foutput_xml, "-fps", fps]
        full_command = [command] + args
        full_command_path = os.path.abspath(command)  

        if not os.path.isfile(full_command_path):
            QtWidgets.QMessageBox.critical(None, "Error", "The specified ''Tools/BDN XML.exe'' does not exist")
            return
        
        try:
            subprocess.Popen(full_command, shell=True)
        except Exception as e:
            print(f"Error: {e}")

    def csv_run(self):
        fps = self.comboBox1.currentText()
        finput_txt = self.textBox_txt_open.text().strip()
        foutput_csv = self.textBox_csv_save.text().strip()

        if not finput_txt or not foutput_csv:
            msg_box = QMessageBox(self)
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setWindowIcon(QIcon('C:\\Users\\48716\\Desktop\\AVid Media Composer TXT to BDNXML Tools v0.0.1\\ICO1.ico'))
            msg_box.setWindowFlags(
                Qt.WindowType.Dialog
                | Qt.WindowType.WindowTitleHint
                | Qt.WindowType.WindowCloseButtonHint
            )
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please input txt file and save csv file.")
            msg_box.setStandardButtons(
                QMessageBox.StandardButton.Ok
            )
            msg_box.exec()
            return

        command = f"Tools/CSV Chapter.exe"
        args = [finput_txt, "-o", foutput_csv, "-fps", fps]
        full_command = [command] + args
        full_command_path = os.path.abspath(command)  

        if not os.path.isfile(full_command_path):
            QtWidgets.QMessageBox.critical(None, "Error", "The specified ''Tools/CSV Chapter.exe'' does not exist")
            return

        try:
            subprocess.Popen(full_command, shell=True)
        except Exception as e:
            print(f"Error: {e}")

    def xml_to_xml(self):
        itc = "-itc" if self.checkBox1.isChecked() else ""
        otc = "-otc" if self.checkBox2.isChecked() else ""
        w = "-w" if self.checkBox3.isChecked() else ""
        he = "-he" if self.checkBox4.isChecked() else ""
        x = "-x" if self.checkBox5.isChecked() else ""
        y = "-y" if self.checkBox6.isChecked() else ""
        finput_xml_1 = self.textBox_xml_1_open.text().strip()
        finput_xml_2 = self.textBox_xml_2_open.text().strip()

        if not finput_xml_1 or not finput_xml_2:
            msg_box = QMessageBox(self)
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setWindowIcon(QIcon('C:\\Users\\48716\\Desktop\\AVid Media Composer TXT to BDNXML Tools v0.0.1\\ICO1.ico'))
            msg_box.setWindowFlags(
                Qt.WindowType.Dialog
                | Qt.WindowType.WindowTitleHint
                | Qt.WindowType.WindowCloseButtonHint
            )
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please Open Main BDN XML and To Main BDN XML Files.")
            msg_box.setStandardButtons(
                QMessageBox.StandardButton.Ok
            )  
            msg_box.exec()
            return

        if not (itc or otc or w or he or x or y):
            msg_box = QMessageBox(self)
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setWindowIcon(QIcon('C:\\Users\\48716\\Desktop\\AVid Media Composer TXT to BDNXML Tools v0.0.1\\ICO1.ico'))
            msg_box.setWindowFlags(
                Qt.WindowType.Dialog
                | Qt.WindowType.WindowTitleHint
                | Qt.WindowType.WindowCloseButtonHint
            )
            msg_box.setWindowTitle("Error")
            msg_box.setText("Must one replace value")
            msg_box.setStandardButtons(
                QMessageBox.StandardButton.Ok
            )  
            msg_box.exec()
            return

        command = f"Tools/BDN XML to BDN XML.exe"
        
        args = [finput_xml_1, finput_xml_2]
        full_command_path = os.path.abspath(command)  

        if not os.path.isfile(full_command_path):
            QtWidgets.QMessageBox.critical(None, "Error", "The specified ''Tools/BDN XML to BDN XML.exe'' does not exist")
            return
        
        if itc:
            args.append(itc)
        if otc:
            args.append(otc)
        if w:
            args.append(w)
        if he:
            args.append(he)
        if x:
            args.append(x)
        if y:
            args.append(y)

        full_command = [command] + args

        # print(f"Executing command: {' '.join(full_command)}")

        try:
            result = subprocess.run([command] + args, check=True, capture_output=True, text=True)
            output = result.stdout
            error_message = result.stderr

            if "Error" in output:
                msg_box = QtWidgets.QMessageBox(self)
                msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                msg_box.setWindowTitle("Error")
                msg_box.setText("")
                msg_box.setInformativeText(output)
                msg_box.setWindowIcon(QtGui.QIcon('C:\\Users\\48716\\Desktop\\AVid Media Composer TXT to BDNXML Tools v0.0.1\\1ICO.ico'))
                msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg_box.exec()
                
        except subprocess.CalledProcessError as e:    
            error_message = e.stderr.decode() if e.stderr else "Unknown Error"
            msg_box = QtWidgets.QMessageBox(self)
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText("")
            msg_box.setInformativeText(error_message)
            msg_box.setWindowIcon(QtGui.QIcon('C:\\Users\\48716\\Desktop\\AVid Media Composer TXT to BDNXML Tools v0.0.1\\1ICO.ico'))
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg_box.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = XML_Edit()
    window.show()
    sys.exit(app.exec())
