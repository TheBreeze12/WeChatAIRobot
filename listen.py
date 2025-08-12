from wxauto.msgs import FriendMessage
from config import AI_CONFIG, WECHAT_CONFIG, GENERAL_CONFIG
from openai import OpenAI
from ai import AI

class WxSender():
    def __init__(self, wx, msg_dic=None):
        
        self.wx = wx
        self.ai=AI( AI_CONFIG["api_key"], AI_CONFIG["api_url"],\
            AI_CONFIG["endpoint_id"],AI_CONFIG["system_prompt"])
        self.msg_dic = msg_dic or WECHAT_CONFIG["listen_contacts"]
        self.reply_prefix = WECHAT_CONFIG["reply_prefix"]
        self.debug_mode = GENERAL_CONFIG["debug_mode"]
        for person in self.msg_dic:
            self.wx.SendMsg("你好,AI助手开始工作了", who=person)

    def on_message(self, msg, chat):
        if isinstance(msg, FriendMessage):
            msg_type = msg.type
            msg_content = msg.content
            
            if self.debug_mode:
                print(f"收到消息: {msg_content}, 消息类型: {msg_type}")
            
            if msg_content == '':
                smsg = '对不起，我无法理解您的问题'
            else:
                try:
                    smsg = self.ai.get_response(chat.who,msg_content)
                except Exception as e:
                    if self.debug_mode:
                        print(f"API调用失败: {e}")
                    smsg = '抱歉，AI服务暂时不可用'
            
            msg.quote(self.reply_prefix + smsg)
    
    def run(self):
        print(self.msg_dic)
        for person in self.msg_dic:
            self.wx.AddListenChat(nickname=person, callback=self.on_message)

        self.wx.KeepRunning()
