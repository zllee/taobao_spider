import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
def get_cookie(username, password):

    browser = webdriver.Chrome('D:\\work\\chromedriver.exe')

    url = "https://login.taobao.com/"
    browser.get(url)
    # 调整最大窗口，否则某些元素无法显示
    browser.maximize_window()
    #<a href="" class="forget-pwd J_Quick2Static" target="_blank" data-spm-anchor-id="a2107.1.0.0">密码登录</a>
    e1 = browser.find_element_by_class_name("J_Quick2Static")
    e1.click()
    #转到iframe里面去 
    # browser.switch_to_frame(browser.find_element_by_name("taobaoLoginIfr"))

    #<input type="text" name="TPL_username" id="TPL_username_1" class="login-text J_UserName" value="" maxlength="32" tabindex="1" aria-label="会员名/邮箱/手机号" data-spm-anchor-id="a2107.1.0.i4.3e9111d9OF9rUf">
    #输入用户名 
    browser.find_element_by_id("TPL_username_1").clear()
    browser.find_element_by_id("TPL_username_1").send_keys(username)
    time.sleep(1)
    #输入密码 
    browser.find_element_by_id("TPL_password_1").clear()
    browser.find_element_by_id("TPL_password_1").send_keys(password)
    # 模拟登陆淘宝，滑块滑动还有问题。
    # time.sleep(5)  # 等待滑动模块和其他JS文件加载完毕！
    # while True:
    #     try:
    #         # 定位滑块元素
    #         source = browser.find_element_by_id("//*[@id='nc_1_n1z']")
    #         # 定义鼠标拖放动作
    #         ActionChains(browser).drag_and_drop_by_offset(source, 400, 0).perform()
    #         # 等待JS认证运行,如果不等待容易报错
    #         time.sleep(2)
    #         # 查看是否认证成功，获取text值
    #         text = browser.find_element_by_xpath("//div[@id='nc_1__scale_text']/span")
    #         # 目前只碰到3种情况：成功（请在在下方输入验证码,请点击图）；无响应（请按住滑块拖动)；失败（哎呀，失败了，请刷新）
    #         if text.text.startswith(u'请在下方'):
    #             print('成功滑动')
    #             break
    #         if text.text.startswith(u'请点击'):
    #             print('成功滑动')
    #             break
    #         if text.text.startswith(u'请按住'):
    #             continue
    #     except Exception as e:
    #         # 这里定位失败后的刷新按钮，重新加载滑块模块
    #         browser.find_element_by_xpath("//div[@id='havana_nco']/div/span/a").click()
    #         print(e)
    #点击登录按钮 
    browser.find_element_by_id("J_SubmitStatic").click();

    #检测URL是否已经变化，变化我就认为登录成功，简单点嘛
    while True:
            if browser.current_url != url:
                break;
            time.sleep(1)
    
    #cookie取到了 
    cookie = "; ".join([item["name"] + "=" + item["value"] for item in browser.get_cookies()]) \
    #关闭浏览器
    
    browser.quit()
    
    return cookie

cookie = get_cookie('13735578461','gy19891171')
print(cookie)