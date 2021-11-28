import pymysql

class curdMysql:
    def __init__(self):
        self.host = "81.70.194.69"
        self.name = "emotion_detect"
        self.passwd = "emo" 
        self.dbname = "emotion_detect"
        self.charset = "utf-8"
        self.mysqlConnect = self.getConnect()
    def getConnect(self):
        mysqlConnect = pymysql.connect(
                host = self.host,
                user = self.name,
                password = self.passwd,
                db = self.dbname,
                )
        return mysqlConnect
    



a = curdMysql()

