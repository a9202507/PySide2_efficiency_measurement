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

# set icon to taskbar
import ctypes
myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class efficiency_measure_thread(QThread):

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
        #iout_list = [1, 2, 3, 4, 5]
        for iout in iout_list:
            myWin.push_msg_to_GUI(f"Iout={iout}")
            myWin.eload.abort()
            time.sleep(cooldown_time)
            myWin.eload.setCurrent(9, iout)
            myWin.eload.run()
            time.sleep(duration_time)
            myWin.get_all_daq_value_once()

        myWin.eload.abort()

        myWin.push_msg_to_GUI("completed")

    def stop(self):
        self.terminate()
        pass
    '''
        self.DB410_msg.emit("==3D test stop==")
        self.DB410_msg.emit(" ")
        self.DB410_process_bar.emit(0)
        # todo
        self.terminate()
    '''
    pass


'''

class DB410_3d_thread(QThread): 
    DB410_msg = Signal(str)
    DB410_process_bar = Signal(int)

    def __init__(self):
        QThread.__init__(self)

        # self.DB410_msg = Signal(str)

    def __del__(self):
        self.wait()

    def run(self):
        self.DB410_msg.emit("== start to run 3D test==")
        myWin.update_GUI()
        myWin.init_scope()

        freq_list_len = len(myWin.parameter_main_freq_list)
        duty_list_len = len(myWin.parameter_main_duty_list)
        measure_result_dict = dict()
        df = pd.DataFrame()
                    
        base_filename = "IFX_"
        for freq_idx, freq in enumerate(myWin.parameter_main_freq_list):
            for duty_idx, duty in enumerate(myWin.parameter_main_duty_list):

                self.DB410_msg.emit(f"Freq={str(freq)}, Duty={str(duty)}")
                self.DB410_process_bar.emit(
                    int((duty_idx+freq_idx*duty_list_len)/(freq_list_len*duty_list_len)*100))

                # scope horizontal scale
                myWin.set_horizontal_scale_in_scope(str(1/(freq*1000)))

                myWin.send_function_gen_command_one_time(freq, duty, True)

                # for transinet duration time.
                time.sleep(myWin.parameter_main_ton_duration_time_sec)
                dt = datetime.datetime.now()
                timestamp_str = dt.strftime("_%Y%m%d_%H%M%S")
                filename = base_filename+str(myWin.parameter_main_high_current)+"A_"+str(
                    myWin.parameter_main_low_current)+"A_"+"Gain"+str(myWin.parameter_main_gain)+"mVa"+"_"+str(freq)+"Khz"+"_D"+str(duty)+timestamp_str

                print(f"line65 filename={filename}")
                myWin.lineEdit_7.setText(filename)
                try:
                    myWin.update_GUI_then_save_waveform_once_time()

                except:
                    myWin.push_msg_to_GUI("Failed to save waveform to Scope")

                if myWin.debug == True:
                    myWin.push_msg_to_GUI("save_file_to_PC")

                try:
                    myWin.save_wavefrom_from_scope_to_pc(filename)
                except:
                    myWin.push_msg_to_GUI("Failed to save waveform to PC")
                # for save wavefrom delay time
                # myWin.scope.inst.query('*OPC?')
                time.sleep(1)

            
                measure_result_dict['Freq'] = float(freq)
                measure_result_dict['duty'] = float(duty)
                vmax=myWin.get_scope_meansurement_value('1', "mean")
                print(f"line88 vmax={vmax}")
                measure_result_dict['Vmax'] = float(vmax)

                #
                #except:
                #    myWin.push_msg_to_GUI(f"Failed to get measurement from scope , Vmax={vmax}")

                
                vmin=myWin.get_scope_meansurement_value('2', "mean")
                print(f"line97 vmin={vmin}")
                measure_result_dict['Vmin'] = vmin
                
                #
                #except:
                #    myWin.push_msg_to_GUI(f"Failed to get measurement from scope , Vmin={vmin}")

                df = df.append(measure_result_dict, ignore_index=True)

                if myWin.debug == True:
                    self.DB410_msg.emit(str(measure_result_dict))
                    print(f"df={df}")
                time.sleep(0.2)

                myWin.send_function_gen_command_one_time(freq, duty, False)

                # for transient off duration time
                time.sleep(myWin.parameter_main_toff_duration_time_sec)
        self.DB410_process_bar.emit(100)

        try:
            df.to_excel(
                f"{myWin.lineEdit_27.text()}/{myWin.lineEdit_7.text()}{myWin.parameter_main_high_current}A_{myWin.parameter_main_low_current}A_report_{datetime.datetime.now().strftime('%Y_%m%d_%H%M')}.xls")
        except:
            myWin.push_msg_to_GUI("Failed to save report to PC")
        self.DB410_msg.emit("==3D test finish==")
        self.DB410_msg.emit(" ")

    def stop(self):
        self.DB410_msg.emit("==3D test stop==")
        self.DB410_msg.emit(" ")
        self.DB410_process_bar.emit(0)
        # todo
        self.terminate()
'''


