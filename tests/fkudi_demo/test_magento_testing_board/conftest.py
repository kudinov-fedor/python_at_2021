from typing import Optional, List
import logging

import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from magento_softwaretesting_board import config


logger = logging.getLogger("DriverLogger")


class MyWebElement(WebElement):

    def find_element(self, by=By.ID, value: Optional[str] = None) -> WebElement:
        logger.info(f"{by} {value}")
        return super().find_element(by, value)

    def find_elements(self, by=By.ID, value: Optional[str] = None) -> List[WebElement]:
        logger.info(f"{by} {value}")
        return super().find_elements(by, value)

    def click(self) -> None:
        logger.info(f"click")
        super().click()


class MyChrome(Chrome):
    _web_element_cls = MyWebElement

    def find_element(self, by=By.ID, value: Optional[str] = None) -> WebElement:
        logger.info(f"{by} {value}")
        return super().find_element(by, value)

    def find_elements(self, by=By.ID, value: Optional[str] = None) -> List[WebElement]:
        logger.info(f"{by} {value}")
        return super().find_elements(by, value)


@pytest.fixture
def user():
    return {"login": config.LOGIN,
            "password": config.PASSWORD,
            "name": config.USER_NAME}


@pytest.fixture
def session():
    session = Chrome()

    with session:
        session.maximize_window()
        yield session


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and "session" in item.funcargs:
        driver = item.funcargs["session"]

        screenshot_path = "screenshots/{}.png".format(report.head_line)
        driver.save_screenshot(screenshot_path)

        try:
            import allure
            allure.attach.file(screenshot_path, attachment_type=allure.attachment_type.PNG)
        except ImportError:
            ...
