# -*- coding: utf-8 -*-
import random
import re
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from taobao_spider.SimpleSpider.settings import Settings as settings

# -*- coding: utf-8 -*-
import time
from scrapy.exceptions import IgnoreRequest
from scrapy.http import HtmlResponse, Response
from selenium import webdriver
import selenium.webdriver.support.ui as ui

# class CustomDownloader(object):
#     def __init__(self):
#         # use any browser you wish
#         cap = webdriver.DesiredCapabilities.PHANTOMJS
#         cap["phantomjs.page.settings.resourceTimeout"] = 1000
#         cap["phantomjs.page.settings.loadImages"] = True
#         cap["phantomjs.page.settings.disk-cache"] = True
#         cap["phantomjs.page.customHeaders.Cookie"] = ' '
#         self.driver = webdriver.PhantomJS(executable_path='F:/phantomjs/bin/phantomjs.exe', desired_capabilities=cap)
#         wait = ui.WebDriverWait(self.driver, 10)
#
#     def VisitPersonPage(self, url):
#         print('正在加载网站.....')
#         self.driver.get(url)
#         time.sleep(1)
#         # 翻到底，详情加载
#         js = "var q=document.documentElement.scrollTop=10000"
#         self.driver.execute_script(js)
#         time.sleep(5)
#         content = self.driver.page_source.encode('gbk', 'ignore')
#         print('网页加载完毕.....')
#         return content
#
#     def __del__(self):
#         self.driver.quit()

# 获取商品详情页
def getItemDetail(shop, id, url):
    # 开启虚拟浏览器参数
    # dcap = dict(DesiredCapabilities.PHANTOMJS)
    # url = "https://detail.tmall.com/item.htm?id=564151856373"
    # headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #            'Accept-Encoding': 'gzip, deflate, sdch, br',
    #            'Accept-Language': 'zh-CN,zh;q=0.8',
    #            'Referer': 'https://www.taobao.com/'
    #            }
    # for key, value in headers.items():
    #     dcap['phantomjs.page.customHeaders.{}'.format(key)] = value
    #
    # # 设置agents
    # dcap["phantomjs.page.settings.userAgent"] = (random.choice(settings.USER_AGENT_LIST))
    #
    # # 禁止加载图片
    # dcap["phantomjs.page.settings.loadImages"] = False

    # driver = webdriver.PhantomJS(executable_path=settings.PHANTOMJS_PATH, desired_capabilities=dcap)
    driver = webdriver.PhantomJS(executable_path=settings.PHANTOMJS_PATH)

    ## 设置20秒页面超时返回
    # driver.set_page_load_timeout(12)
    # # 设置20秒脚本超时时间
    # driver.set_script_timeout(12)
    # get page request
    driver.get(url)

    # simulate user behavior
    padix = 2050 + random.randint(0, 500)  # 超出页面长度也行？
    js = 'window.scrollTo(0,3000)'  # 模拟移动到网页(0,3000)像素点的位置，如果网页过长，要分多次移动，以免中间部分因为太快没有加载成功。
    driver.execute_script(js)  # 可执行js，模仿用户操作。此处为将页面拉至1000。
    time.sleep(5)
    driver.get_screenshot_as_file('test2.png')

    # 获取页面源码
    body = driver.page_source
    return body


if __name__ == '__main__':
    fLog = open(settings.LOG_FILE, "a", encoding='utf-8')
    fid = open(settings.ITEM_ID_FILE, "r", encoding='utf-8')
    fDone = open(settings.ITEM_DONE_FILE, "a", encoding='utf-8')
    try:
        #读商品ID
        #TODO 设置开始的行
        for line in fid.readlines():
            line.replace('\n','')
            segs = line.split('    ')
            if len(segs) < 3:
                continue
            url = segs[2]
            id = segs[1]
            shop = segs[0]
            #访问详情页
            body = getItemDetail(shop,id,url)
            #  Selenium 的 find_element_by_xpath 好像有问题。所以用正则取。详情图的html格式不固定，不能直接根据详情图的class来筛选。所以分开两步。
            #先取出详情部分
            content = re.compile('(<div class="content ke-post" .+<.div>)').findall(body)
            if len(content) == 0:
                fLog.write('[WARN] No Pic.URL:'+ url)
                fLog.write(body)
                continue
            #再取图片
            pic_urls = re.compile('"https:(\/\/img.alicdn.com\/imgextra\/.{50,60}\.jpg)"').findall(content[0])
            if len(pic_urls) == 0:
                fLog.write('[WARN] No Pic.URL:'+ url)
                fLog.write(body)
                continue
                pass
            fPic = open(settings.ITEM_PIC_FILE, "a", encoding='utf-8')
            for i in range(0, len(pic_urls)):
                fPic.write(shop + "\t" + id + "\thttps:" + pic_urls[i] + '\n')
            fPic.close()
            fDone.write(line)
    except Exception as e:
        print('S2错误:', e)
        fLog.write('S2错误:'+ e)
    finally:
        fLog.close()
        fid.close()
        fDone.close()



