# encoding:utf-8

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from src.module import approval_module, date_module
import time


def remain_petition(d, frame="留货申请单详情"):
    u"""新增留货申请单"""
    d.find_element_by_link_text("留货申请单").click()
    d.implicitly_wait(10)
    d.switch_to.frame("留货申请单")
    d.find_element_by_link_text("新增").click()
    d.implicitly_wait(10)

    d.switch_to.default_content()
    d.switch_to.frame("新增留货申请单")

    # -----------------------------------------------基本信息------------------------------------------------------------

    # 下拉框选择
    Select(d.find_element_by_name("remain_type_id")).select_by_index("1")

    # -----------------------------------------------客户信息------------------------------------------------------------

    # 客户
    d.find_element_by_xpath(".//*[@id='create_check_submit']/div[2]/div/div[2]/span[1]/span[1]/span").click()
    time.sleep(1)
    d.find_element_by_xpath(".//*[@id='iframe']/span/span/span[1]/input").send_keys("141")
    time.sleep(3)
    d.find_element_by_xpath(".//*[@id='iframe']/span/span/span[1]/input").send_keys(Keys.DOWN)
    d.find_element_by_xpath(".//*[@id='iframe']/span/span/span[1]/input").send_keys(Keys.ENTER)
    time.sleep(3)

    # -----------------------------------------------产品明细------------------------------------------------------------

    # 产品
    d.find_element_by_xpath(".//*[@id='tabmaps']/tr/td[3]/span/span[1]/span").click()
    time.sleep(1)
    d.find_element_by_xpath(".//*[@id='iframe']/span/span/span[1]/input").send_keys("141")
    time.sleep(3)
    d.find_element_by_xpath(".//*[@id='iframe']/span/span/span[1]/input").send_keys(Keys.ENTER)
    time.sleep(3)

    # 留货仓库
    d.find_element_by_xpath(".//*[@id='tabmaps']/tr/td[14]/span/span[1]/span").click()
    time.sleep(1)
    d.find_element_by_xpath(".//*[@id='iframe']/span/span/span[1]/input").send_keys("141")
    time.sleep(3)
    d.find_element_by_xpath(".//*[@id='iframe']/span/span/span[1]/input").send_keys(Keys.ENTER)
    time.sleep(3)

    # 下拉框选择
    Select(d.find_element_by_name("brand_id0")).select_by_index("1")
    Select(d.find_element_by_name("level_id0")).select_by_index("1")
    Select(d.find_element_by_name("place_id0")).select_by_index("1")
    Select(d.find_element_by_name("packing_id0")).select_by_index("1")

    # 输入框输入
    d.find_element_by_id("color0").send_keys("141")
    d.find_element_by_id("standard_num0").send_keys("1")
    time.sleep(2)

    # ------------------------------------------------------------------------------------------------------------------

    d.find_element_by_id("add_button").click()
    time.sleep(0.5)
    d.find_element_by_id("check_submit").click()
    time.sleep(5)

    # 调用审批模块并获取相应编号
    approval_module.approval(d, frame)
    d.implicitly_wait(10)
