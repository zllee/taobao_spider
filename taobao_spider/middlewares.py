# douguo request middleware
# for the page which loaded by js/ajax
# ang changes should be recored here:
#
# @author zhangjianfei
# @date 2017/05/04
import base64
import re
import time

from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
from scrapy.utils.project import get_project_settings

settings = get_project_settings()


# 在scrapy中设置的header同样作用于PhantomJS，这里无需再设置
class JavaScriptMiddleware(object):
    def process_request(self, request, spider):
        url = request.url
        pat_url = "https://(.*?).com"
        web = re.compile(pat_url).findall(url)

        if len(web) > 0 and web[0] == 'detail.tmall':  # 仅处理tmall详情页商品
            # 开启虚拟浏览器参数
            dcap = dict(DesiredCapabilities.PHANTOMJS)

            # 设置agents
            dcap["phantomjs.page.settings.userAgent"] = (random.choice(settings.get('USER_AGENT_LIST')))

            # 加载图片
            dcap["phantomjs.page.settings.loadImages"] = True

            driver = webdriver.PhantomJS(executable_path=settings.get('PHANTOMJS_PATH'), desired_capabilities=dcap)

            # 设置20秒页面超时返回
            driver.set_page_load_timeout(12)
            # 设置20秒脚本超时时间
            driver.set_script_timeout(12)
            # get page request
            driver.get(request.url)

            # simulate user behavior
            padix = 2050 + random.randint(0,500)    #超出页面长度也行？
            js = 'window.scrollTo(0,' + str(padix) + ')'  # 模拟移动到网页(0,3000)像素点的位置，如果网页过长，要分多次移动，以免中间部分因为太快没有加载成功。
            driver.execute_script(js)  # 可执行js，模仿用户操作。此处为将页面拉至1000。
            time.sleep(5 + random.randint(0,9))

            # 测试发现，在图片加载的场景中，wait并不起作用
            # 等待异步请求响应
            # driver.implicitly_wait(12)

            # 获取页面源码
            body = driver.page_source

            response = HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)

            return response

        # 由于phantomjs路径已经增添在path中，path可以不写
        # driver = webdriver.PhantomJS()

        # 利用firfox
        # driver = webdriver.Firefox(executable_path=r"D:\FireFoxBrowser\firefox.exe")

        # 利用chrome
        # chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        # os.environ["webdriver.chrome.driver"] = chromedriver
        # driver = webdriver.Chrome(chromedriver)

        # 模拟登陆
        # driver.find_element_by_class_name("input_id").send_keys("34563453")
        # driver.find_element_by_class_name("input_pwd").send_keys("zjf%#￥&")
        # driver.find_element_by_class_name("btn btn_lightgreen btn_login").click()
        # driver.implicitly_wait(15)
        # time.sleep(10)

        # 模拟用户下拉
        # js1 = 'return document.body.scrollHeight'
        # js2 = 'window.scrollTo(0, document.body.scrollHeight)'
        # js3 = "document.body.scrollTop=1000"
        # old_scroll_height = 0
        # while driver.execute_script(js1) > old_scroll_height:
        #     old_scroll_height = driver.execute_script(js1)
        #     driver.execute_script(js2)
        #     time.sleep(3)

        # get time stamp

        # get page screenshot
        # driver.save_screenshot("D:\p.jpg")

        # # 模拟用户在同一个浏览器对象下刷新页面
        # # the whole page source
        # body = ''
        # for i in range(50):
        #     print("SPider name: " + spider.name)
        #     # sleep in a random time for the ajax asynchronous request
        #     # time.sleep(random.randint(5, 6))
        #     time.sleep(random.randint(300, 600))
        #
        #     print("LOGS: freshing page " + str(i) + "...")
        #
        #     # get page request
        #     driver.get(request.url)
        #
        #     # waiting for response
        #     driver.implicitly_wait(30)
        #
        #     # get page resource
        #     body = body + driver.page_source

    # 随机使用预定义列表里的 Proxy代理
