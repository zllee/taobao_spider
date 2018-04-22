import time

from selenium import webdriver
driver = webdriver.PhantomJS(executable_path='D:\\work\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
# driver.implicitly_wait(10) # seconds
driver.get("https://detail.tmall.com/item.htm?id=564151856373")
# driver.execute_script("window.scrollTo(0,2000)")
# time.sleep(5)
# driver.get_screenshot_as_file('test3.png')        #截图对于排查问题很有帮助
driver.execute_script("window.scrollTo(0,3000)")
time.sleep(5)
driver.get_screenshot_as_file('test2.png')
# 获取页面源码
body = driver.page_source

# response = HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
myDynamicElement = driver.find_elements_by_class_name('img-ks-lazyload')
e2 = driver.find_elements_by_xpath('//*[@id="description"]/div/p')
print(myDynamicElement)