# filename:spider_taobao.py
#!/usr/bin/env python
# -*- coding=utf-8 -*-

import re
import urllib2


USER_AGENT_LIST = [
        #    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        #    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER',
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]

urldict = {
    'https://s.taobao.com/search?spm=a230r.1.0.0.aCclFK&q=%E7%9C%9F%E4%B8%9D%E8%BF%9E%E8%A1%A3%E8%A3%99':'真丝连衣裙',
    'https://s.taobao.com/search?spm=a230r.1.0.0.ijf5DJ&q=%E5%8D%8A%E8%BA%AB%E8%A3%99':'半身裙',
}

 headers = {
  'Accept':'application/json, text/plain, */*',
  'Accept-Language':'zh-CN,zh;q=0.3',
  'Referer':'https://item.taobao.com/item.htm',
  'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
  'Connection':'keep-alive',
 }

 goods_id = re.findall('id=(\d+)', url)[0]

 try:
  req = urllib2.Request(url=url, headers=headers)
  res = urllib2.urlopen(req).read().decode('gbk', 'ignore')
 except Exception as e:
  print ('无法打开网页:', e.reason)

 try:
  title = re.findall('<h3 class="tb-main-title" data-title="(.*?)"', res)
  title = title[0] if title else None
  line_price = re.findall('<em class="tb-rmb-num">(.*?)</em>', res)[0]

  # 30-42行为抓取淘宝商品真实价格，该数据是动态加载的
  purl = "https://detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId={}&modules=price,xmpPromotion".format(goods_id)

  price_req = urllib2.Request(url=purl, headers=headers)
  price_res = urllib2.urlopen(price_req).read()
  data = list(set(re.findall('"price":"(.*?)"', price_res)))
  # data列表中的价格可能是定值与区间的组合，也可能只是定值，而且不一定有序
  real_price = ""
  for t in data:
   if '-' in t:
    real_price = t
    break
  if not real_price:
   real_price = sorted(map(float, data))[0]

  # 45-53行为抓取评论数据，该数据也是动态加载的
  comment_url = "https://rate.tmall.com/list_detail_rate.htm?itemId={}&sellerId=880734502¤tPage=1".format(goods_id)
  comment_data = urllib2.urlopen(comment_url).read().decode("GBK", "ignore")
  temp_data = re.findall('("commentTime":.*?),"days"', comment_data)
  temp_data = temp_data if temp_data else re.findall('("rateContent":.*?),"reply"', comment_data)
  comment = ""
  for data in temp_data:
   comment += data.encode('utf-8')
  comment = comment if comment else "暂无评论"
 except Exception as e:
  print '数据抽取失败!!!'

 print '商品名:', title
 print '划线价格:', line_price
 print '真实价格:', real_price
 print '商品链接:', url
 print '部分评论内容:', comment

if __name__ == '__main__':
 #url = 'https://item.taobao.com/item.htm?spm=a230r.1.14.30.43306a3fOeuZ0B&id=553787375606&ns=1&abbucket=10#detail'
 url = raw_input("请输入商品链接: ")
 spider_taobao(url)