# encoding:utf-8

from sendmail import sendreport
from runcases_sale import now2
import unittest, os, HTMLTestRunner, time
import runcases_sale

testunit = unittest.TestSuite()
testunit.addTest(unittest.makeSuite(runcases_sale.Runcases))
filename = r"%s\..\reports\%s_report.html" % (os.getcwd(), now2)
filepath = file(filename, 'w+')

runner = HTMLTestRunner.HTMLTestRunner(
    stream=filepath,
    title=u"erp测试报告",
    description=u"用例执行情况："
)

if __name__ == "__main__":
    runner.run(testunit)
    filepath.close()
    time.sleep(1)
    sendreport()
