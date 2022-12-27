# Rev2022.09.02 init
# a9202507@gmail.com

import sys
import traceback
from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PySide2.QtGui import QIcon
import efficiency_ui
import visa_function as myvisa
import pandas as pd
import time
import datetime
import openpyxl
import os
import json
from UliPlot.XLSX import auto_adjust_xlsx_column_width

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
        while float(format(itemp,".2f")) <= end_current:
            iout_list.append(format(itemp,".2f"))
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
            efficiency_result_dict['Istep']=float(iout)
            efficiency_result_dict['Vin'] = myWin.vin_measurement_value
            efficiency_result_dict['Iin'] = myWin.iin_measurement_value
            efficiency_result_dict['Vout'] = myWin.vout_measurement_value
            efficiency_result_dict['remote Vout sense']=myWin.vout2_measurement_value
            efficiency_result_dict['Iout'] = myWin.iout_measurement_value

            efficiency=(efficiency_result_dict['Vout']*efficiency_result_dict['Iout'])/(efficiency_result_dict['Vin']*efficiency_result_dict['Iin'])
            efficiency_remote=(efficiency_result_dict['remote Vout sense']*efficiency_result_dict['Iout'])/(efficiency_result_dict['Vin']*efficiency_result_dict['Iin'])

            efficiency_result_dict['Efficiency'] = float(format(efficiency*100,".3f"))
            efficiency_result_dict['Efficiency_remote'] = float(format(efficiency_remote*100,".3f"))
            

            efficiency_result_df = efficiency_result_df.append(
                efficiency_result_dict, ignore_index=True)
        myWin.eload.abort()
        self.efficiency_process_bar.emit(100)
        myWin.push_msg_to_GUI("completed")
        df = pd.DataFrame(efficiency_result_df, columns=[
                          "Istep","Vin", "Iin", "Vout","remote Vout sense", "Iout","Efficiency","Efficiency_remote"])
        #now=datetime.datetime.now()
        #filename=now.strftime('%Y%m%d_%H%M%S')
        #df.to_excel(filename+'.xlsx')
        ##df.to_excel("./reports/"+myWin.save_filename+".xlsx",sheet_name=f"{myWin.lineEdit_16.text()}Vin_{format(df['Vout'][0],'.2f')}Vout_{end_current}Amps")


        mysheet=f"{myWin.lineEdit_16.text()}Vin_{format(df['Vout'][0],'.2f')}Vout_{end_current}Amps"
        with pd.ExcelWriter("./reports/"+myWin.save_filename+".xlsx") as writer:
            df.to_excel(writer, sheet_name=mysheet)
            auto_adjust_xlsx_column_width(df, writer, sheet_name=mysheet, margin=5)


        myWin.open_report_folder()

    def stop(self):
        myWin.push_msg_to_GUI("user click stop")
        self.terminate()


