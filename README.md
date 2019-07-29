# airsensor
空気の品質センサー

#必要モジュール

``
sudo pip3 install sparkfun-qwiic-i2c
``

qwiic_ccs811  
``
git clone https://github.com/sparkfun/Qwiic_CCS811_Py.git
python setup.py install
``

#i2c設定変更

``
sudo vi /boot/config.txt
dtparam=i2c_arm_baudrate=10000
``
