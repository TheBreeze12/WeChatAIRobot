from wxauto import WeChat
from listen import WxSender

# 初始化微信客户端
wx = WeChat()

# 创建微信自动回复对象（配置在config.py中）
wx_sender_obj = WxSender(wx)

print("🚀 微信AI自动回复已启动...")
print("📝 请先确保在config.py中配置了正确的API密钥和endpoint ID")
print("💬 开始监听微信消息...")

# 运行自动回复
wx_sender_obj.run()

del wx_sender_obj
 