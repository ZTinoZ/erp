# encoding:utf-8

from src.module import approval_module_new, date_module

import billing_add
import time, os


def delivery(d, frame="提货通知书详情"):
    u"""生成提货通知书"""
    d.find_element_by_xpath(".//*[@id='page-wrapper']/div[1]/div/div/div/div[2]/a").click()

    d.switch_to.default_content()
    d.switch_to.frame("生成提货通知书")

    # -----------------------------------------------承运时间及条件-------------------------------------------------------

    # # 期望到达时间（模拟点击方式）
    # d.find_element_by_class_name("row").find_element_by_name("expect_arrive_date").click()
    # time.sleep(1)
    # d.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/a[2]/span").click()
    # d.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[1]/td[4]/a").click()
    # time.sleep(1)

    # 期望到达时间（修改readonly属性方式）
    js1 = "document.getElementById('expect_arrive_date').removeAttribute('readonly');"
    d.execute_script(js1)
    d.find_element_by_id("expect_arrive_date").clear()
    d.find_element_by_id("expect_arrive_date").send_keys(str(date_module.tomorrow))

    # -----------------------------------------------承运车辆信息---------------------------------------------------------

    # 输入框输入
    d.find_element_by_id("client").send_keys(u"十三张娱乐城")
    d.find_element_by_id("carrier_name").send_keys(u"张十三")
    d.find_element_by_id("carrier_tel").send_keys("110")
    d.find_element_by_id("carrier_car_num").send_keys(u"沪B13")

    # ------------------------------------------------------------------------------------------------------------------

    d.find_element_by_xpath(".//*[@id='page-wrapper']/div/div/div/div/div[2]/button").click()
    time.sleep(0.5)
    d.find_element_by_id("check_submit").click()
    time.sleep(5)

    # 调用审批模块并获取相应编号
    approval_module_new.approval(d, frame)
    d.implicitly_wait(10)
