# encoding:utf-8

from src.module import approval_module_new

import billing_add
import time, os


def goods_send(d, frame="销售发货单详情"):
    u"""生成发货单"""
    d.find_element_by_xpath(".//*[@id='wrapper']/div/div/span[1]").click()
    d.implicitly_wait(10)
    d.find_element_by_xpath(".//*[@id='page-wrapper']/div/div/div/div/div[2]/a/button").click()

    d.switch_to.default_content()
    d.switch_to.frame("生成销售发货单")

    # ------------------------------------------------------------------------------------------------------------------

    d.find_element_by_xpath(".//*[@id='page-wrapper']/div[1]/div/div/div/div[2]/button").click()
    time.sleep(0.5)
    d.find_element_by_id("check_submit").click()
    time.sleep(5)

    # 调用审批模块并获取相应编号
    approval_module_new.approval(d, frame)
    d.implicitly_wait(10)
