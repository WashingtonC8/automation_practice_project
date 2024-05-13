import pytest
import yaml
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--config', action='store', default="config.yaml",
                     help="Path to the configuration file")


@pytest.fixture(scope="function")
def browser(request):
    config_file = request.config.getoption("config")
    with open(config_file) as file:
        config = yaml.safe_load(file)
    browser_name = config.get("browser_name", "chrome")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()