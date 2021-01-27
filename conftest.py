from selenium import webdriver
from utilities.read_config import *

EXECUTABLE_PATH = "browser_driver/chromedriver.exe"
cfg = get_config()
BASE_URL = cfg["E-COMMERCE"]["ADMIN_URL"]


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="my " "option: Chrome or Firefox or IE",
    )


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
    driver.get(url=BASE_URL)
    print(f"Opened URL: {BASE_URL}")
    driver.maximize_window()
    print("Window maximized")
    request.cls.driver = driver
    yield
    driver.close()
