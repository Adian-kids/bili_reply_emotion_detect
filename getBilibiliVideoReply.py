import requests
import json
import curdMysql

class getBilibiliVideoReply:
    '''
    根据oid获取视频评论区
    @params string oid
    @return list result_list
    '''
    def __init__(self):
        print("-->Crawler init")
        self.SESSDATA = "90a31abd%2C165101%2C467c3%2Ab1"
        self.bili_jct = "5a7b48fb937a757a0dd2a73d54c"
        self.DedeUserId = "179450"
        self.DedeUserId_ckMd5 = "1ba7d100de029d"

    def getReply(self,oid):
        for page in range(1,10):
            topic_url ="http://api.bilibili.com/x/v2/reply?type=1&ps=49&oid=" + oid + "&pn=" + str(page)
            mysql_connect = curdMysql.curdMysql().getConnect()
            mysql_cursor = mysql_connect.cursor()
            requests_result = requests.get(topic_url)
            #print(requests_result.status_code)
            #print(requests_result.content)

            result_json = json.loads(requests_result.content)
            reply_list = result_json.get("data").get("replies")
            for reply in reply_list:
                mysql_sql_string = "INSERT INTO reply (content) VALUES ('"+ reply.get("content").get("message") + "')"
                mysql_cursor.execute(mysql_sql_string)
                mysql_connect.commit()
                print("-->get reply " + reply.get("content").get("message"))


if __name__=='__main__':
    reply = getBilibiliVideoReply()
    reply.getReply("806854032")
