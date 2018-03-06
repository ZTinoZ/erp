# encoding:utf-8

from selenium.webdriver.support.select import Select
import time, os


def salestock(d):
    u"""生成备货单"""
    d.find_element_by_xpath(".//*[@id='page-wrapper']/div[1]/div/div/div/div[2]/a").click()

    d.switch_to.default_content()
    d.switch_to.frame("生成备货单")

    # -----------------------------------------------基本信息------------------------------------------------------------

    # 下拉框选择
    Select(d.find_element_by_id("warehouse_user_id")).select_by_value("585")

    # -----------------------------------------------产品明细------------------------------------------------------------

    # 下拉框选择
    Select(d.find_element_by_id("item0location_id")).select_by_index("1")

    # ------------------------------------------------------------------------------------------------------------------

    d.find_element_by_xpath(".//*[@id='page-wrapper']/div[1]/div/div/div/div[2]/button").click()
    time.sleep(0.5)
    d.find_element_by_id("check_submit").click()
    time.sleep(5)
