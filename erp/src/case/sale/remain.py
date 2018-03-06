# encoding:utf-8

from src.module import approval_module_new, date_module

import time, os


def remain(d):
    u"""生成留货单"""
    d.find_element_by_id("makePurchasePlan").click()

    d.switch_to.default_content()
    d.switch_to.frame("生成留货单")

    # ------------------------------------------------------------------------------------------------------------------

    d.find_element_by_id("addbutton").click()
    time.sleep(0.5)
    d.find_element_by_id("check_submit").click()
    time.sleep(5)

    d.find_element_by_id(".//*[@id='wrapper']/div/div/span[1]").click()
    d.switch_to.default_content()
    d.switch_to.frame("留货单详情")
    d.implicitly_wait(10)
