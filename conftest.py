<<<<<<< HEAD
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Language for browser UI, e.g. es, fr, ru"
    )


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("--language")

    options = Options()
    options.add_experimental_option(
        "prefs", {"intl.accept_languages": language}
    )

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
=======
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Language for browser UI, e.g. es, fr, ru"
    )


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("--language")

    options = Options()
    options.add_experimental_option(
        "prefs", {"intl.accept_languages": language}
    )

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
>>>>>>> fdd979e849d18d4b493c2c6bf457474bc0219f1e
