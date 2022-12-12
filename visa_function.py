import pyvisa
import time
import pathlib
from datetime import datetime
rm = pyvisa.ResourceManager()


def get_visa_resource_list(remove_ASRL_devices=False):
    rm = pyvisa.ResourceManager()
    device_list = rm.list_resources()

    if remove_ASRL_devices == True:
        filtered = filter(lambda device: "ASRL" not in device, device_list)
        device_list = list(filtered)
    else:
        pass

    return device_list


def create_visa_equipment(resource_name):
    equipment = rm.open_resource(resource_name)

    return equipment


class visa_equipment():
    def __init__(self, visa_resource_name):
        self.visa_resource_name = visa_resource_name
        self.inst = pyvisa.ResourceManager().open_resource(self.visa_resource_name)
    '''
    def write(self, visa_str=""):
        self.inst.write(visa_str)

    def query(self, visa_str=""):
        self.inst.query(visa_str)
    '''

    def get_equipment_name(self):
        self.equipment_name = self.inst.query("*IDN?")
        return self.equipment_name


class agilentDAQ(visa_equipment):
    def __init__(self, visa_resource_name):
        visa_equipment.__init__(self, visa_resource_name)
        pass

    def read_channel_voltage(self, channel_number):
        self.voltage_value = self.inst.query(
            'MEAS:VOLT:DC? Auto,DEF,(@'+str(channel_number)+")")

    def get_voltage_result(self):
        return self.voltage_value

class agilent_visa_equipment(visa_equipment):
    def __init__(self, visa_resource_name):
        visa_equipment.__init__(self, visa_resource_name)
        

    def on(self):
        self.inst.write('OUTPUT:STATE ON')

    def off(self):
        self.inst.write('OUTPUT:STATE OFF')


class agilent_DCSource(agilent_visa_equipment):
    def __init__(self, visa_resource_name):
        agilent_visa_equipment.__init__(self, visa_resource_name)

    def set_voltage(self, voltage):
        self.inst.write(f'SOURce:VOLTage {voltage}')

    def set_current(self, current):
        self.inst.write(f'SOURce:CURRent {current}')

    def measure_voltage(self):
        self.measure_voltage_value = self.inst.query("MEAS:VOLT?")

    def measure_current(self):
        self.measure_current_value = self.inst.query("MEAS:CURR?")


class tek_visa_equipment(visa_equipment):
    def __init__(self, visa_resource_name):
        visa_equipment.__init__(self, visa_resource_name)

    def on(self):
        self.inst.write("OUTPut1:STATe ON")

    def off(self):
        self.inst.write("OUTPut1:STATe off")


class tek_visa_functionGen(tek_visa_equipment):
    def __init__(self, visa_resource_name, shape="PULS"):
        tek_visa_equipment.__init__(self, visa_resource_name)
        self.set_waveform_shape(shape)

    def set_freq(self, freq_khz):
        self.inst.write("SOURce1:FREQuency:FIXed "+str(freq_khz)+"kHz")

    def set_duty(self, duty):
        self.inst.write("SOURce1:PULSe:DCYCLe "+str(duty))

    def set_rise_time_ns(self, rise_time):
        self.inst.write("SOURce1:PULSe:TRANsition:LEADing " +
                        str(rise_time)+"ns")

    def set_fall_time_ns(self, fall_time):
        self.inst.write("SOURce1:PULSe:TRANsition:TRAiling " +
                        str(fall_time)+"ns")

    def set_waveform_shape(self, shape="PULS"):
        self.inst.write("SOURce1:FUNCtion:SHAPe "+shape)

    def set_voltage_high(self, voltage=0):
        self.inst.write("SOURce1:VOLTage:LEVel:IMMediate:High "+str(voltage))

    def set_voltage_low(self, voltage=0):
        self.inst.write("SOURce1:VOLTage:LEVel:IMMediate:Low "+str(voltage))

    def get_rise_time_ns(self):
        return self.inst.query("SOURce1:PULSe:TRANsition:LEADing?")