class MyMainWindow(QMainWindow, efficiency_ui.Ui_MainWindow):
    def __init__(self, parent=None, debug=True):
        super(MyMainWindow, self).__init__(parent)
        self.setFixedSize(730, 780)
        self.setupUi(self)
        self.debug = debug

        self.setWindowTitle("Rev 2022.12.27")
        if self.debug:
            self.push_msg_to_GUI("Debug mode")

        self.pushButton_6.clicked.connect(self.update_equipment_on_combox)

        self.comboBox.currentIndexChanged.connect(self.update_dcsource_name)
        self.comboBox_7.currentIndexChanged.connect(self.update_DAQ_name)
        self.comboBox_3.currentIndexChanged.connect(self.update_eload_name)
        self.pushButton_13.clicked.connect(self.get_all_daq_value_once)
        self.pushButton_8.clicked.connect(self.run_efficiency_measurement)
        self.pushButton_4.clicked.connect(self.abort_efficiency_measurement)
        self.pushButton_5.clicked.connect(self.clear_log_msg)
        self.pushButton_11.clicked.connect(self.open_report_folder)
        self.comboBox_5.setEnabled(True)
        self.groupBox_4.setEnabled(True)
        #self.lineEdit_27.setEnabled(True)
        self.checkBox_2.setEnabled(False)
        self.pushButton_11.setEnabled(True)
        #self.lineEdit_27.setReadOnly(False)

        self.actionLoad_config.setEnabled(True)
        self.actionLoad_config.triggered.connect(self.load_config)
        self.actionSave_config.setEnabled(True)
        self.actionSave_config.triggered.connect(self.save_config)

        ## test function 
        #self.pushButton_12.clicked.connect(self.test_folder_function)

        # DCsource

        self.checkBox_8.stateChanged.connect(self.select_dc_source_vendor)

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

        ###
        #self.load_config_sub2('./init.json')

        ## test only
        self.comboBox_2.addItem("201")

    def create_filename_includes_condition_timestamp(self):
        myreportpath=self.lineEdit_27.text()
        if myreportpath[0]!=".":
            myreportpath="."+myreportpath
        if os.path.isdir(myreportpath) is False:
            os.makedirs(myreportpath)
            #self.push_msg_to_GUI(f"create {myreportpath} successful")
        else:
            #self.push_msg_to_GUI(f"the {myreportpath} already exist")
            pass
        vin=self.lineEdit_16.text()
        self.get_all_daq_value_once()
        vout=format(self.vout_measurement_value,".3f")
        now=datetime.datetime.now()
        now_stamp=now.strftime('%Y%m%d_%H%M%S')
        filename=f"{self.lineEdit_7.text()}_{vin}Vin_{vout}Vout_{self.lineEdit_19.text()}Amps_Istep{self.lineEdit_20.text()}pct_{now_stamp}"
        #self.push_msg_to_GUI(f"filename={filename}")
        self.save_filename=filename

    def update_GUI_and_get_DAQ_value_once(self):
        self.update_GUI()
        self.DAQ = myvisa.agilentDAQ(self.comboBox_7.currentText())

        if self.comboBox_2.currentText() != "":
            self.DAQ.read_channel_voltage(self.comboBox_2.currentText())
            result = self.DAQ.get_voltage_result()
            self.push_msg_to_GUI(
                f"DAQ CH{self.comboBox_2.currentText()} reading value is {result}")
            time.sleep(1)

        if self.comboBox_4.currentText() != "":
            self.DAQ.read_channel_voltage(self.comboBox_4.currentText())
            result = self.DAQ.get_voltage_result()
            self.push_msg_to_GUI(
                f"DAQ CH{self.comboBox_4.currentText()} reading value is {result}")
            time.sleep(1)

        if self.comboBox_5.currentText() != "":  
            self.DAQ.read_channel_voltage(self.comboBox_5.currentText())
            result = self.DAQ.get_voltage_result()
            self.push_msg_to_GUI(
                f"DAQ CH{self.comboBox_5.currentText()} reading value is {result}")

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

    def select_dc_source_vendor(self):

        if self.checkBox_8.isChecked() == True:
            self.set_dc_source_to_Agilent()
        else:
            self.set_dc_source_to_Chroma()
        

    def set_dc_source_to_Agilent(self): 

        self.dcsource = myvisa.agilent_DCSource(self.comboBox.currentText())

    def set_dc_source_to_Chroma(self):
        self.dcsource = myvisa.gpibChromaDCSource(self.comboBox.currentText())

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
        self.DAQ.read_channel_voltage(self.comboBox_5.currentText())
        self.vout2_measurement_value = float(self.DAQ.get_voltage_result())
        self.DAQ.read_channel_voltage(self.comboBox_2.currentText())
        self.vin_measurement_value = float(self.DAQ.get_voltage_result())
        self.dcsource.measure_current()
        self.iin_measurement_value = float(self.dcsource.measure_current_value)
        self.iout_measurement_value = float(self.eload.getCurrentMeasurement())

        self.push_msg_to_GUI(
            f"vout={self.vout_measurement_value}, vout2={self.vout2_measurement_value},vin={self.vin_measurement_value},Iin={self.iin_measurement_value}")

    def abort_efficiency_measurement(self):
        self.efficiency_measurement_thread.stop()

    def run_efficiency_measurement(self, iout_list=0, cooldown_time=2, duration_time=2):
        self.create_filename_includes_condition_timestamp() # get filename for report.
        self.efficiency_measurement_thread.start()

    def set_process_bar(self, value):
        self.progressBar.setValue(value)

    def about_the_GUI(self):
        QMessageBox.about(self, "about the GUI",'Powered by PySide2 and <a href=https://github.com/a9202507/PySide2_efficiency_measurement>Source code</a>' )

    def load_config(self):
        filenames=self.load_config_sub1()
        self.load_config_sub2(filenames)

    def load_config_sub1(self):

        try:
            dlg = QFileDialog(self, 'Open File', '.',
                              'JSON Files (*.json);;All Files (*)')
            if dlg.exec_():
                filenames = dlg.selectedFiles()

                return filenames

                with open(filenames[0], 'r') as j:
                    json_data = json.load(j)
                    
                self.lineEdit_16.setText(json_data["main_dcsource_voltage"])
                self.lineEdit_17.setText(json_data["main_dcsource_current"])
                self.lineEdit_18.setText(json_data["main_condition_start_current"])
                self.lineEdit_19.setText(json_data["main_condition_end_current"])
                self.lineEdit_20.setText(json_data["main_condition_percentage"])
                self.lineEdit_21.setText(json_data["main_condition_duration_time"])
                self.lineEdit_22.setText(json_data["main_condition_cooldown_time"])

            else:
                QMessageBox.about(
                    self, "Warning", "It can't support this page")
        except:
            QMessageBox.about(
                self, "Warning", "The JSON file can't match this page, please select another .JSON file")

    def load_config_sub2(self,filenames):

        with open(filenames[0], 'r') as j:
                    json_data = json.load(j)
                    
        self.lineEdit_16.setText(json_data["main_dcsource_voltage"])
        self.lineEdit_17.setText(json_data["main_dcsource_current"])
        self.lineEdit_18.setText(json_data["main_condition_start_current"])
        self.lineEdit_19.setText(json_data["main_condition_end_current"])
        self.lineEdit_20.setText(json_data["main_condition_percentage"])
        self.lineEdit_21.setText(json_data["main_condition_duration_time"])
        self.lineEdit_22.setText(json_data["main_condition_cooldown_time"])
        self.lineEdit_27.setText(json_data["setting_misc_save_folder"])
        self.lineEdit_7.setText(json_data["setting_misc_save_filename"])
        self.comboBox_2.setCurrentText(json_data["setting_daq_vin_channel"])
        self.comboBox_4.setCurrentText(json_data["setting_daq_vout_channel"])
        self.comboBox_5.setCurrentText(json_data["setting_daq_vout2_channel"])
        self.comboBox.setCurrentText(json_data["setting_equipment_DC_source"])
        self.comboBox_7.setCurrentText(json_data["setting_equipment_DAQ"])
        self.comboBox_3.setCurrentText(json_data["setting_equipment_e_load"])

    def save_config(self):
        if True:
            self.parameter_dict = {"main_dcsource_voltage": self.lineEdit_16.text(),
                                   "main_dcsource_current": self.lineEdit_17.text(),
                                   "main_condition_start_current":self.lineEdit_18.text(),
                                   "main_condition_end_current":self.lineEdit_19.text(),
                                   "main_condition_percentage":self.lineEdit_20.text(),
                                   "main_condition_duration_time":self.lineEdit_21.text(),
                                   "main_condition_cooldown_time":self.lineEdit_22.text(),
                                   "setting_misc_save_folder":self.lineEdit_27.text(),
                                   "setting_misc_save_filename":self.lineEdit_7.text(),
                                   "setting_daq_vin_channel":self.comboBox_2.currentText(),
                                   "setting_daq_vout_channel":self.comboBox_4.currentText(),
                                   "setting_daq_vout2_channel":self.comboBox_5.currentText(),
                                   "setting_equipment_DC_source":self.comboBox.currentText(),
                                   "setting_equipment_DAQ":self.comboBox_7.currentText(),
                                   "setting_equipment_e_load":self.comboBox_3.currentText(),
                                   }
        
        filename_with_path = QFileDialog.getSaveFileName(
            self, 'Save File', '.', 'JSON Files (*.json)')
        save_filename = filename_with_path[0]
        if save_filename != "":
            with open(save_filename, 'w') as fp:
                #json.dump(self.parameter_dict, fp)
                fp.write(json.dumps(self.parameter_dict, indent=4))
        # else:
            # print(self.tabWidget.currentIndex)
            #print("only can save first tab now")

        self.parameter_dict.clear()

    def open_report_folder(self):
        path=self.lineEdit_27.text()
        os.system(f'start {os.path.realpath(path)}')


def run():
   try:
        
        app = QApplication(sys.argv)

        myWin = MyMainWindow(debug=True)

        myWin.show()

        sys.exit(app.exec_())
        
   except Exception as err:
        with open("log.txt",'a') as file:
            now=datetime.datetime.now()
            now_stamp=now.strftime('%Y%m%d_%H%M%S')
            err_type = err.__class__.__name__ # 取得錯誤的class 名稱
            info = err.args[0] # 取得詳細內容
            detains = traceback.format_exc() # 取得完整的tracestack
            n1, n2, n3 = sys.exc_info() #取得Call Stack
            lastCallStack =  traceback.extract_tb(n3)[-1] # 取得Call Stack 最近一筆的內容
            fn = lastCallStack [0] # 取得發生事件的檔名
            lineNum = lastCallStack[1] # 取得發生事件的行數
            funcName = lastCallStack[2] # 取得發生事件的函數名稱
            errMesg = f"{now_stamp}\n FileName : {fn}, lineNum: {lineNum}, Fun: {funcName}, reason: {info}, trace:\n {traceback.format_exc()}\n"
            file.write(errMesg)

if __name__ == "__main__":
    run()