class MyMainWindow(QMainWindow, efficiency_ui.Ui_MainWindow):
    def __init__(self, parent=None, debug=True):
        super(MyMainWindow, self).__init__(parent)
        self.setFixedSize(730, 850)
        self.setupUi(self)
        self.debug = debug

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

        self.DAQ.read_channel_voltage(self.comboBox_2.currentText())
        self.vout_measurement_value = float(self.DAQ.get_voltage_result())
        self.DAQ.read_channel_voltage(self.comboBox_4.currentText())
        self.vin_measurement_value = float(self.DAQ.get_voltage_result())
        self.dcsource.measure_current()
        self.iin_measurement_value = float(self.dcsource.measure_current_value)

        self.push_msg_to_GUI(
            f"line139 vout={self.vout_measurement_value},vin={self.vin_measurement_value},Iin={self.iin_measurement_value}")

    def abort_efficiency_measurement(self):
        self.efficiency_measurement_thread.stop()

    def run_efficiency_measurement(self, iout_list=0, cooldown_time=2, duration_time=2):

        self.efficiency_measurement_thread.start()
        '''
        iout_list = [1, 2, 3, 4, 5]
        self.eload = myvisa.chromaEload(self.comboBox_3.currentText())
        for iout in iout_list:
            self.eload.abort()
            time.sleep(cooldown_time)
            self.eload.setCurrent(9, iout)
            self.eload.run()
            time.sleep(duration_time)
            self.get_all_daq_value_once()

        self.eload.abort()
        '''
        pass

        '''
        # self.pushButton_8.clicked.connect(self.create_visa_equipment)
        self.pushButton_8.clicked.connect(self.run_function_gen_3d_thread)
        self.pushButton_4.clicked.connect(self.stop_function_gen_3d_thread)
        self.pushButton_6.clicked.connect(self.update_equipment_on_combox)
        self.pushButton_5.clicked.connect(self.clear_message_box)
        self.comboBox_2.currentIndexChanged.connect(
            self.update_function_gen_name)
        self.comboBox.currentIndexChanged.connect(
            self.update_escope_name)
        self.pushButton_9.clicked.connect(self.open_3d_report_max)
        self.pushButton_9.setText("load 3D report")

        self.pushButton_10.setText("init Scope")
        self.pushButton_10.clicked.connect(self.check_debug_mode)

        self.pushButton_7.clicked.connect(
            self.update_GUI_then_save_waveform_once_time)
        self.pushButton_7.setEnabled(False)
        
        self.actionLoad_config.triggered.connect(self.load_config)
        self.actionSave_config.triggered.connect(self.save_config)
        self.actionAbout_the_GUI.triggered.connect(self.about_the_GUI)
        self.about_the_gui_text = "Powered by PySide2 and Python3. \n https://github.com/a9202507/ifx_loadslammer"
        self.debug = debug
        # set off_RadioButton is checked.
        self.radioButton_2.setChecked(True)
        self.pushButton_11.clicked.connect(self.select_directory)

        # start-up function
        self.update_equipment_on_combox()

        # set auto load init.json during startup
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.path_file_list = list()
        self.path_file_list.append(self.path+"\init.json")
        self.load_config_from_filename(self.path_file_list)

        # functionGen
        self.radioButton.toggled.connect(
            self.update_GUI_then_send_to_function_gen_on)
        self.radioButton_2.toggled.connect(
            self.update_GUI_then_send_to_function_gen_off)

        # initial thread
        self.function_gen_3d = DB410_3d_thread()
        self.function_gen_3d.DB410_msg.connect(self.push_msg_to_GUI)
        self.function_gen_3d.DB410_process_bar.connect(self.set_process_bar)

        # set windowTitle
        self.Window_title = "IFX loadSlammer GUI Rev.2022.06.17"

        # set icon
        app_icon = QIcon()
        app_icon.addFile("./resource/load slammer.ico")
        self.setWindowIcon(app_icon)

        self.set_window_title_with_debug_mode()

    def set_window_title_with_debug_mode(self):
        if self.debug == True:
            self.setWindowTitle(self.Window_title+"_Debug mode")
        else:
            self.setWindowTitle(self.Window_title)

    def check_debug_mode(self):
        self.update_GUI()
        self.init_scope()

        if self.lineEdit_7.text() == "53523962":
            self.set_debug_mode_enable(True)
            self.push_msg_to_GUI(f"debug is {self.debug}")
        else:
            self.set_debug_mode_enable(False)
        self.pushButton_7.setEnabled(True)
    def set_debug_mode_enable(self, mode=False):
        self.debug = mode
        self.set_window_title_with_debug_mode()

    def update_GUI_then_save_waveform_once_time(self):

        self.parameter_setting_folder_in_inst = self.lineEdit_26.text()
        self.parameter_setting_filename = self.lineEdit_7.text()
        self.save_waveform_in_scope(self.parameter_setting_folder_in_inst,
                                    self.parameter_setting_filename, False)
        time.sleep(1)
        #self.save_wavefrom_from_scope_to_pc(
        #    self.waveform_file, self.parameter_setting_filename_include_timestamp)

    def init_scope(self):
        self.scope = myvisa.tek_visa_mso_escope(
            self.parameter_setting_scope_resource_name)

    def save_waveform_in_scope(self, filefolder, filename, timestamp=True):
        self.init_scope()

        # set waveform dirctory in scope
        self.scope.set_waveform_directory_in_scope(self.lineEdit_26.text())

        if timestamp == True:
            dt = datetime.datetime.now()
            timestamp_str = dt.strftime("_%Y%m%d_%H%M%S")
            self.waveform_file = filename+timestamp_str
        else:
            self.waveform_file = filename

        # save waveform
        if self.debug == True:
            self.push_msg_to_GUI(
                f"save waveform as: {filefolder}, {self.waveform_file}")

        self.scope.save_waveform_in_inst(filefolder, self.waveform_file, False)

        # read waveform back to check save funciton success.
        self.scope.read_file_in_inst(filefolder, self.waveform_file+".png")

    # comment out as below line for MSO58, 20220609
        # self.scope.inst.read_raw(1024*1024)

    def save_wavefrom_from_scope_to_pc(self, filename, debug=True):
        local_fildfolder = self.lineEdit_26.text()
        self.scope.save_waveform_back_to_pc(
            local_fildfolder, self.waveform_file+".png", self.lineEdit_27.text()+"/", self.debug)

    def get_scope_meansurement_value(self, item_number=1, measure_item_type="max"):
        result = self.scope.get_measurement_value(str(item_number), measure_item_type)
        return result

    def set_process_bar(self, data):
        self.progressBar.setValue(data)

    def run_function_gen_3d_thread(self):
        # self.push_msg_to_GUI("run function gen 3d")
        self.update_GUI()
        if self.comboBox_2.currentText() == "" or self.comboBox.currentText() == "":
            QMessageBox.about(
                self, "error", "please check equipment setting on Setting page")
        else:
            self.function_gen_3d.start()
        # self.myprogpressbar.start()

    def stop_function_gen_3d_thread(self):
        self.function_gen_3d.stop()
        # self.push_msg_to_GUI("stop the 3d test")

    def run_function_gen(self, function_gen_resource_name, high_voltage, low_voltage, freq, duty, rise_time, fall_time, on_off=False):
        self.function_gen = myvisa.tek_visa_functionGen(
            self.comboBox_2.currentText())
        # self.function_gen.set_voltage_high = high_voltage
        # self.function_gen.set_voltage_low = low_voltage
        self.function_gen.set_freq = str(freq)
        self.function_gen.set_duty = str(duty)
        self.function_gen.set_rise_time_ns = str(rise_time)
        self.function_gen.set_fall_time_ns = str(fall_time)

        if self.debug == True:
            print(
                f"run_function_gen freq{freq}duty{duty}rise{rise_time}fala{fall_time}")

        if on_off == True:
            self.function_gen.on()
        else:
            self.function_gen.off()

    def update_GUI_then_send_function_gen(self):
        self.update_GUI()
        self.send_function_gen_command_one_time(
            self.lineEdit_8.text(), self.lineEdit_5.text(), self.comboBox_3.currentIndex())

    def update_GUI_then_send_to_function_gen_on(self):
        if self.comboBox_2.currentText() == "":
            QMessageBox.about(
                self, "error", "please select fucntion get on Setting page first")
        else:
            self.update_GUI_then_send_to_function_gen(
                function_output_enable=True)

    def update_GUI_then_send_to_function_gen_off(self):
        if self.comboBox_2.currentText() != "":
            self.update_GUI_then_send_to_function_gen(
                function_output_enable=False)

    def update_GUI_then_send_to_function_gen(self, function_output_enable):
        self.update_GUI()
        self.send_function_gen_command_one_time(self.lineEdit_8.text(
        ), self.lineEdit_5.text(), function_output_enable)

    def send_function_gen_command_one_time(self, freq, duty, on_off=False):
        self.function_gen = myvisa.tek_visa_functionGen(
            self.comboBox_2.currentText())
        self.function_gen.set_duty(duty)
        self.function_gen.set_freq(freq)

        high_voltage_value = float(
            self.lineEdit_16.text())*float(self.lineEdit_17.text())/1000
        low_voltage_value = float(self.lineEdit.text()) * \
            float(self.lineEdit_17.text())/1000
        self.function_gen.set_voltage_high(str(high_voltage_value))
        self.function_gen.set_voltage_low(str(low_voltage_value))
        self.function_gen.set_rise_time_ns(self.lineEdit_6.text())
        self.function_gen.set_fall_time_ns(self.lineEdit_4.text())

        if on_off == True:
            self.function_gen.on()
        else:
            self.function_gen.off()

    def create_visa_equipment(self):
        if self.comboBox.currentText() != "":

            self.escope = myvisa.create_visa_equipment(
                self.comboBox.currentText())
            message = self.escope.query('*IDN?')
            if self.debug == True:
                self.push_msg_to_GUI(message)

    def update_equipment_on_combox(self):
        self.get_visa_resource()
        self.comboBox.clear()
        self.lineEdit_28.clear()
        self.comboBox_2.clear()
        self.lineEdit_29.clear()
        self.comboBox.addItem("")
        self.comboBox.addItems(self.resource_list)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItems(self.resource_list)

    def get_visa_resource(self):

        self.resource_list = myvisa.get_visa_resource_list(
            not self.debug)
        if self.debug == True:
            self.push_msg_to_GUI(self.resource_list)

    def push_msg_to_GUI(self, msg=""):
        if True:
            self.textEdit.append(str(msg))
            # self.textEdit.append("")
        else:
            pass

    def save_config(self):
        self.update_GUI()
        self.parameter_dict = {"parameter_main_high_current": self.parameter_main_high_current,
                               "parameter_main_low_current": self.parameter_main_low_current,
                               "parameter_main_gain": self.parameter_main_gain,
                               "parameter_main_rise_time_nsec": self.parameter_main_rise_time_nsec,
                               "parameter_main_fall_time_nsec": self.parameter_main_fall_time_nsec,
                               "parameter_main_duty": self.parameter_main_duty,
                               "parameter_main_frequency": self.parameter_main_frequency,
                               # ===========================================================
                               "parameter_main_duty_list": self.parameter_main_duty_list,
                               "parameter_main_freq_list": self.parameter_main_freq_list,
                               "parameter_main_ton_duration_time_sec": self.parameter_main_ton_duration_time_sec,
                               "parameter_main_toff_duration_time_sec": self.parameter_main_toff_duration_time_sec,
                               "parameter_main_roll_up_down_enable": self.parameter_main_roll_up_down_enable,
                               # ===========================================================
                               "parameter_setting_scope_resource_name": self.parameter_setting_scope_resource_name,
                               "parameter_setting_function_gen_resource_name": self.parameter_setting_function_gen_resource_name,
                               "parameter_setting_folder_in_inst": self.parameter_setting_folder_in_inst,
                               "parameter_setting_filename": self.parameter_setting_filename,
                               "parameter_setting_filename_include_timestamp": self.parameter_setting_filename_include_timestamp,
                               "parameter_setting_filename_include_transient": self.parameter_setting_filename_include_transient,
                               }
        filename_with_path = QFileDialog.getSaveFileName(
            self, 'Save File', '.', 'JSON Files (*.json)')
        save_filename = filename_with_path[0]
        if save_filename != "":
            with open(save_filename, 'w') as fp:
                # json.dump(self.parameter_dict, fp)
                fp.write(json.dumps(self.parameter_dict, indent=4))

        if self.debug == True:
            self.push_msg_to_GUI(self.parameter_dict)

    def load_config(self):

        self.get_filename()
        # print(self.filenames[0])
        self.load_config_from_filename(self.filenames)

    def get_filename(self):
        try:
            dlg = QFileDialog(self, 'Open File', '.',
                              'JSON Files (*.json);;XLS Files (*.xls);;All Files (*)')
            if dlg.exec_():
                self.filenames = dlg.selectedFiles()
                if self.debug == True:
                    self.push_msg_to_GUI(self.filenames)

        except:
            QMessageBox.about(self, "Warning", "the filename isn't work")

    def load_config_from_filename(self, filenames):

        with open(filenames[0], 'r') as j:
            json_data = json.load(j)
            if self.debug == True:
                self.push_msg_to_GUI(str(json_data))

            self.lineEdit_16.setText(
                str(json_data["parameter_main_high_current"]))
            self.lineEdit.setText(str(json_data["parameter_main_low_current"]))
            self.lineEdit_17.setText(str(json_data["parameter_main_gain"]))
            self.lineEdit_6.setText(str(
                json_data["parameter_main_rise_time_nsec"]))
            self.lineEdit_4.setText(str(
                json_data["parameter_main_fall_time_nsec"]))
            self.lineEdit_5.setText(str(json_data["parameter_main_duty"]))
            self.lineEdit_8.setText(str(json_data["parameter_main_frequency"]))
            # =============================
            self.lineEdit_13.setText(
                str(json_data["parameter_main_duty_list"])[1:-1])
            self.lineEdit_15.setText(
                str(json_data["parameter_main_freq_list"])[1:-1])
            self.lineEdit_21.setText(str(
                json_data["parameter_main_ton_duration_time_sec"]))
            self.lineEdit_22.setText(str(
                json_data["parameter_main_toff_duration_time_sec"]))
            self.checkBox_3.setChecked(
                json_data["parameter_main_roll_up_down_enable"])
            # ==================================
            self.lineEdit_26.setText(
                json_data["parameter_setting_folder_in_inst"])
            self.lineEdit_7.setText(
                str(json_data["parameter_setting_filename"]))
            self.checkBox_2.setChecked(
                json_data["parameter_setting_filename_include_timestamp"])

    def about_the_GUI(self):
        QMessageBox.about(self, "about the GUI", self.about_the_gui_text)

    def update_GUI(self):
        # get GUI import
        # main page
        self.parameter_main_high_current = float(self.lineEdit_16.text())
        self.parameter_main_low_current = float(self.lineEdit.text())
        self.parameter_main_gain = float(self.lineEdit_17.text())
        self.parameter_main_rise_time_nsec = float(self.lineEdit_6.text())
        self.parameter_main_fall_time_nsec = float(self.lineEdit_4.text())
        self.parameter_main_duty = float(self.lineEdit_5.text())
        self.parameter_main_frequency = float(self.lineEdit_8.text())

        # ======
        self.parameter_main_duty_list = eval(
            "["+str(self.lineEdit_13.text())+"]")

        self.parameter_main_freq_list = eval(
            "["+str(self.lineEdit_15.text())+"]")
        self.parameter_main_ton_duration_time_sec = float(
            self.lineEdit_21.text())
        self.parameter_main_toff_duration_time_sec = float(
            self.lineEdit_22.text())
        self.parameter_main_roll_up_down_enable = self.checkBox_3.isChecked()

        # setting page
        self.parameter_setting_function_gen_resource_name = self.comboBox_2.currentText()
        self.parameter_setting_scope_resource_name = self.comboBox.currentText()
        self.parameter_setting_folder_in_inst = self.lineEdit_26.text()
        self.parameter_setting_filename = self.lineEdit_7.text()
        self.parameter_setting_filename_include_timestamp = self.checkBox_2.isChecked()
        self.parameter_setting_filename_include_transient = self.checkBox.isChecked()

    def update_function_gen_name(self):
        if self.comboBox_2.currentText() != "":
            self.function_gen = myvisa.tek_visa_functionGen(
                self.comboBox_2.currentText())
            device_name = self.function_gen.get_equipment_name()
            self.lineEdit_29.setText(device_name)

    def update_escope_name(self):
        if self.comboBox.currentText() != "":
            self.function_gen = myvisa.tek_visa_functionGen(
                self.comboBox.currentText())
            device_name = self.function_gen.get_equipment_name()
            self.lineEdit_28.setText(device_name)

    def set_horizontal_scale_in_scope(self, scale_value="1e-6"):
        self.scope.set_horizontal_scale(scale_value)

    def clear_message_box(self):
        self.textEdit.clear()

    def open_3d_report_max(self):
        self.get_filename()

        if self.debug == True:
            print(self.filenames[0])
        pandas_report.plt_vmax(self.filenames[0])

    def select_directory(self):
        self.dir_path = QFileDialog.getExistingDirectory(
            self, "Chose Directory", "./")
        self.lineEdit_27.setText(self.dir_path)
'''


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWin = MyMainWindow(debug=True)

    myWin.show()

    sys.exit(app.exec_())
