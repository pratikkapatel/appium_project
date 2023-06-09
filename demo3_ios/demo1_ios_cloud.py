import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap = {
    # Set URL of the application under test
    "app" : "bs://7647a37db4740bb456d32340690bd253b0135249",
    # Specify device and os_version for testing
    "deviceName": "iPhone 11 Pro",
    "platformVersion": "13",
    # Set other BrowserStack capabilities
    "bstack:options": {
        "userName": "tobimylan_1pFN9B",
        "accessKey": "xYxViSzMdVNFtoqV4zFi",
        "projectName": "First Python project",
        "buildName": "browserstack-build-1-ios",
        "sessionName": "BStack first_test-ios"
    }
}

driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", desired_capabilities=des_cap)
driver.implicitly_wait(30)
print(driver.page_source)
time.sleep(5)
driver.quit()