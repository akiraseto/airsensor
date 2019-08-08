import sqlite3
from line_Notify import lineNotify

# データベースから取り出し
dbname = '/home/pi/airsensor/airsensor.db'
con = sqlite3.connect(dbname)
cur = con.cursor()
cur.execute('SELECT * FROM airsensor ORDER BY id DESC LIMIT 1')
latest = cur.fetchone()
con.close()

# LINEに通知
message = "\n気温:{0}*C\n湿度:{1}%\n不快指数:{2}p\n二酸化炭素:{3}ppm\n空気の汚れ:{4}ppb\n気圧:{5}hPa\n海抜:{6}m\n海面気圧:{7}hPa\n取得日:{8}"
message = message.format(latest[1], latest[2], latest[3], latest[4], latest[5], latest[6],  latest[7], latest[8],latest[9])

lineNotify(message)
print(message)
