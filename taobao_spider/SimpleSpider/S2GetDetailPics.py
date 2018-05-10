# -*- coding: utf-8 -*-
import random
import re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from taobao_spider.SimpleSpider.settings import Settings as settings
import time
from selenium import webdriver
# 导入chrome选项
from selenium.webdriver.chrome.options import Options

taobao_cookies = 'enc=bE9aJP%2B565HBf%2B3TCYIl%2Bc4RIeLWlHKcRn9x%2BJ4jeNUyyvNl9%2FLbvb4dhszbA36Zg6wimL15qsqwMU74srKl7w%3D%3D; ' \
't=096e86139d08724157d57b1051cbf0c2; cna=cJ9PEhYlZQgCASp4SmJtKyWC; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; ' \
'_ga=GA1.2.1884042961.1523099823; miid=74728206941844550; lgc=tb578461_33; tracknick=tb578461_33; ' \
'tg=0; ali_ab=42.120.74.248.1523159078905.5; mt=np=&ci=81_1; cookie2=1c92fbc8e12bd9ab3b5c29ae794e3489; ' \
'_tb_token_=e0e0653337ee3; v=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; dnk=tb578461_33; ' \
'sg=34a; cookie1=Vy%2BWLw1VTtEv2faVWLGajQgdWNYr0FDECQD3zWCSrT8%3D; unb=754316474; publishItemObj=Ng%3D%3D; ' \
'_l_g_=Ug%3D%3D; _nk_=tb578461_33; cookie17=VASuhZ2lbzy1; _mw_us_time_=1524414104426; ' \
'uc1=cookie14=UoTeOozenQ66jQ%3D%3D&lng=zh_CN&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&existShop=false&cookie21=W5iHLLyFe3xm&tag=10&cookie15=WqG3DMC9VAQiUQ%3D%3D&pas=0; ' \
'uc3=nk2=F5RARUIxWA%2BR41U%3D&id2=VASuhZ2lbzy1&vt3=F8dBz4FQolhwqPyQ56k%3D&lg2=W5iHLLyFOGW7aA%3D%3D; existShop=MTUyNDQxNTc5OQ%3D%3D; ' \
'csg=23b31b04; skt=99abeb86c26bae90; _cc_=Vq8l%2BKCLiw%3D%3D; isg=BLS04R8UUjt3mMa3ZVnbACeZhXLmJephJp7Nhk4VQD_CuVQDdp2oB2p_PfFhWhDP'

chrome_options = Options()
# chrome_options.add_argument('--headless')
browser = webdriver.Chrome('D:\\work\\chromedriver.exe', chrome_options=chrome_options)
# isg=BHh4l69VVgdSlrqD3kZp59iPSCbKSe59AmoR0rLpxLNmzRi3WvGs-47vgcT9hpRD; _uab_collina=152441564652151152570461; cookieCheck=38285; v=0; cna=oKpjEyD23wsCAXAKGqO29GFd; cookie2=1b35ee9e20e7a7dbf155a9c60bc12575; _tb_token_=9bf186dee4ed; t=42e7add6bf970acda339bc02858d3eba; _umdata=7A3AC4BAEF2935C1FFA217AEA28C214D7CB9A5892BBB16D93200D1D0890D1B715AD10C5C0E9D4BA4CD43AD3E795C914C9D4FE848BDED21385E52859D5986FA20
#_uab_collina=150890181334941261170969; log=lty=Ug%3D%3D; enc=bE9aJP%2B565HBf%2B3TCYIl%2Bc4RIeLWlHKcRn9x%2BJ4jeNUyyvNl9%2FLbvb4dhszbA36Zg6wimL15qsqwMU74srKl7w%3D%3D; t=096e86139d08724157d57b1051cbf0c2; cna=cJ9PEhYlZQgCASp4SmJtKyWC; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; _ga=GA1.2.1884042961.1523099823; miid=74728206941844550; lid=tb578461_33; lgc=tb578461_33; tracknick=tb578461_33; tg=0; ali_ab=42.120.74.248.1523159078905.5; mt=np=&ci=81_1; cookie2=1c92fbc8e12bd9ab3b5c29ae794e3489; _tb_token_=e0e0653337ee3; v=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; uc1=cookie14=UoTeOozenMunzQ%3D%3D&lng=zh_CN&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&existShop=false&cookie21=V32FPkk%2FgPzW&tag=10&cookie15=VT5L2FSpMGV7TQ%3D%3D&pas=0; uc3=nk2=F5RARUIxWA%2BR41U%3D&id2=VASuhZ2lbzy1&vt3=F8dBz4FQolnhjYO9SjQ%3D&lg2=WqG3DMC9VAQiUQ%3D%3D; existShop=MTUyNDQxNDEwMw%3D%3D; dnk=tb578461_33; sg=34a; csg=9c36b654; cookie1=Vy%2BWLw1VTtEv2faVWLGajQgdWNYr0FDECQD3zWCSrT8%3D; unb=754316474; skt=ece04ed841e01f9b; publishItemObj=Ng%3D%3D; _cc_=W5iHLLyFfA%3D%3D; _l_g_=Ug%3D%3D; _nk_=tb578461_33; cookie17=VASuhZ2lbzy1; lc=VygpXWog7Uns0tX4UcUBdQ%3D%3D; cookieCheck=36643; isg=BGBg34GfLn8q25I7ET33ROv1MG7ywXYl2mI5CtpxLHsO1QD_gnkUwzbnaX3V_vwL; _umdata=6AF5B463492A874DBAC2D4C9E0F44B0D904E44E96B0882B67FDE66D358ACFE6FCEB79F1F583A0663CD43AD3E795C914C87DEEFA95D7C93143575455E26B0591B
flag = 0

