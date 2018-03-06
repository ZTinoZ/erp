# encoding:utf-8

from src.module import approval_module_new, date_module
from selenium.webdriver.common.keys import Keys
import billing_add
import time, os


def assure_petition(d, frame="担保单详情"):
    u"""新增担保单"""
    d.find_element_by_link_text("担保单").click()
    d.implicitly_wait(10)
    d.switch_to.default_content()
    d.switch_to.frame("担保单")
    d.find_element_by_link_text("新增").click()
    d.implicitly_wait(10)

    d.switch_to.default_content()
    d.switch_to.frame("新增担保单")

    # -----------------------------------------------基本信息------------------------------------------------------------

    # 输入框输入
    d.find_element_by_id("amount").send_keys("1")

    # -----------------------------------------------客户信息------------------------------------------------------------

    # 客户
    d.find_element_by_xpath(".//*[@id='sale_assure_petition_form']/div[2]/div/div[2]/span[1]/span[1]/span").click()
    time.sleep(1)
    d.find_element_by_xpath(".//*[@id='iframe']/span/span/span[1]/input").send_keys("141")
    time.sleep(3)
    d.find_element_by_xpath(".//*[@id='iframe']/span/span/span[1]/input").send_keys(Keys.DOWN)
    d.find_element_by_xpath(".//*[@id='iframe']/span/span/span[1]/input").send_keys(Keys.ENTER)
    time.sleep(3)

    # ------------------------------------------------------------------------------------------------------------------

    d.find_element_by_id("button0").click()
    time.sleep(0.5)
    d.find_element_by_xpath(".//*[@id='confirm_approve']/div/div/div[3]/div/div/button[1]").click()
    time.sleep(5)

    # 调用审批模块并获取相应编号
    approval_module.approval(d, frame)
    d.implicitly_wait(10)
