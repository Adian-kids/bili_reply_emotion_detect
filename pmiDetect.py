import math
import json
from curdMysql import curdMysql



class pmiDetect:
    def __init__(self):
        self.mysql_connect = curdMysql().getConnect()
        self.mysql_cursor = self.mysql_connect.cursor()
        self.word_count = json.loads(open("wordCounts.json",'r').read())
        self.word_list = json.loads(open("wordList.json",'r').read())


    def getAllReply(self):
        self.reply_list = []
        mysql_sql_string = "SELECT content FROM reply"
        self.mysql_cursor.execute(mysql_sql_string)
        mysql_exec_result = self.mysql_cursor.fetchall()
        for single_result in mysql_exec_result:
            content = single_result[0]
            self.reply_list.append(content)
        self.detect()
        
    def PMI(self,word,W):
        both_time_conut = 0
        for reply in self.reply_list:
            reply = "评论" + reply
            if word in reply and W in reply:
                both_time_conut += 1
        df_value = (len(self.reply_list) * both_time_conut) / (self.word_count[word] * self.word_count[W])  
        pmi_value = math.log(2,df_value)
        return pmi_value

    def detect(self):
        sum_pmi_good = 0
        sum_pmi_bad = 0
        for key in self.word_list.keys():
            #print(type(self.word_list[key]))
            if self.word_list[key] == "1":
                print("good" + self.word_list[key])
                sum_pmi_good += self.PMI(key,"评论")
            elif self.word_list[key] == "-1":
                print("bad" + self.word_list[key])
                sum_pmi_bad += self.PMI(key,"评论")
        print("good"+str(sum_pmi_good))
        print("bad" + str(sum_pmi_bad))
        self.PMI_Preference = sum_pmi_good - sum_pmi_bad
        self.outputResult()

                    


    def outputResult(self):
        print(self.PMI_Preference)

a = pmiDetect()
a.getAllReply()
