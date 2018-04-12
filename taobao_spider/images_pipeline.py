# -*- coding: utf-8 -*-
# import pymongo
from scrapy.conf import settings
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.utils.project import get_project_settings


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html





    # def process_item(self, item, spider):
    #     try:
    #         print('商品ID\t', item['id'])
    #         print('商品店铺\t', item['shop'])
    #         print('商品图片urls:')
    #         for i in range(0, len(item['pic_urls'])):
    #             if (item['pic_urls'][i].endwith('.jpg')):
    #                 print(item['pic_urls'][i], "\r\n")
    #             pass
    #         pass
    #         print('------------------------------\n')
    #         return item
    #     except Exception as err:
    #         pass
