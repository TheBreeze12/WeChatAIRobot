AI_CONFIG = {
    "api_key": "sk-5fa67bd7ccd445bbaaea7f2ff1d54b66", 
    "endpoint_id": "deepseek-chat",  # 你的模型endpoint ID
    "api_url": "https://api.deepseek.com",
    "model_name": "deepseek-1",
    "temperature": 0.7,  # 控制回答的随机性 (0-1)
    "max_tokens": 500,   # 最大回答长度
    "system_prompt":"你是一个友善、有用的助手，请用简洁明了的中文回答用户的问题。"
}

# ========== 微信监听配置 ==========
WECHAT_CONFIG = {
    "listen_contacts": ["龙"],  # 要监听的微信联系人昵称列表
    "reply_prefix": "AI回答：",  # 回复消息前缀
}

# ========== 其他配置 ==========
GENERAL_CONFIG = {
    "debug_mode": True,  # 是否开启调试模式
    "retry_times": 3,    # API调用失败重试次数
    "timeout": 30,       # API请求超时时间(秒)
}