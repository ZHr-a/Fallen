# coding: utf-8

from time import time
from threading import Thread

import requests

class DownloadHandler(Thread):

    def __init__(self,url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/')+1:]
        resp = requests.get(self.url)
        with open(path + filename,'wb') as f :
            f.write(resp.content)

def main():
    resp = requests.get(
        'url'
    )
    data_model = resp.json()
    for mm_dict in data_model['newList']:
        url = mm_dict['picUrl']
        DownloadHandler(url).start()

if __name__ == '__main__':
    main()

