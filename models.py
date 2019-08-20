# coding: utf-8
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date
from database import Base
from datetime import datetime as dt

#Table情報
class Data(Base):
    #TableNameの設定
    __tablename__ = "airsensor"
    #Column情報を設定する
    id = Column(Integer, primary_key=True, autoincrement=True)
    temp = Column(Integer, unique=False)
    humi = Column(Integer, unique=False)
    di = Column(Integer, unique=False)
    co2 = Column(Integer, unique=False)
    tvoc = Column(Integer, unique=False)
    press = Column(Integer, unique=False)
    alti = Column(Integer, unique=False)
    sea = Column(Integer, unique=False)
    date = Column(String, unique=False)

def __init__(self, id=None, temp=None, humi=None, di=None, co2=None, tvoc=None, press=None, alti=None, sea=None, date=None):
        self.id = id
        self.temp = temp
        self.humi = humi
        self.di = di
        self.co2 = co2
        self.tvoc = tvoc
        self.press = press
        self.alti = alti
        self.sea = sea
        self.date = date
