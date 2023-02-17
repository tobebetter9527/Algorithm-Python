# author: tobebetter9527
# since: 2023/02/05 15:40
import os
import re
import time
from os import path
from random import random
from typing import List

import requests


class WechatVoiceSpider:

    def __init__(self, urls_dict: dict, date_time: str):
        self.urls_dict = urls_dict
        self.date_time = date_time
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/109.0.0.0 Safari/537.36'}

    def get_html(self, url: str):
        res = requests.get(url, self.headers)
        return res.text

    def get_voice_encode_fileid(self, html):
        pattern = re.compile('voice_encode_fileid="(.*?)"')
        return pattern.findall(html)

    def create_directory(self):
        p = 'E:\\English\\en_cracker\\' + self.date_time[0:6]
        if not path.exists(p):
            os.makedirs(p)
        return p

    def download_voice(self, voice_ids: List[str], pre_file_name: str, directory: str):
        num = 1
        pre_file_name = self.date_time + pre_file_name
        for voice_id in voice_ids:
            url = 'https://res.wx.qq.com/voice/getvoice?mediaid={}'.format(voice_id)
            r = requests.get(url, self.headers)

            file_name = pre_file_name + '-' + str(num) + '.mp3'
            file_path = directory + '\\' + file_name
            num += 1
            with open(file_path, mode='wb') as f:
                f.write(r.content)

            self.sleep_random_time()

    def sleep_random_time(self):
        sleep_time = int(random() * 10) + 5
        time.sleep(sleep_time)

    def handle_titles(self, heads, html, url):
        pattern = re.compile('var msg_title = \'(.*?)\'')
        hs = pattern.findall(html)
        str_url = '- [' + hs[0] + '](' + url + ')' + '\n'
        heads.append(str_url)

    def run(self):
        directory = self.create_directory()
        heads = ['## ' + self.date_time + '\n']
        for pre_name, url in self.urls_dict.items():
            html = self.get_html(url)
            self.handle_titles(heads, html, url)
            voice_ids = self.get_voice_encode_fileid(html)
            self.download_voice(voice_ids, pre_name, directory)

        with open(directory + '\\' + '123456.txt', mode='w') as f:
            f.writelines(heads)


if __name__ == '__main__':
    urls_dict = {}
    urls_dict['英文早餐'] = 'https://mp.weixin.qq.com/s/xHNDmiOqJMnqbTZ4VLIgDQ'
    urls_dict['美剧人生切割术'] = 'https://mp.weixin.qq.com/s/u2GzAtHQfl0VssCB4lVoZA'
    urls_dict['英语新闻'] = 'https://mp.weixin.qq.com/s/8zwxXo_CHrwZf0YFeZiF6w'
    urls_dict['从零开始学英语'] = 'https://mp.weixin.qq.com/s/gD8kvmGQPplM-DSJZ97Reg'
    date_time = '20230217'
    spider = WechatVoiceSpider(urls_dict, date_time)
    spider.run()
