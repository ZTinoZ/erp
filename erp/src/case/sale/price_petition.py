# encoding:utf-8

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from src.module import approval_module, date_module
import time


def price_petition(d, frame="价格签呈详情"):
    u"""新增价格签呈"""
    d.find_element_by_link_text("价格签呈").click()
    d.implicitly_wait(10)
    d.switch_to.frame("价格签呈")
    d.find_element_by_link_text("新增").click()
    d.implicitly_wait(10)

    d.switch_to.default_content()
    d.switch_to.frame("新增价格签呈")

    # -----------------------------------------------基本信息------------------------------------------------------------

    # 单据日期（修改readonly属性方式）
    js1 = "document.getElementById('bills_date').removeAttribute('readonly');"
    d.execute_script(js1)
    d.find_element_by_id("bills_date").clear()
    d.find_element_by_id("bills_date").send_keys(str(date_module.today))

    # 签呈开始日期（修改readonly属性方式）
    js2 = "document.getElementById('start_date').removeAttribute('readonly');"
    d.execute_script(js2)
    d.find_element_by_id("start_date").clear()
    d.find_element_by_id("start_date").send_keys(str(date_module.today))

    # 签呈结束日期（修改readonly属性方式）
    js2 = "document.getElementById('end_date').removeAttribute('readonly');"
    d.execute_script(js2)
    d.find_element_by_id("end_date").clear()
    d.find_element_by_id("end_date").send_keys(str(date_module.today))

    # 下拉框选择
    Select(d.find_element_by_name("price_petition_type_id")).select_by_index("1")
    Select(d.find_element_by_name("invoice_id")).select_by_index("1")

    # -----------------------------------------------客户信息------------------------------------------------------------

    # 客户名称
    d.find_element_by_xpath(".//*[@id='select2-price_petition_customer-container']").click()
    time.sleep(1)
    d.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys("141")
    time.sleep(3)
    d.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys(Keys.DOWN)
    d.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
    time.sleep(3)

    # -----------------------------------------------产品明细------------------------------------------------------------

    # 产品
    d.find_element_by_xpath(".//*[@id='tabmaps']/tr/td[3]/span").click()
    time.sleep(1)
    d.find_element_by_xpath(".//*[@id='iframe']/span/span/span[1]/input").send_keys("141")
    time.sleep(3)
    d.find_element_by_xpath(".//*[@id='iframe']/span/span/span[1]/input").send_keys(Keys.ENTER)
    time.sleep(3)

    # 输入框输入
    d.find_element_by_id("num0").send_keys("1")
    d.find_element_by_id("petition_price0").send_keys("1")
    time.sleep(2)

    # ------------------------------------------------------------------------------------------------------------------

    d.find_element_by_id(".//*[@id='sale_price_petition_form']/div/div/div[2]/button").click()
    time.sleep(0.5)
    d.find_element_by_id("sale_price_petition_save").click()
    time.sleep(5)

    # 调用审批模块并获取相应编号
    approval_module.approval(d, frame)
    d.implicitly_wait(10)
