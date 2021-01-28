from selenium import webdriver
from utilities.read_config import *

EXECUTABLE_PATH = "browser_driver/chromedriver.exe"
cfg = get_config()
BASE_URL = cfg["E-COMMERCE"]["ADMIN_URL"]


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class")
def create_driver(request, browser):
    """
    Create browser driver
    :param browser:
    :type browser:
    :param request:
    :type request:
    :return:
    :rtype:
    """
    if browser.lower() == "chrome":
        driver = webdriver.Chrome(executable_path=EXECUTABLE_PATH)
        print("***** Launching tests in CHROME *****")
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
        print("***** Launching tests in FIREFOX *****")
    else:
        driver = webdriver.Ie()
        print("***** Launching tests in Internet Explorer *****")
    driver.get(url=BASE_URL)
    print(f"Opened URL: {BASE_URL}")
    driver.maximize_window()
    print("Window maximized")
    request.cls.driver = driver
    yield
    driver.close()
