基于wxpy，在wbot基础上修改实现了对特定微信用户/微信群的自动回复、语音识别和转发。

语音识别基于Baidu Speech.

参考资料：

wxpy: https://github.com/youfou/wxpy

wBot: https://github.com/yaoyuan4102/wBot

百度云服务： https://console.bce.baidu.com/


需要ffmpeg支持，测试环境Python 2.7

除语音识别之外的功能，经过测试可以在Python3下正常使用


目前功能：
- 查看撤回信息： recalled_message_helper()
- 自动转发群信息： auto_forward_msg()
- 自动回复表情图： auto_reply_image()
- 自动导出关键字打卡: auto_daka()
- 语音助手（下载语音消息并识别）： voice_message_helper()， 目前仅限Python2

注意：
自动转发群信息、自动回复表情图、自动导出关键字打卡，这三个功能同时只有一个可以使用，否则会冲突。

启动：

	python runWBot.py
