from getBilibiliVideoReply import getBilibiliVideoReply
from jiebaGetSingleWord import jiebaGetSingleWord

if __name__ == '__main__':
    get_reply = getBilibiliVideoReply()
    get_reply.getReply("806854032")
    jieba_word  = jiebaGetSingleWord()
    jieba_word.getReplyFromMysql()
