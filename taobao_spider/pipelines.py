# -*- coding: utf-8 -*-
# import pymongo
import os
import random

import scrapy
from scrapy.conf import settings
import string
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
import shutil


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class ImagesPipeline(ImagesPipeline):
    # def __init__(self):
    # # 链接数据库
    # self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
    # # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])     #如果有账户密码
    # self.db = self.client[settings['MONGO_DB']]  # 获得数据库的句柄
    # self.coll = self.db[settings['MONGO_COLL']]  # 获得collection的句柄

    # 从项目设置文件中导入图片下载路径
    img_store = get_project_settings().get('IMAGES_STORE')

    # 重写ImagesPipeline类的此方法
    # 发送图片下载请求
    def get_media_requests(self, item, info):
        fip = open("ip.txt", "a")
        for i in range(0, len(item['pic_urls'])):
            fip.writelines(item['shop'] + "    " + item['id'] + "    "+ item['pic_urls'][i])
        fip.close()
        # for i in range(0, len(item['pic_urls'])):
        #     # TODO 这里没有设置UA、headers
        #     download_headers = {
        #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        #         'Accept-Encoding': 'gzip, deflate, sdch, br',
        #         'Accept-Language': 'zh-CN,zh;q=0.8',
        #         'Referer': 'https://www.taobao.com/',
        #         'user-agent': random.choice(settings.get('USER_AGENT_LIST'))
        #     }
        #     request = scrapy.Request("http:" + item['pic_urls'][i], headers=download_headers)
        #     yield request
        # pass

    # 重写item_completed方法
    # 将下载的文件保存到不同的目录中
    def item_completed(self, results, item, info):
        # image_path = [x["path"] for ok, x in results if ok]
        # for i in range(0, len(image_path)):
        #     # 定义分类保存的路径
        #     store_path = self.img_store + item['shop'] + "\\" + item['id'] + "\\"
        #     # 目录不存在则创建目录
        #     if os.path.exists(store_path) == False:
        #         os.makedirs(store_path)
        #     # 将文件从默认下路路径移动到指定路径下
        #     if os.path.exists(store_path + os.path.basename(image_path[i])) == False:
        #         # TODO 有时候会报“找不到指定文件”，是因为多个商品都引用了同一张图,导致图片名相同。不影响下载。
        #         shutil.move(self.img_store + image_path[i], store_path)
        #     else:
        #         print("[Warn] 重复图片，要提前过滤。URL:" + item['pic_urls'][i])
        # pass

        return item
