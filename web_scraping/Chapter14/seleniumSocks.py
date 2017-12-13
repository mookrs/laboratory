from selenium import webdriver

service_args = ['--proxy=localhost:1080', '--proxy-type=socks5']
driver = webdriver.PhantomJS(service_args=service_args)

driver.get("http://icanhazip.com")
print(driver.page_source)
driver.close()
