# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectile_movement_outputs.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(744, 437)
        self.range_label = QtWidgets.QLabel(Form)
        self.range_label.setGeometry(QtCore.QRect(20, 30, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        font.setPointSize(12)
        self.range_label.setFont(font)
        self.range_label.setFrameShape(QtWidgets.QFrame.Box)
        self.range_label.setLineWidth(3)
        self.range_label.setObjectName("range_label")
        self.range = QtWidgets.QLabel(Form)
        self.range.setGeometry(QtCore.QRect(180, 30, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        font.setPointSize(12)
        self.range.setFont(font)
        self.range.setFrameShape(QtWidgets.QFrame.Box)
        self.range.setLineWidth(3)
        self.range.setObjectName("range")
        self.V_highest_x_label = QtWidgets.QLabel(Form)
        self.V_highest_x_label.setGeometry(QtCore.QRect(410, 30, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        font.setPointSize(12)
        self.V_highest_x_label.setFont(font)
        self.V_highest_x_label.setFrameShape(QtWidgets.QFrame.Box)
        self.V_highest_x_label.setLineWidth(3)
        self.V_highest_x_label.setObjectName("V_highest_x_label")
        self.V_highest_x = QtWidgets.QLabel(Form)
        self.V_highest_x.setGeometry(QtCore.QRect(570, 30, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        font.setPointSize(12)
        self.V_highest_x.setFont(font)
        self.V_highest_x.setFrameShape(QtWidgets.QFrame.Box)
        self.V_highest_x.setLineWidth(3)
        self.V_highest_x.setObjectName("V_highest_x")
        self.V_highest_y = QtWidgets.QLabel(Form)
        self.V_highest_y.setGeometry(QtCore.QRect(570, 110, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        font.setPointSize(12)
        self.V_highest_y.setFont(font)
        self.V_highest_y.setFrameShape(QtWidgets.QFrame.Box)
        self.V_highest_y.setLineWidth(3)
        self.V_highest_y.setObjectName("V_highest_y")
        self.V_final_x_label = QtWidgets.QLabel(Form)
        self.V_final_x_label.setGeometry(QtCore.QRect(20, 110, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        font.setPointSize(12)
        self.V_final_x_label.setFont(font)
        self.V_final_x_label.setFrameShape(QtWidgets.QFrame.Box)
        self.V_final_x_label.setLineWidth(3)
        self.V_final_x_label.setObjectName("V_final_x_label")
        self.V_highest_y_label = QtWidgets.QLabel(Form)
        self.V_highest_y_label.setGeometry(QtCore.QRect(410, 110, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        font.setPointSize(12)
        self.V_highest_y_label.setFont(font)
        self.V_highest_y_label.setFrameShape(QtWidgets.QFrame.Box)
        self.V_highest_y_label.setLineWidth(3)
        self.V_highest_y_label.setObjectName("V_highest_y_label")
        self.V_final_x = QtWidgets.QLabel(Form)
        self.V_final_x.setGeometry(QtCore.QRect(180, 110, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        font.setPointSize(12)
        self.V_final_x.setFont(font)
        self.V_final_x.setFrameShape(QtWidgets.QFrame.Box)
        self.V_final_x.setLineWidth(3)
        self.V_final_x.setObjectName("V_final_x")
        self.x_highest = QtWidgets.QLabel(Form)
        self.x_highest.setGeometry(QtCore.QRect(570, 190, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        font.setPointSize(12)
        self.x_highest.setFont(font)
        self.x_highest.setFrameShape(QtWidgets.QFrame.Box)
        self.x_highest.setLineWidth(3)
        self.x_highest.setObjectName("x_highest")
        self.V_final_y_label = QtWidgets.QLabel(Form)
        self.V_final_y_label.setGeometry(QtCore.QRect(20, 190, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        font.setPointSize(12)
        self.V_final_y_label.setFont(font)
        self.V_final_y_label.setFrameShape(QtWidgets.QFrame.Box)
        self.V_final_y_label.setLineWidth(3)
        self.V_final_y_label.setObjectName("V_final_y_label")
        self.x_highest_label = QtWidgets.QLabel(Form)
        self.x_highest_label.setGeometry(QtCore.QRect(410, 190, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        font.setPointSize(12)
        self.x_highest_label.setFont(font)
        self.x_highest_label.setFrameShape(QtWidgets.QFrame.Box)
        self.x_highest_label.setLineWidth(3)
        self.x_highest_label.setObjectName("x_highest_label")
        self.V_final_y = QtWidgets.QLabel(Form)
        self.V_final_y.setGeometry(QtCore.QRect(180, 190, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        font.setPointSize(12)
        self.V_final_y.setFont(font)
        self.V_final_y.setFrameShape(QtWidgets.QFrame.Box)
        self.V_final_y.setLineWidth(3)
        self.V_final_y.setObjectName("V_final_y")
        self.y_highest = QtWidgets.QLabel(Form)
        self.y_highest.setGeometry(QtCore.QRect(570, 270, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        font.setPointSize(12)
        self.y_highest.setFont(font)
        self.y_highest.setFrameShape(QtWidgets.QFrame.Box)
        self.y_highest.setLineWidth(3)
        self.y_highest.setObjectName("y_highest")
        self.t_final_label = QtWidgets.QLabel(Form)
        self.t_final_label.setGeometry(QtCore.QRect(20, 270, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        font.setPointSize(12)
        self.t_final_label.setFont(font)
        self.t_final_label.setFrameShape(QtWidgets.QFrame.Box)
        self.t_final_label.setLineWidth(3)
        self.t_final_label.setObjectName("t_final_label")
        self.y_highest_label = QtWidgets.QLabel(Form)
        self.y_highest_label.setGeometry(QtCore.QRect(410, 270, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        font.setPointSize(12)
        self.y_highest_label.setFont(font)
        self.y_highest_label.setFrameShape(QtWidgets.QFrame.Box)
        self.y_highest_label.setLineWidth(3)
        self.y_highest_label.setObjectName("y_highest_label")
        self.t_final = QtWidgets.QLabel(Form)
        self.t_final.setGeometry(QtCore.QRect(180, 270, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        font.setPointSize(12)
        self.t_final.setFont(font)
        self.t_final.setFrameShape(QtWidgets.QFrame.Box)
        self.t_final.setLineWidth(3)
        self.t_final.setObjectName("t_final")
        self.t_highest = QtWidgets.QLabel(Form)
        self.t_highest.setGeometry(QtCore.QRect(570, 350, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        font.setPointSize(12)
        self.t_highest.setFont(font)
        self.t_highest.setFrameShape(QtWidgets.QFrame.Box)
        self.t_highest.setLineWidth(3)
        self.t_highest.setObjectName("t_highest")
        self.initial_theta_label = QtWidgets.QLabel(Form)
        self.initial_theta_label.setGeometry(QtCore.QRect(20, 350, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        font.setPointSize(12)
        self.initial_theta_label.setFont(font)
        self.initial_theta_label.setFrameShape(QtWidgets.QFrame.Box)
        self.initial_theta_label.setLineWidth(3)
        self.initial_theta_label.setObjectName("initial_theta_label")
        self.t_highest_label = QtWidgets.QLabel(Form)
        self.t_highest_label.setGeometry(QtCore.QRect(410, 350, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        font.setPointSize(12)
        self.t_highest_label.setFont(font)
        self.t_highest_label.setFrameShape(QtWidgets.QFrame.Box)
        self.t_highest_label.setLineWidth(3)
        self.t_highest_label.setObjectName("t_highest_label")
        self.initial_theta = QtWidgets.QLabel(Form)
        self.initial_theta.setGeometry(QtCore.QRect(180, 350, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        font.setPointSize(12)
        self.initial_theta.setFont(font)
        self.initial_theta.setFrameShape(QtWidgets.QFrame.Box)
        self.initial_theta.setLineWidth(3)
        self.initial_theta.setObjectName("initial_theta")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(350, 50, 31, 361))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.range_label.setText(_translate("Form", "range:"))
        self.range.setText(_translate("Form", "range"))
        self.V_highest_x_label.setText(_translate("Form", "V_highest_x"))
        self.V_highest_x.setText(_translate("Form", "V_highest_x"))
        self.V_highest_y.setText(_translate("Form", "V_highest_y"))
        self.V_final_x_label.setText(_translate("Form", "V_final_x:"))
        self.V_highest_y_label.setText(_translate("Form", "V_highest_y"))
        self.V_final_x.setText(_translate("Form", "V_final_x"))
        self.x_highest.setText(_translate("Form", "x_highest"))
        self.V_final_y_label.setText(_translate("Form", "V_final_y:"))
        self.x_highest_label.setText(_translate("Form", "x_highest:"))
        self.V_final_y.setText(_translate("Form", "V_final_y"))
        self.y_highest.setText(_translate("Form", "y_highest"))
        self.t_final_label.setText(_translate("Form", "t_final:"))
        self.y_highest_label.setText(_translate("Form", "y_highest:"))
        self.t_final.setText(_translate("Form", "t_final"))
        self.t_highest.setText(_translate("Form", "t_highest"))
        self.initial_theta_label.setText(_translate("Form", "initial_theta:"))
        self.t_highest_label.setText(_translate("Form", "t_highest:"))
        self.initial_theta.setText(_translate("Form", "initial_theta"))
        self.label.setText(_translate("Form", "O\n"
"U\n"
"T\n"
"P\n"
"U\n"
"T\n"
"S"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
