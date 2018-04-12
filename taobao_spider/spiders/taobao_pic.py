# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from taobao_spider.items import TaobaoPicItem
import urllib.request
# from scrapy_redis.spiders import RedisSpider
from scrapy.spiders import Spider

class TaobaoSpider(Spider):
    name = 'taobao_pic'
    # allowed_domains = ['taobao.com']
    start_urls = ['http://taobao.com/']
    redis_key = 'TaobaoSpider:start_urls'

    def parse(self, response):
        # key = input("请输入你要爬取的关键词\t")
        # pages = input("请输入你要爬取的页数\t")
        key = "女装"
        pages = '100'
        print("\n")
        print("当前爬取的关键词是",key)
        print("\n")
        for i in range(0, int(pages)):
            url = "https://s.taobao.com/search?q=" + str(key) + "&s=" + str(44*i)
            yield Request(url=url, callback=self.page)
        pass

    def page(self,response):
        body = response.body.decode('utf-8', 'ignore')

        pat_id = '"nid":"(.*?)"'    #匹配id
        pat_shop = '"nick":"(.*?)"'      #匹配店铺名

        all_id = re.compile(pat_id).findall(body)
        all_shop = re.compile(pat_shop).findall(body)

        for i in range(0, len(all_id)):
            this_id = all_id[i]
            this_shop = all_shop[i]
            url = "https://item.taobao.com/item.htm?id=" + str(this_id)
            yield Request(url=url, callback=self.next, meta={ 'this_id': this_id, 'this_shop': this_shop})
            pass
        pass

    def next(self, response):
        item = TaobaoPicItem()
        url = response.url
        pat_url = "https://(.*?).com"
        web = re.compile(pat_url).findall(url)

        if web[0] != 'item.taobao':     #天猫或天猫超市 TODO 后续支持淘宝商品
            pic_urls = re.compile('(\/\/img.alicdn.com\/imgextra\/.{52}\.jpg)').findall(response.body.decode('utf-8', 'ignore'))
            # pic_urls = response.xpath("//div[contains(@class,'content ke-post')]//img/@src").extract()  #获取商品详情图片urls     #TODO xpath解析出错，先用正则代替
            # price = response.xpath("//span[@class = 'tm-price']/text()").extract()  #获取商品原价格
            # pat_id = 'id=(.*?)&'
            # this_id = re.compile(pat_id).findall(url)[0]

            item['id'] = response.meta['this_id']
            item['shop'] = response.meta['this_shop']
            item['pic_urls'] = list(set(pic_urls))  #去重，因为使用正则会有重复图片
            yield item


