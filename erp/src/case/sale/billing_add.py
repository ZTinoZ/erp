# encoding:utf-8

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from src.module import approval_module_new, date_module
import time, os


def billing(d, frame="销售开单详情"):
    u"""新增销售开单"""
    d.find_element_by_link_text("销售开单").click()
    d.implicitly_wait(10)
    d.switch_to.frame("销售开单")
    d.find_element_by_link_text("新增").click()
    d.implicitly_wait(10)

    d.switch_to.default_content()
    d.switch_to.frame("新增销售开单")

    # -----------------------------------------------基本信息------------------------------------------------------------

    # # 单据日期（模拟点击方式）
    # d.find_element_by_id("date").click()
    # time.sleep(1)
    # d.find_element_by_link_text(str(now.day)).click()
    # time.sleep(1)

    # # 预计提货日期（模拟点击方式）
    # d.find_element_by_class_name("col-lg-6").find_element_by_name("expect_delivery_date").click()
    # time.sleep(1)
    # d.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/a[2]/span").click()
    # d.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[1]/td[4]/a").click()
    # time.sleep(1)

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

    # 提货仓库
    d.find_element_by_xpath(".//*[@id='select2-delivery_warehouse_id-container']").click()
    time.sleep(1)
    d.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys("141")
    time.sleep(3)
    d.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
    time.sleep(1)

    # 下拉框选择
    Select(d.find_element_by_name("order_type_id")).select_by_index("1")
    Select(d.find_element_by_name("price_type_id")).select_by_index("1")
    Select(d.find_element_by_name("payment_type_id")).select_by_index("1")
    Select(d.find_element_by_name("bill_type_id")).select_by_index("1")
    Select(d.find_element_by_name("rebate_type_id")).select_by_index("1")
    Select(d.find_element_by_name("delivery_id")).select_by_index("1")

    # -----------------------------------------------客户信息------------------------------------------------------------

    # 客户名称
    d.find_element_by_id(".//*[@id='i_form_data']/div[2]/div[1]/div[2]/span[1]/span[1]/span").click()
    time.sleep(1)
    d.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys("141")
    time.sleep(3)
    d.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys(Keys.DOWN)
    d.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
    time.sleep(3)

    # 下拉框选择
    Select(d.find_element_by_name("sale_user_id")).select_by_index("1")

    # 收货地址（该操作属于基本信息）
    d.find_element_by_id("addr_detail").send_keys(u"真如寺")

    # -----------------------------------------------产品明细------------------------------------------------------------

    d.find_element_by_id("item_add_s").click()
    time.sleep(1)

    # 产品
    d.find_element_by_xpath(".//*[@id='tpl_list']/tr[1]/td[5]/div/span/span[1]/span").click()
    time.sleep(1)
    d.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys("141")
    time.sleep(3)
    d.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
    time.sleep(3)

    # 下拉框选择
    Select(d.find_element_by_id("color0")).select_by_index("1")
    Select(d.find_element_by_id("brand_id0")).select_by_index("1")
    Select(d.find_element_by_id("produce_addr_detail0")).select_by_index("1")
    Select(d.find_element_by_id("level_id0")).select_by_index("1")

    Select(d.find_element_by_id("sign0")).select_by_index("1")
    Select(d.find_element_by_id("packing_type_id0")).select_by_index("1")

    # 输入框输入
    d.find_element_by_id("box_num0").send_keys("1")
    time.sleep(2)

    # -----------------------------------------------附件----------------------------------------------------------------

    # d.find_element_by_id("file_add_modal").click()
    # time.sleep(5)
    # d.find_element_by_id("file1_name").send_keys(u"测试附件")
    # d.find_element_by_id("SWFUpload_0").click()
    # SendKeys.SendKeys("E:\PythonWorkspace\erp\data\Selenium.jpg")
    # time.sleep(0.5)
    # SendKeys.SendKeys("{ENTER}")
    # time.sleep(1)
    # try:
    #     d.find_element_by_id("file1_result").text == "Selenium.jpg"
    # except:
    #     print "上传的文件的文件名和屏幕显示的不一样！"
    # d.find_element_by_id("getfile").click()

    # ------------------------------------------------------------------------------------------------------------------

    d.find_element_by_id("button1").click()
    time.sleep(0.5)
    d.find_element_by_id("buy_check_submit").click()
    time.sleep(5)

    # 调用审批模块并获取相应编号
    approval_module_new.approval(d, frame)
    d.implicitly_wait(10)
