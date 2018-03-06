# encoding:utf-8


def logout(d):
    d.find_element_by_link_text("系统退出").click()
    d.implicitly_wait(10)
    try:
        d.current_url == "http://erp151test.xincap.com/admin/system/login"
    except:
        raise
