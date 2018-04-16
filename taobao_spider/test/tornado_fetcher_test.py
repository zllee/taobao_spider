from selenium import webdriver
import warnings
from taobao_spider.test.tornado_fetcher import Fetcher

warnings.filterwarnings('ignore')

fetcher= Fetcher(
        user_agent='phantomjs', # user agent
        phantomjs_proxy='http://localhost:6666', # phantomjs url
        pool_size=10, # max httpclient num
        async=False
        )
# return fetcher.phantomjs_fetch(url)

url = "https://detail.tmall.com/item.htm?id=563872046867"
response =  fetcher.phantomjs_fetch(url, js_script='setTimeout("function(){window.scrollTo(0,3000)}", 5000)')

print (response)


# url = "https://detail.tmall.com/item.htm?id=563872046867"
# driver = webdriver.PhantomJS(executable_path='D:\\work\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
# driver.get(url)
# print (driver.page_source)


