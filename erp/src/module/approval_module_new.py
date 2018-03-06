# encoding:utf-8

import time


def approval(d, frame):
    d.switch_to.default_content()
    d.switch_to.frame("提交成功")
    if d.find_element_by_xpath(".//*[@id='wrapper']/div/div/span[1]").text == u"查看详情":
        d.find_element_by_xpath(".//*[@id='wrapper']/div/div/span[1]").click()
    else:
        d.find_element_by_xpath(".//*[@id='wrapper']/div/div/span[2]").click()
    d.implicitly_wait(10)
    d.switch_to.default_content()
    d.switch_to.frame(frame)
    d.find_element_by_name("pass").click()
    d.find_element_by_id("js_confirm_reason").send_keys(u"此处是审批通过的原因。")
    d.find_element_by_xpath(".//*[@id='js_confirm_refer_modal']/div/div/div[3]/div/div[2]/button[1]").click()
    d.implicitly_wait(10)

    # 获取编号
    global num
    num = d.find_element_by_xpath(".//*[@id='page-wrapper']/div[1]/div/div/div/div[3]/form/div[1]/div[1]/div[2]").text

    try:
        d.find_element_by_xpath(".//*[@id='page-wrapper']/div[1]/div/div/div/div[3]/form/div[1]/div[1]/div[11]/span").text == u"审批通过"
    except:
        raise
