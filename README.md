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

### 数値の目安
#### ＜おおまかな二酸化炭素濃度の目安＞
- 350～450ppm　　 過剰な換気（外気：330～400ppm）
- 450～700ppm　　 理想的な換気レベル
- 700～1000ppm　　換気が不十分（室内では1000ppm以下に抑えることとされている※）
- 1000～1500ppm　 悪い室内空気環境（学校環境では1500ppm以下が望ましいとされいる）
- 1500～5000ppm　 これ以上の環境で労働をしてはいけない（労働安全基準法では、5000ppmが限度）
- 5000ppm以上　　　疲労集中力の欠如（締め切った車の中は、5000ppm以上になることもあるらしい）  
※建築物衛生法、建築基準法、労働安全衛生法

#### ＜人体への影響＞
- 1000ppm: 思考力に影響し始める
- 2000ppm: 眠気を感じる人が出てくる
- 3000ppm: 肩こりや頭痛を感じる人が出てくる
- 3000ppm以上: 集中力や意思決定に支障をきたす  

研究者らによると、「室内の二酸化炭素濃度が2500ppmや3000ppmに達したとしても決して健康に害があるわけではないが、集中力や意思決定に支障をきたす可能性があることは明らかになった」とのこと。

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

### 数値の目安
標準大気圧:1013.25 hPa＝1気圧


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

### 数値の目安

#### 熱中症
温度:28C以上 湿度:70％以上で危険

#### インフルエンザ
湿度50％以上でウイルス激減

#### 不快指数
ざっくり
- 70以上は一般的に不快で
- 75以上で半数の人が不快
- 85以上でほとんどの人が不快

こまかく
- ~55:  寒い
- 55~60:肌寒い
- 60~65:何も感じない
- 65~70:快い
- 70~75:暑くない
- 75~80:やや暑い
- 80~85:暑くて汗が出る
- 85~:  暑くてたまらない

不快指数がDI（Tは乾球気温℃、Hは湿度％）  
DI=0.81T + 0.01H x (0.99T-14.3)+46.3