# 获取商品详情页
def getItemDetailByChrome(shop, id, url):
    # chrome_options = Options()
    # # chrome_options.add_argument('--headless')
    # browser = webdriver.Chrome('D:\\work\\chromedriver.exe', chrome_options=chrome_options)
    # browser = webdriver.Chrome('D:\\work\\chromedriver.exe')
    browser.get(url)
    for cookie in taobao_cookies.split("; "):
        kv = cookie.split("=")
        browser.add_cookie({'domain': '.taobao.com', 'name': kv[0], 'value': kv[1]})

    browser.execute_script('window.scrollTo(0, 2000)')
    time.sleep(5)
    body = browser.page_source
    return body

# 获取商品详情页
def getItemDetail(shop, id, url):
    driver = webdriver.PhantomJS(executable_path=settings.PHANTOMJS_PATH)
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

# 获取商品详情页 添加header信息。参考：http://www.cnblogs.com/zhouxinfei/p/8098809.html
# 总结1：详情加载不出来时，再次模拟移动也不会有作用。
def getItemDetailWithHeaders(shop, id, url):
    # headers = {
    #     'Cookie': 'OUTFOX_SEARCH_USER_ID=-1948611671@42.120.74.233; fvf_gouwu=https://s.taobao.com/search?q=%E8%8A%B1%E9%A6%99%E8%82%89%E6%A1%82; fvt_gouwu=2017-11-08; vts_gouwu=1; zhushou_browser=chrome; zhushou_version=4.2.9.7; Hm_lvt_01a30a02a2ef2f43ddce734acd978400=1523675232; eadsync=1; zspid=2815; zsrecmd=manualedit; JSESSIONID=abcY6wNp_gwPk6WWaIPlw; sf_gouwu=https://detail.tmall.com/item.htm?id=565198855572; vendor_gouwu=tmall.com; zs_popup_lock=manualedit',
    # }
    # service_args = [
    #     # '--proxy=%s' % ips,  # 代理 IP：prot    （eg：192.168.0.28:808）
    #     # '--ssl-protocol=any',  # 忽略ssl协议
    #     '--load-images=yes',  # 关闭图片加载（可选）
    #     # '--disk-cache=yes',  # 开启缓存（可选）
    #     # '--ignore-ssl-errors=true'  # 忽略https错误(可选)
    # ]

    dcap = DesiredCapabilities.PHANTOMJS.copy()
    dcap["phantomjs.page.settings.userAgent"] = (
        random.choice(settings.USER_AGENT_LIST)
    )
    # for key in headers:
    #     dcap['phantomjs.page.customHeaders.{}'.format(key)] = headers[key]

    driver = webdriver.PhantomJS(executable_path=settings.PHANTOMJS_PATH, desired_capabilities=dcap)
    driver.start_session(dcap)
    driver.get(url)

    # simulate user behavior
    js = 'window.scrollTo(' + str(random.randint(0, 400)) + ',' + str(random.randint(2500, 3500)) + ')'  # 模拟移动到网页(0,3000)像素点的位置，如果网页过长，要分多次移动，以免中间部分因为太快没有加载成功。
    driver.execute_script(js)  # 可执行js，模仿用户操作。此处为将页面拉至1000。
    time.sleep(5)
    driver.get_screenshot_as_file('test2.png')

    # 获取页面源码
    body = driver.page_source

    # if "描述加载中" in body:
    #     js = 'window.scrollTo(' + str(random.randint(0, 400)) + ',' + str(random.randint(1500, 2500)) + ')'  # 模拟移动到网页(0,3000)像素点的位置，如果网页过长，要分多次移动，以免中间部分因为太快没有加载成功。
    #     driver.execute_script(js)  # 可执行js，模仿用户操作。此处为将页面拉至1000。
    #     time.sleep(5)
    #     driver.get_screenshot_as_file('test2.png')

    return body


if __name__ == '__main__':
    fLog = open(settings.LOG_FILE, "a", encoding='utf-8')
    fid = open(settings.ITEM_ID_FILE, "r", encoding='utf-8')
    try:
        # 读商品ID
        # TODO 设置开始的行
        for line in fid.readlines():
            line.replace('\n', '')
            segs = line.split('    ')
            if len(segs) < 3:
                continue
            url = segs[2]
            id = segs[1]
            shop = segs[0]
            # 访问详情页
            body = getItemDetailByChrome(shop, id, url)
            #  Selenium 的 find_element_by_xpath 好像有问题。所以用正则取。详情图的html格式不固定，不能直接根据详情图的class来筛选。所以分开两步。
            # 先取出详情部分
            content = re.compile('(<div class="content ke-post" .+<.div>)').findall(body)
            if len(content) == 0:
                fLog.write('[WARN] No Pic.URL:' + url)
                fLog.write(body)
                continue
            # 再取图片
            pic_urls = re.compile('"https:(\/\/img.alicdn.com\/imgextra\/.{50,60}\.jpg)"').findall(content[0])
            if len(pic_urls) == 0:
                fLog.write('[WARN] No Pic.URL:' + url)
                fLog.write(body)
                continue
                pass
            fPic = open(settings.ITEM_PIC_FILE, "a", encoding='utf-8')
            fDone = open(settings.ITEM_DONE_FILE, "a", encoding='utf-8')
            for i in range(0, len(pic_urls)):
                fPic.write(shop + "\t" + id + "\thttps:" + pic_urls[i] + '\n')
            fPic.close()
            fDone.write(line)
            fDone.close()
    except Exception as e:
        print('S2错误:', e)
        fLog.write('S2错误:' + e)
    finally:
        fLog.close()
        fid.close()
