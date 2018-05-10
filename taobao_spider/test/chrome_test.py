# 导入selenium的浏览器驱动接口
import time

from selenium import webdriver

# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

# 导入chrome选项
from selenium.webdriver.chrome.options import Options
#
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


# 操作浏览器登录知乎并抓包cookies

chrome_options = Options()
# chrome_options.add_argument('--headless')
browser = webdriver.Chrome('D:\\work\\chromedriver.exe', chrome_options=chrome_options)
for cookie in taobao_cookies.split("; "):
   kv = cookie.split("=")
   browser.add_cookie({'domain': '.taobao.com', 'name': kv[0], 'value': kv[1]})
# browser = webdriver.Chrome('D:\\work\\chromedriver.exe')
browser.get('https://detail.tmall.com/item.htm?id=540174011602')
browser.execute_script('window.scrollTo(0, 2000)')
time.sleep(5)
body = browser.page_source
if "描述加载中" in body:
    print("error")
#<input class="rate-list-all rate-radio-group" id="J_RateWithFilterall1524410054392" type="radio" name="radiogrounp" checked="" data-spm-anchor-id="a220o.1000855.0.i7.577722e3wcgay3">