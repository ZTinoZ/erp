# encoding:utf-8


def login(d):
    d.find_element_by_id("exampleInputEmail1").send_keys("zhangyinhao")
    d.find_element_by_name("password").send_keys("123abc")
    d.find_element_by_name("captcha").send_keys("pwd!@#")
    d.find_element_by_xpath(".//*[@id='abs']/form/button").click()
    d.implicitly_wait(10)
    try:
        d.current_url == "http://erp151test.xincap.com/admin/system/my_home"
    except:
        raise
