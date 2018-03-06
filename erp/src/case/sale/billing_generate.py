# encoding:utf-8

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from src.module import approval_module_new, date_module
import time, os


def billing(d, frame="销售开单详情"):
    u"""生成销售开单"""
    d.find_element_by_id("makePurchasePlan").click()
    time.sleep(0.5)
    Select(d.find_element_by_name("w_id")).select_by_index("1")
    d.find_element_by_xpath(".//*[@id='reason_copyForm']/div/div/div[3]/div/div[2]/button[1]").click()

    d.switch_to.default_content()
    d.switch_to.frame("生成销售开单")

    # -----------------------------------------------基本信息------------------------------------------------------------

    # 单据日期（修改readonly属性方式）
    js1 = "document.getElementById('date').removeAttribute('readonly');"
    d.execute_script(js1)
    d.find_element_by_id("date").clear()
    d.find_element_by_id("date").send_keys(str(date_module.today))

    # 预计提货日期（修改readonly属性方式）
    js2 = "document.getElementById('expect_delivery_date').removeAttribute('readonly');"
    d.execute_script(js2)
    d.find_element_by_id("expect_delivery_date").clear()
    d.find_element_by_id("expect_delivery_date").send_keys(str(date_module.tomorrow))

    # 下拉框选择
    Select(d.find_element_by_name("price_type_id")).select_by_index("1")
    Select(d.find_element_by_name("payment_type_id")).select_by_index("1")
    Select(d.find_element_by_name("rebate_type_id")).select_by_index("1")
    Select(d.find_element_by_name("delivery_id")).select_by_index("1")

    # -----------------------------------------------客户信息------------------------------------------------------------

    # 下拉框选择
    Select(d.find_element_by_name("sale_user_id")).select_by_index("1")

    # 收货地址（该操作属于基本信息）
    d.find_element_by_id("addr_detail").send_keys(u"真如寺")

    # -----------------------------------------------产品明细------------------------------------------------------------

    # 下拉框选择
    Select(d.find_element_by_id("sign0")).select_by_index("1")

    # ------------------------------------------------------------------------------------------------------------------

    d.find_element_by_id("button1").click()
    time.sleep(0.5)
    d.find_element_by_id("buy_check_submit").click()
    time.sleep(5)

    # 调用审批模块并获取相应编号
    approval_module_new.approval(d, frame)
    d.implicitly_wait(10)
