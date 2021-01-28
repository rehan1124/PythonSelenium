from selenium import webdriver
from utilities.read_config import *

EXECUTABLE_PATH = "browser_driver/chromedriver.exe"
cfg = get_config()
BASE_URL = cfg["E-COMMERCE"]["ADMIN_URL"]


def pytest_addoption(parser):
    """
    Add extra parameter to take browser name as input
    :param parser:
    :type parser:
    :return:
    :rtype:
    """
    parser.addoption("--browser")


@pytest.fixture(scope="class")
def browser(request):
    """
    Fetch the browser name to pass into create_driver fixture
    :param request:
    :type request:
    :return:
    :rtype:
    """
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


def pytest_configure(config):
    """
    Hook for adding environment info to HTML report
    :param config:
    :type config:
    :return:
    :rtype:
    """
    config._metadata['Project Name'] = "nopcommerce"
    config._metadata['Module Name'] = "Customers"
    config._metadata['QA Engineer'] = "Syed Rehan"


def pytest_metadata(metadata):
    """
    Hook to remove/modify environment info in HTML report
    :param metadata:
    :type metadata:
    :return:
    :rtype:
    """
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