class tek_visa_mso_escope(visa_equipment):
    def __init__(self, visa_resource_name):
        visa_equipment.__init__(self, visa_resource_name)

    def save_waveform_in_inst(self, file_save_location_in_inst, filename, timestamp_enable=True, debug=False):
        self.file_save_path = pathlib.Path(file_save_location_in_inst)
        dt = datetime.now()
        if timestamp_enable == True:
            timestamp = dt.strftime("_%Y%m%d_%H%M%S")
            self.filename_in_inst = filename+timestamp
        else:
            self.filename_in_inst = filename
        self.filename_in_inst += ".png"
        self.filename_with_path_in_inst = "'" + \
            str(self.file_save_path / self.filename_in_inst) + "'"
        self.inst.write(('SAVE:IMAGe '+self.filename_with_path_in_inst))

        if debug == True:
            print(('SAVE:IMAGe '+self.filename_with_path_in_inst))

    def read_file_in_inst(self, inst_directory, filename):
        inst_direct_filename = inst_directory+"/"+filename
        self.inst.write(f"FileSystem:READFile '{inst_direct_filename}'")

    # TODO:
    def save_waveform_back_to_pc(self, inst_directory, filename, local_directory="./report/", debug=False):

        inst_direct_filename = inst_directory+"/"+filename
        if debug == True:
            print(f'save wavfrom:{inst_direct_filename}')
        self.inst.write(f"FileSystem:READFile '{inst_direct_filename}'")
        imgData = self.inst.read_raw(1024*1024)
        pc_dicrect_filename = local_directory+filename
        file = open(pc_dicrect_filename, "wb")
        file.write(imgData)
        file.close()
        return None

    def set_waveform_directory_in_scope(self, directory="E:/20220530"):
        self.inst.write(f"FILESystem:CWD '{directory}'")

    def get_waveform_directory_in_scope(self):
        directory = self.inst.query(f"FILESystem:CWD?")
        return directory

    def set_channel_measure_items(self):
        pass

    def get_measurement_value(self, item_number="1", measure_item_type="max"):
        measure_type_dict = {"max": "MAXIMUM",
                             "min": "MINIMUM",
                             "mean": "MEAN",
                             "value": "value", }
        result = self.inst.query(
            "MEASUrement:MEAS"+str(item_number)+":RESUlts:CURRentacq:"+measure_type_dict[measure_item_type]+"?")
        return result

    def set_horizontal_scale(self, scale="2e-6"):
        self.inst.write("HORIZONTAL:SCAlE "+scale)

    def set_trigger_level(self, trigger_level="1.0"):
        self.inst.write("TRIGger:A:level "+trigger_level)

    def set_trigger_channel(self, channel="CH1"):
        self.inst.write(f"TRIGger:A:EDGE:SOURCE {channel}")


def save_waveform_in_inst(visaRsrcAddr, fileSaveLocationInInst, filename, timestamp_enable=True, debug=False):
    rm = pyvisa.ResourceManager()
    scope = rm.open_resource(visaRsrcAddr)
    visaRsrcAddr = visaRsrcAddr
    fileSaveLocation2 = pathlib.Path(fileSaveLocationInInst)
    dt = datetime.now()
    timestamp = dt.strftime("MSO56_%Y%m%d_%H%M%S.png")
    if timestamp_enable == True:
        filename_in_inst = filename+timestamp
    else:
        filename_in_inst = filename

    rm = pyvisa.ResourceManager()
    scope = rm.open_resource(visaRsrcAddr)

    path_filename_in_inst = "'"+str(fileSaveLocation2 / filename_in_inst)+"'"
    scope.write('SAVE:IMAGe '+path_filename_in_inst)
    if debug == True:

        print(scope.query('*IDN?'))  # Print instrument id to console window

        print('SAVE:IMAGe '+path_filename_in_inst)
    scope.close()
    rm.close()

class gpibChromaMachine(visa_equipment):
    def __init__(self, visa_resource_name):
        visa_equipment.__init__(self, visa_resource_name)

    def on(self):
        self.inst.write("CONFigure:OUTPut ON")

    def off(self):
        self.inst.write("CONFigure:OUTPut OFF")


class gpibChromaDCSource(gpibChromaMachine):
    def __init__(self, visa_resource_name):
        gpibChromaMachine.__init__(self, visa_resource_name)

    def set_voltage(self, voltage):
        self.inst.write(f"SOUR:VOLT {voltage}")

    def set_current(self, current):
        self.inst.write(f"SOUR:CURR {current}")

    def measure_voltage(self):
        self.measure_voltage_value = self.inst.query("FETCh:VOLTage?")

    def measure_current(self):
        self.measure_current_value = self.inst.query('FETCh:CURRent?')


class chromaEload(gpibChromaMachine):
    def __init__(self, visa_resource_name):
        gpibChromaMachine.__init__(self, visa_resource_name)

    def run(self):
        self.inst.write("RUN")

    def abort(self):
        self.inst.write("Abort")

    def setCurrent(self, channel, current):
        self.current = current
        self.inst.write('CHAN '+str(channel))
        self.inst.write('CURR:STAT:L1 '+str(current))
        
    def getCurrentMeasurement(self):
        self.current_measurment=self.inst.query("FETCh:CURRent?")
        return self.current_measurment


if __name__ == '__main__':

    devices = get_visa_resource_list()
    print(devices)
    agilent_DC=agilent_DCSource(devices[3])
