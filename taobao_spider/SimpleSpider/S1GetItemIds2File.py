# -*- coding: utf-8 -*-
import re

import requests
from taobao_spider.SimpleSpider.settings import Settings as settings

# 从列表页下载商品ID，店铺ID
if __name__ == '__main__':
    key = "女装"
    pages = 5
    url = "https://s.taobao.com/search?q=" + str(key) + "&s=" + str(44 * pages)
    fLog = open(settings.LOG_FILE, "a", encoding='utf-8')
    try:
        response = requests.get(url)
        body = response.content.decode('utf-8', 'ignore')

        pat_id = '"nid":"(.*?)"'  # 匹配id
        pat_shop = '"nick":"(.*?)"'  # 匹配店铺名

        all_id = re.compile(pat_id).findall(body)
        all_shop = re.compile(pat_shop).findall(body)
        for i in range(0, len(all_id)):
            this_id = all_id[i]
            this_shop = all_shop[i]
            url = "https://item.taobao.com/item.htm?id=" + str(this_id)
            fip = open(settings.ITEM_ID_FILE, "a", encoding='utf-8')
            fip.write(this_shop + "    " + this_id + "    " + url)
            fip.close()
    except Exception as e:
        print('获取商品ID错误:', e.reason)
        fLog.write('获取商品ID错误:', e.reason)
    fLog.close()