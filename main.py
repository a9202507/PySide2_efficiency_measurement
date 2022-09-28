# Rev2022.09.02 init
# a9202507@gmail.com

import sys
from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PySide2.QtGui import QIcon
import efficiency_ui
import visa_function as myvisa
import pandas as pd
import time
import datetime
import openpyxl

class efficiency_measure_thread(QThread):
    efficiency_process_bar = Signal(int)

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        cooldown_time = float(myWin.lineEdit_22.text())
        duration_time = float(myWin.lineEdit_21.text())

        end_current = float(myWin.lineEdit_19.text())
        percentage = (float(myWin.lineEdit_20.text()))/100

        iout_list = [0]
        iout_step = end_current*percentage
        itemp = iout_step
        while itemp <= end_current:
            iout_list.append(itemp)
            itemp += iout_step
        myWin.push_msg_to_GUI(f"iout_list={iout_list}")

        efficiency_result_dict = dict()
        efficiency_result_df = pd.DataFrame()

        for iout_idx, iout in enumerate(iout_list):
            # myWin.set_process_bar(int(iout_idx/(len(iout_list))))
            bar_value = int((iout_idx)/(len(iout_list))*100)
            #print(iout_idx, temp_value)
            self.efficiency_process_bar.emit(bar_value)
            # for iout in iout_list:
            myWin.push_msg_to_GUI(f"Iout={iout}")
            myWin.eload.abort()
            time.sleep(cooldown_time)
            myWin.eload.setCurrent(9, iout)
            myWin.eload.run()
            time.sleep(duration_time)
            myWin.get_all_daq_value_once()

            # save value to DF
            efficiency_result_dict['Vin'] = myWin.vin_measurement_value
            efficiency_result_dict['Iin'] = myWin.iin_measurement_value
            efficiency_result_dict['Vout'] = myWin.vout_measurement_value
            efficiency_result_dict['Iout'] = myWin.iout_measurement_value

            efficiency_result_df = efficiency_result_df.append(
                efficiency_result_dict, ignore_index=True)
        myWin.eload.abort()
        self.efficiency_process_bar.emit(100)
        myWin.push_msg_to_GUI("completed")
        df = pd.DataFrame(efficiency_result_df, columns=[
                          "Vin", "Iin", "Vout", "Iout"])
        df.to_excel(f"{str(datetime.datetime.now().timestamp())+'.xlsx'}")

    def stop(self):
        myWin.push_msg_to_GUI("user click stop")
        self.terminate()


