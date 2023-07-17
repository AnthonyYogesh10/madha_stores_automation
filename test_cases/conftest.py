import os
import time
from datetime import datetime
from platform import python_version

import pytest
from appium import webdriver
from py.xml import html

caps = {
    "platformName": "Android",
    "appium:platformVersion": "7.0",
    "appium:deviceName": "ad906ac20703",
    "appium:appPackage": "com.madhastore.pushnotificaiton",
    "appium:appActivity": "com.madhastore.pushnotificaiton/.MainActivity",
    "appium:automationName": "UiAutomator2",
    "appium:noReset": True,
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
}
driver = webdriver.Remote("http://127.0.0.1:4723", caps)


@pytest.fixture(scope="class")
def setup(request):
    global driver
    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.quit()


# modifying  pytest-html title
def pytest_html_report_title(report):
    report.title = "Madha stores html Report"


def pytest_configure(config):
    global caps
    android_version = caps["appium:platformVersion"]
    platform_name = caps["platformName"]
    automation_tool = caps["appium:automationName"]
    py_version = python_version()

    config._metadata = {
        "platform_name": platform_name,
        "android version": android_version,
        "automation_tool": automation_tool,
        "python version": py_version,
    }


# Changing table header pytest-html
def pytest_html_results_table_header(cells):
    del cells[:]
    cells.insert(0, html.th("S.no", class_="sortable"))
    cells.insert(1, html.th("Time"))
    cells.insert(2, html.th("Test Name"))
    cells.insert(3, html.th('Test Case'))
    cells.insert(4, html.th('Result'))
    cells.insert(5, html.th('Duration', col='time'))
    cells.insert(6, html.th('Url'))
    # cells.insert(7, html.th('Browser name'))
    # cells.insert(8, html.th('Browser version'))
    # cells.insert(9, html.th('Screen Size'))
    # cells.insert(10, html.th('last one'))
    cells.pop()


# to remove the additional traceback in html-report  comment longrepr on report in pytest-html

# for take screenshot in pytest html
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    # this is for getting result from pytest result
    report = outcome.get_result()
    # this is for get node id from pytest result
    node_id = report.nodeid
    # Split function is used to split :: from string,very useful function
    module_name, class_name, method_name = node_id.split("::")
    # use this both for data in table row
    report.test_name = class_name
    report.test_case = method_name

    if report.when == "call":
        extra = getattr(report, "extra", [])
        xfail = hasattr(report, "wasxfail")
        # only add additional html on log area
        if (report.failed and not xfail) or report.passed:
            report_directory = os.path.dirname(item.config.option.htmlpath)
            screenshot_folder = 'screenshots'
            test_name = report.test_name
            path_test_name_folder = os.path.join(report_directory, screenshot_folder, test_name)
            time.sleep(2)
            os.makedirs(path_test_name_folder, exist_ok=True)
            file_name = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ".png"
            destination_file = os.path.join(report_directory, screenshot_folder, test_name, file_name)
            time.sleep(2)
            driver.save_screenshot(destination_file)
            rel_file_path = os.path.relpath(destination_file, start=report_directory)
            html = f'<div><img src="{rel_file_path}" alt="screenshot" style="width:300px;height:200px" ' \
                   f'onclick="window.open(this.src)" align="right"/></div>'
            if file_name:
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


serial_no = 0


# Content or data for table row of pytest-html
def pytest_html_results_table_row(report, cells):
    global driver
    del cells[:]
    # for get serial no from pytest html
    global serial_no

    if report.when == "call":
        serial_no += 1
    cells.insert(0, html.td(serial_no))
    cells.insert(1, html.td(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"), class_='col-time'))
    cells.insert(2, html.td(report.test_name))
    cells.insert(3, html.td(report.test_case))
    # this is used to display result
    if report.passed:
        cells.insert(4, html.td('Passed', class_='col-result'))
        cells.append(html.td(html.a('show details', href=f"javascript:show_test_detail('{report.nodeid}')")))
    elif report.failed:
        cells.insert(4, html.td('Failed', class_='col-result'))
        cells.append(html.td(html.a('show details', href=f"javascript:show_test_detail('{report.nodeid}')")))

    # for duration in sec
    duration = '{:.2f}s'.format(report.duration)
    cells.insert(5, html.td(duration, class_='col-time'))
    # for insert url on report
    # url = "https://intertek-dev.trutesta.io/trusamples.mdb5/samples/cf5c0b49-6f07-4a93-b379-dba01ccde2db/sample" \
    #       "-details-tab"
    # cells.insert(6, html.td(html.a('URL', href=url, target="_blank")))
    # # for browser name
    # capabilities = driver.capabilities
    # browser_name = capabilities.get('browserName').capitalize()
    # cells.insert(7, html.td(browser_name))
    # # for browser version
    # browser_version = capabilities.get('browserVersion')
    # cells.insert(8, html.td(browser_version))
    # # for screen size
    # global size
    # cells.insert(9, html.td(size))
    cells.pop()
