# airsensor

## CO2、TVOCセンサー
### CCS811
- CO2濃度取得
- TVOC（空気の汚れ具合）取得  

必要モジュール  
``
sudo pip3 install sparkfun-qwiic-i2c
``

qwiic_ccs811  
``
git clone https://github.com/sparkfun/Qwiic_CCS811_Py.git
python setup.py install
``

i2c設定変更  
``
sudo vi /boot/config.txt
dtparam=i2c_arm_baudrate=10000
``

## 大気圧センサー
### BMP180
- TEMP 気温
- Pressure 気圧（パスカル）
- Altitude 高度
- Sealevel Pressure 海面気圧

必要モジュール  
``
git clone https://github.com/adafruit/Adafruit_Python_BMP.git
cd Adafruit_Python_BMP
sudo python3 setup.py install
``

## 気温、湿度センサー
### DHT11
- TEMP 気温
- Humidity 湿度

必要モジュール  
``
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python3 setup.py install
``
