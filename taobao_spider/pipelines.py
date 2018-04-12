# -*- coding: utf-8 -*-
# import pymongo
import os

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
        for i in range(0, len(item['pic_urls'])):
            yield scrapy.Request("http:" + item['pic_urls'][i])
        pass

    # 重写item_completed方法
    # 将下载的文件保存到不同的目录中
    def item_completed(self, results, item, info):
        image_path = [x["path"] for ok, x in results if ok]
        for i in range(0, len(image_path)):
            # 定义分类保存的路径
            store_path = self.img_store + item['shop'] + "\\" + item['id'] + "\\"
            # 目录不存在则创建目录
            if os.path.exists(store_path) == False:
                os.makedirs(store_path)
            # 将文件从默认下路路径移动到指定路径下
            if os.path.exists(store_path + os.path.basename(image_path[i])) == False:
                shutil.move(self.img_store + image_path[i], store_path)
            else:
                print("[Warn] 重复图片，要提前过滤。URL:" + item['pic_urls'][i])
        pass

        return item


class TaobaoSpiderPipeline(object):
    # def __init__(self):
    # # 链接数据库
    # self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
    # # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])     #如果有账户密码
    # self.db = self.client[settings['MONGO_DB']]  # 获得数据库的句柄
    # self.coll = self.db[settings['MONGO_COLL']]  # 获得collection的句柄

    def process_item(self, item, spider):
        try:
            print('商品ID\t', item['id'])
            print('商品店铺\t', item['shop'])
            print('商品图片urls:')
            for i in range(0, len(item['pic_urls'])):
                if (item['pic_urls'][i].endwith('.jpg')):
                    print(item['pic_urls'][i], "\r\n")
                pass
            pass
            print('------------------------------\n')
            return item
        except Exception as err:
            pass
