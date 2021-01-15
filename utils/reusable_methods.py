from configparser import ConfigParser
import pytest


def get_config():
    """
    Create a configuration object which can pass values at different files
    :return:
    :rtype:
    """
    cfg = ConfigParser()
    cfg.read("utils/properties.ini")
    return cfg


@pytest.mark.usefixtures("create_driver")
class Utils:
    """
    Class will hold all the reuable methods that can be used across tests
    """
    def assert_content_absence(self, expected, actual):
        assert expected not in actual