class MyMainWindow(QMainWindow, efficiency_ui.Ui_MainWindow):
    def __init__(self, parent=None, debug=True):
        super(MyMainWindow, self).__init__(parent)
        self.setFixedSize(730, 850)
        self.setupUi(self)
        self.debug = debug

        self.setWindowTitle("Rev 2022.09.28")
        if self.debug:
            self.push_msg_to_GUI("Debug mode")

        self.pushButton_6.clicked.connect(self.update_equipment_on_combox)

        self.comboBox.currentIndexChanged.connect(self.update_dcsource_name)
        self.comboBox_7.currentIndexChanged.connect(self.update_DAQ_name)
        self.comboBox_3.currentIndexChanged.connect(self.update_eload_name)
        self.pushButton_12.clicked.connect(self.get_all_daq_value_once)
        self.pushButton_8.clicked.connect(self.run_efficiency_measurement)
        self.pushButton_4.clicked.connect(self.abort_efficiency_measurement)
        self.pushButton_5.clicked.connect(self.clear_log_msg)

        # DCsource
        self.radioButton.toggled.connect(
            self.update_GUI_and_set_dcsource_on)
        self.radioButton_2.toggled.connect(
            self.update_GUI_and_set_dcsource_off)

        # Chroma eload
        self.radioButton_6.toggled.connect(self.udpate_GUI_and_set_eload_on)
        self.radioButton_5.toggled.connect(self.udpate_GUI_and_set_eload_off)

        # DAQ
        self.pushButton_13.clicked.connect(
            self.update_GUI_and_get_DAQ_value_once)

        # init thread
        self.efficiency_measurement_thread = efficiency_measure_thread()
        self.efficiency_measurement_thread.efficiency_process_bar.connect(
            self.set_process_bar)

        # 
        self.actionAbout_the_GUI.triggered.connect(self.about_the_GUI)

    def update_GUI_and_get_DAQ_value_once(self):
        self.update_GUI()
        self.DAQ = myvisa.agilentDAQ(self.comboBox_7.currentText())
        self.DAQ.read_channel_voltage(self.comboBox_2.currentText())
        result = self.DAQ.get_voltage_result()
        self.push_msg_to_GUI(
            f"DAQ CH{self.comboBox_2.currentText()} reading value is {result}")

    def udpate_GUI_and_set_eload_on(self):
        self.update_GUI()
        self.eload = myvisa.chromaEload(self.comboBox_3.currentText())
        self.eload.setCurrent(9, float(self.lineEdit_23.text()))
        self.eload.run()

    def udpate_GUI_and_set_eload_off(self):
        self.update_GUI()
        self.eload.abort()

    def update_GUI_and_set_dcsource_on(self):
        self.update_GUI()
        self.dcsource.set_voltage(self.dcsource_voltage_float)
        self.dcsource.set_current(self.dcsource_current_float)
        self.dcsource.on()

    def update_GUI_and_set_dcsource_off(self):
        self.update_GUI()
        self.dcsource.off()

    def update_GUI(self):
        self.dcsource_voltage_float = float(self.lineEdit_16.text())
        self.dcsource_current_float = float(self.lineEdit_17.text())

    def update_equipment_on_combox(self):
        self.get_visa_resource()
        self.comboBox.clear()
        self.comboBox.addItem("")
        self.comboBox.addItems(self.resource_list)

        self.comboBox_7.clear()
        self.comboBox_7.addItem("")
        self.comboBox_7.addItems(self.resource_list)

        self.comboBox_3.clear()
        self.comboBox_3.addItem("")
        self.comboBox_3.addItems(self.resource_list)

    def update_dcsource_name(self):
        self.lineEdit_28.clear()
        if self.comboBox.currentText() != "":
            self.dcsource = myvisa.gpibChromaDCSource(
                self.comboBox.currentText())
            device_name = self.dcsource.get_equipment_name()
            self.lineEdit_28.setText(device_name)

    def update_DAQ_name(self):
        self.lineEdit_29.clear()
        if self.comboBox_7.currentText() != "":
            self.DAQ = myvisa.agilentDAQ(self.comboBox_7.currentText())
            device_name = self.DAQ.get_equipment_name()
            self.lineEdit_29.setText(device_name)

    def update_eload_name(self):
        self.lineEdit_30.clear()
        if self.comboBox_3.currentText() != "":
            self.eload = myvisa.chromaEload(
                self.comboBox_3.currentText())
            device_name = self.eload.get_equipment_name()
            self.lineEdit_30.setText(device_name)

    def get_visa_resource(self):

        self.resource_list = myvisa.get_visa_resource_list()
        if self.debug == True:
            self.push_msg_to_GUI(self.resource_list)

    def push_msg_to_GUI(self, msg=""):
        if True:
            self.textEdit.append(str(msg))
            # self.textEdit.append("")
        else:
            pass

    def clear_log_msg(self):
        self.textEdit.clear()

    def get_all_daq_value_once(self):
        self.update_GUI()

        self.DAQ.read_channel_voltage(self.comboBox_4.currentText())
        self.vout_measurement_value = float(self.DAQ.get_voltage_result())
        self.DAQ.read_channel_voltage(self.comboBox_2.currentText())
        self.vin_measurement_value = float(self.DAQ.get_voltage_result())
        self.dcsource.measure_current()
        self.iin_measurement_value = float(self.dcsource.measure_current_value)
        self.iout_measurement_value = float(self.eload.getCurrentMeasurement())

        self.push_msg_to_GUI(
            f"line139 vout={self.vout_measurement_value},vin={self.vin_measurement_value},Iin={self.iin_measurement_value}")

    def abort_efficiency_measurement(self):
        self.efficiency_measurement_thread.stop()

    def run_efficiency_measurement(self, iout_list=0, cooldown_time=2, duration_time=2):

        self.efficiency_measurement_thread.start()

    def set_process_bar(self, value):
        self.progressBar.setValue(value)

    def about_the_GUI(self):
        QMessageBox.about(self, "about the GUI",'Powered by PySide2 and <a href=https://github.com/a9202507/PySide2_efficiency_measurement>Source code</a>' )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWin = MyMainWindow(debug=True)

    myWin.show()

    sys.exit(app.exec_())
