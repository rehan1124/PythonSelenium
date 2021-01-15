from selenium import webdriver
import pytest
from utils.reusable_methods import *

EXECUTABLE_PATH = "browser_driver/chromedriver.exe"
cfg = get_config()


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="my "
                                                                              "option: Chrome or Firefox or IE")


@pytest.fixture(scope="class")
def create_driver(request):
    """
    Create browser driver
    :param request:
    :type request:
    :return:
    :rtype:
    """
    # browser_name = request.config.getoption("browser_name")
    driver = webdriver.Chrome(executable_path=EXECUTABLE_PATH)
    driver.get(url=cfg['PYTHON-DOCS']['URL'])
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
