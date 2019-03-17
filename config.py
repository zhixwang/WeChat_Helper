# -*- coding: utf-8 -*-

STORAGE_PATH = u'storage/'
MAX_HISTORY = 10000
MESSAGE_LENGTH = 150
TULING_API_KEY = u'aaaaaaaaaaaa'
TULING_URL = u'http://www.tuling123.com/openapi/api'
BAIDU_VOICE = {
    u'app_id': u'88888888',
    u'api_key': u'aaaaaaaaaaaaaaaa',
    u'secret_key': u'aaaaaaaaaaaaaaaaaaaaaaa'
}

INPUT_GROUP_NAME = [u'输入的群1',u'输入的群2',u'输入的群3']          # 监控的群名，用于 自动转发、打卡、自动回复等功能； 这些功能有时会冲突！
OUTPUT_GROUP_NAME = [u'输出的群1',u'输出的群2',u'输出的群3']	#turn off relating functoin: set this name to u''
FORWARD_TO_GROUP = True				#True: forward message to group(OUTPUT_GROUP_NAME), else: forward message to chat (OUTPUT_CHAT_NAME)
OUTPUT_CHAT_NAME = u'你自己'
COPY_TO_FILE_HELPER = False
DAKA_KEY_WORD = u'打卡'				#turn off relating functoin: set this name to u''
REPLY_KEY_WORD = u'笑一个'				# Key word for activate auto reply image; listenint to INPUT_GROUP_NAME as well, #turn off relating functoin: set this name to u''