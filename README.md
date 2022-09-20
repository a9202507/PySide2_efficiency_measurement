# PySide2_efficiency_measurement
## Users can measure voltage regulator efficiency through this GUI.

### equipments list
* Win10 or later
* Python 3.6.5 32bits( 64bits shoule be workable)
* Chroma DC source
* Agilent/Keysight 34970A Data Acquisition
* Chroma Eload 

### installation and setup
1. pip install -r requirements.txt
2. python main.py


### GUI setup
1. goes to setup page.
2. press rescan buttion to find all equipments.
3. select dcsource/DAQ/Eload equipment in the comboBox.
4. select DAQ's channel for Vin and Vout measurment.
5. goest to main page. and press on/off for DCsoucre for test
6. press on/off for Eload for test
7. press run efficinecy to do volage regulator efficinecy measurement.
8. open .xlsx file when the measurment completed.


