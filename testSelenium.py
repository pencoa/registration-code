import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
    )
driver = webdriver.PhantomJS(executable_path="/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs", desired_capabilities=dcap)
driver.get('http://www.tianyancha.com/login')
time.sleep(5)
content = driver.page_source
driver.close()
print(content)
