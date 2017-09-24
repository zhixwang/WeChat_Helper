# -*- coding: utf-8 -*-
from wxpy import *
from aip import AipSpeech
import config as config
import os
import requests
import random
import re


class WBot(object):
    def __init__(self):
        self.bot = Bot()
        self.bot.enable_puid()
        self.bot.messages.max_history = config.MAX_HISTORY
        self.aipSpeech = AipSpeech(
            config.BAIDU_VOICE[u'app_id'],
            config.BAIDU_VOICE[u'api_key'],
            config.BAIDU_VOICE[u'secret_key']
        )
        self.input=self.bot.groups().search(config.INPUT_CHAT_NAME)[0]      # 默认输入源类型是微信群
        self.output=self.bot.friends().search(config.OUTPUT_CHAT_NAME)[0]   # 默认将转录的文字内容发给特定好友

    def run(self):
        self.output.send(u'机器人建立:')
        self.input.send(u'讲座开始：')
        self.voice_message_helper()
        embed()


    ### Multimedia Message Process ###
    def voice_message_helper(self):
        """
        对语音消息进行处理
        
        :return: 
        """
        @self.bot.register(chats=self.input,msg_types=RECORDING)
        def auto_process(msg):
            self.output.send(u'收到一条语音：')
            file_path = self._download_attachment(msg, RECORDING)
            if file_path:
                audio_path = self._audio_conversion(file_path)
                if os.path.isfile(audio_path):
                    response = self.aipSpeech.asr(self._get_file_content(audio_path), 'wav', 8000, {
                        'lan': 'zh',
                    })
                    res_msg = self._next_topic()
                    if response[u'err_no'] == 0:
                        text = response[u'result'][0]
                        self.output.send(text)
                        if config.COPY_TO_FILE_HELPER == True:
                            self.bot.file_helper.send(text)


    def _download_attachment(self, msg, msg_type):
        """
        下载文件到对应文件夹
        
        :param msg: 
        :param msg_type: 
        :return: 
        """
        file_path = self._get_storage_path(msg, msg_type)
        msg.get_file(save_path=file_path)
        if os.path.isfile(file_path) and os.path.getsize(file_path) > 0:
            return file_path
        else:
            self.output.send('os.path.isfile(file_path) and os.path.getsize(file_path) < 0')
            return None

    @staticmethod
    def _get_storage_path(msg, msg_type):
        """
        Get File Path
        
        :param msg: 
        :param msg_type: 
        :return: 
        """
        puid = msg.sender.puid if msg.sender.puid else u'other'
        path = config.STORAGE_PATH + msg_type.lower()# + u'/' + puid
        absolute_path = os.getcwd()
        if path:
            path_list = path.split(u'/')
            for folder in path_list:
                absolute_path = absolute_path + u'/' + folder
                if not os.path.exists(absolute_path):
                    os.makedirs(absolute_path)
            absolute_path = absolute_path + u'/' + msg.file_name
        return absolute_path

    @staticmethod
    def _audio_conversion(path, audio_format='.wav', sample_rate='8000'):
        """
        Audio Conversion
        
        :param path: 
        :return: 
        """
        filename, file_extension = os.path.splitext(path)
        audio_path = filename + audio_format
        conversion_command = u'ffmpeg -i ' + path + u' -acodec pcm_s16le -ar ' + sample_rate + u' ' + audio_path
        os.system(conversion_command)

        return audio_path

    @staticmethod
    def _get_file_content(file_path):
        with open(file_path, 'rb') as fp:
            return fp.read()

   
