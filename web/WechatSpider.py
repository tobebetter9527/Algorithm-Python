# author: tobebetter9527
# since: 2023/02/05 15:40
import re
import time
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

    def download_voice(self, voice_ids: List[str], pre_file_name: str):
        num = 1
        pre_file_name = self.date_time + pre_file_name
        for voice_id in voice_ids:
            url = 'https://res.wx.qq.com/voice/getvoice?mediaid={}'.format(voice_id)
            r = requests.get(url, self.headers)

            file_name = pre_file_name + '-' + str(num) + '.mp3'
            num += 1
            file_path = 'E:\\English\\en_cracker\\{}'.format(file_name)

            with open(file_path, mode='wb') as f:
                f.write(r.content)

            sleep_time = int(random() * 20) + 5
            time.sleep(sleep_time)

    def run(self):
        for pre_name, url in self.urls_dict.items():
            html = self.get_html(url)
            voice_ids = self.get_voice_encode_fileid(html)
            self.download_voice(voice_ids, pre_name)


if __name__ == '__main__':
    urls_dict = {'英文早餐': 'https://mp.weixin.qq.com/s/aexCIz49MXFyKMrWI03z4A',
                 '美剧绝命律师': 'https://mp.weixin.qq.com/s/y58G9XsK7iWO7bflSTgwRA',
                 '英语新闻': 'https://mp.weixin.qq.com/s/XZUqyAh6sBQ77Pzu1-xgbA',
                 '从零开始学英语': 'https://mp.weixin.qq.com/s/TxPv1DHmKOaJvc-EEZx9Cw'}
    date_time = '20230203'
    spider = WechatVoiceSpider(urls_dict, date_time)
    spider.run()
