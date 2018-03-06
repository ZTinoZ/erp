# encoding:utf-8

from selenium import webdriver
from module import login_module, grid_module, starthub, quithub
from billing_add import now
import unittest, os, time
import billing_add, delivery

# 获取当前路径
currentdir = os.path.abspath(os.curdir)
now2 = now.strftime("%Y-%m-%d_%H.%M.%S")
f = open(r"%s\..\error\error.txt" % currentdir, 'wb+')


class Runcases(unittest.TestCase):

    def setUp(self):

        # 启动hub和node
        starthub.h.start()
        time.sleep(1)
        starthub.n1.start()
        # starthub.n2.start()
        # starthub.n3.start()
        # starthub.n4.start()
        # starthub.n5.start()
        time.sleep(5)

        self.baseurl = "http://erp151test.xincap.com/admin/system/login"

    def tearDown(self):
        quithub.kill()  # 终止进程

    def test_run1(self):
        u"""登录"""
        for host, browser in grid_module.grid().items():
            self.driver = webdriver.Remote(
                command_executor=host,
                desired_capabilities={
                    'platform': 'ANY',
                    'browserName': browser,
                    'version': '',
                    'javascriptEnabled': True
                }
            )

            driver = self.driver
            driver.maximize_window()
            driver.get(self.baseurl)

            # 用例部分
            try:  # （需要优化！）
                login_module.login(driver)
                # billing.billing(driver)
                # delivery.delivery(driver)

            except Exception, msg:
                print("用例执行失败，请查看错误信息和错误截图！")
                print(Exception, ":", msg)
                f.write("%s : %s" % (Exception, msg))
                driver.get_screenshot_as_file(r"%s\..\error\%s.jpg" % (currentdir, now2))
                raise
            finally:
                driver.quit()

if __name__ == "__main__":
    unittest.main()
