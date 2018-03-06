# encoding:utf-8

from selenium import webdriver
from module import login_module, logout_module, date_module
from case.sale import price_petition, remain_petiton, remain, billing_generate, billing_add, delivery, salestock, goods_send, assure_petition
import unittest, os, time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 获取当前路径
currentdir = os.path.abspath(os.curdir)
now2 = date_module.now.strftime("%Y-%m-%d_%H.%M.%S")
f = open(r"%s\..\error\error.txt" % currentdir, 'wb+')


class Runcases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://erp151test.xincap.com/admin/system/login')

        login_module.login(self.driver)

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(".//*[@id='bs-example-navbar-collapse-1']/ul/li[6]/a").click()

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

    def test_a_billing(self):
        u"""销售开单+提货通知书+备货单+销售发货单"""
        try:

            # 用例组合
            billing_add.billing(self.driver)
            delivery.delivery(self.driver)
            salestock.salestock(self.driver)
            goods_send.goods_send(self.driver)

        except Exception, msg:
            print("用例执行失败，请查看错误信息和错误截图！")
            print(Exception, ":", msg)
            f.write("%s : %s" % (Exception, msg))
            self.driver.get_screenshot_as_file(r"%s\..\error\%s.jpg" % (currentdir, now2))
            raise

    def test_b_price_petition(self):
        u"""价格签呈+销售开单+提货通知书+备货单+销售发货单"""
        try:

            # 用例组合
            price_petition.price_petition(self.driver)
            billing_generate.billing(self.driver)
            delivery.delivery(self.driver)
            salestock.salestock(self.driver)
            goods_send.goods_send(self.driver)

        except Exception, msg:
            print("用例执行失败，请查看错误信息和错误截图！")
            print(Exception, ":", msg)
            f.write("%s : %s" % (Exception, msg))
            self.driver.get_screenshot_as_file(r"%s\..\error\%s.jpg" % (currentdir, now2))
            raise

    def test_c_remain_petition(self):
        u"""留货申请单+销售开单+提货通知书+备货单+销售发货单"""
        try:

            # 用例组合
            remain_petiton.remain_petition(self.driver)
            remain.remain(self.driver)
            billing_generate.billing(self.driver)
            delivery.delivery(self.driver)
            salestock.salestock(self.driver)
            goods_send.goods_send(self.driver)

        except Exception, msg:
            print("用例执行失败，请查看错误信息和错误截图！")
            print(Exception, ":", msg)
            f.write("%s : %s" % (Exception, msg))
            self.driver.get_screenshot_as_file(r"%s\..\error\%s.jpg" % (currentdir, now2))
            raise

    def test_d_assure_petition(self):
        u"""担保单"""
        try:

            # 用例组合
            assure_petition.assure_petition(self.driver)

        except Exception, msg:
            print("用例执行失败，请查看错误信息和错误截图！")
            print(Exception, ":", msg)
            f.write("%s : %s" % (Exception, msg))
            self.driver.get_screenshot_as_file(r"%s\..\error\%s.jpg" % (currentdir, now2))
            raise


if __name__ == "__main__":
    unittest.main()
