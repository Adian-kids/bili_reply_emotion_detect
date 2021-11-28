import pymysql
import jieba
import json
import curdMysql
import paddle
paddle.enable_static()

class jiebaGetSingleWord:
    '''
    通过调用jieba库，实现中文分词和频次分析
    @params null
    @return file_IO
    '''
    def __init__(self):
        # init mysql connector
        self.mysql_connect = curdMysql.curdMysql().getConnect()
        self.mysql_cursor = self.mysql_connect.cursor()

    def getReplyFromMysql(self):
        output_list = []
        mysql_sql_string = "SELECT content FROM reply"
        self.mysql_cursor.execute(mysql_sql_string)
        mysql_exec_result = self.mysql_cursor.fetchall()
        jieba.enable_paddle()
        for single_result in mysql_exec_result:
            content = single_result[0]
            word_list = jieba.lcut(content)
            for word in word_list:
                output_list.append(word)
        self.outputJson(output_list)

    def outputJson(self,word_list):
        data = {"sum":str(len(word_list))}
        # json for counts
        for word in word_list:
            if not data.__contains__(word):
                data[word] = word_list.count(word)
        json_file = open("wordCounts.json","w+",encoding='utf-8')
        json_file.write(json.dumps(data,ensure_ascii=False))
        json_file.close()

        # json just for word list
        data = {}
        for word in word_list:
            if not data.__contains__(word):
                data[word] = "0"
        json_file = open("wordList.json","w+",encoding='utf-8')
        json_file.write(json.dumps(data,ensure_ascii=False))
        json_file.close()
        

a = jiebaGetSingleWord()
a.getReplyFromMysql()
