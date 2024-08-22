from __future__ import annotations
import logging
import time
from datetime import datetime
from time import sleep
import allure
from allure_commons.types import AttachmentType
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import WebDriverException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import env
from ui.src.PlatformConfig import PlatformConfig

log = logging.getLogger(__name__)


class BaseAppPage:
    """Base parent class for every application PageObject class"""
    app_launched = False

    def __init__(self):
        self.driver = PlatformConfig.drivers[PlatformConfig.platform]
        self.wait = self.create_wait(30)
        self.click_wait_time = 0

    def create_wait(self, secs: int) -> WebDriverWait:
        return WebDriverWait(self.driver, secs)

    def reset_app(self) -> None:
        log.info("Resetting App")
        self.driver.reset()

    def launch_app(self) -> None:
        if not BaseAppPage.app_launched:
            log.info("re-launching | launch app")
            self.driver.launch_app()
            BaseAppPage.app_launched = True

    def close_relaunch_app(self) -> None:
        log.info("Closing the application")
        self.driver.close_app()
        log.info("Relaunch app")
        self.driver.launch_app()

    def find_element_by_xpath_without_waiting(self, element: str) -> WebElement:
        log.info(f"Finding this {element} element without any delay")
        return self.driver.find_element(AppiumBy.XPATH, element)

    def wait_for_element_visibility(self, locator) -> WebElement:
        log.info(f'waiting for element visibility: {locator}')
        self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, locator)))
        self.wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, locator)))
        return self.driver.find_element(By.XPATH, locator)

    def wait_for_element_by_accessibility_id(self, element: str) -> WebElement:
        log.info(f"Waiting for element by accessibility id with element = {element}")
        self.wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, element)))
        self.wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, element)))
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, element)

    def dump_server_logs(self):
        for entry in self.driver.get_log('server'):
            if entry:
                log.info(f'server-logs: {entry}')

    def get_click_wait_time(self) -> int:
        return self.click_wait_time

    def set_click_wait_time(self, secs: int):
        self.click_wait_time = secs

    def click_element(self, locator, wait_time: int = 0) -> str:
        def click_element_impl(locator) -> str:
            click_wait_time = wait_time + self.get_click_wait_time()
            if click_wait_time:
                log.info(f"click element: {locator} in {click_wait_time} secs")
            else:
                log.info(f"click element: {locator}")
            self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, locator)))
            self.wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, locator)))
            self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, locator)))
            element = self.driver.find_element(AppiumBy.XPATH, locator)
            if click_wait_time:
                time.sleep(click_wait_time)
            element.click()
            return element_text

        element_text = None
        try:
            element_text = click_element_impl(locator)
        except Exception:
            element_text = click_element_impl(locator)
        return element_text

    def check_invisibility_of_element(self, locator) -> bool:
        log.info(f'check invisibility of element: {locator}')
        count = len(self.driver.find_elements(AppiumBy.XPATH, locator))
        return count == 0

    def check_visibility_of_element(self, locator, wait_time: int = 0) -> bool:
        log.info(f'check visibility of element: {locator}')
        time.sleep(wait_time)
        count = len(self.driver.find_elements(AppiumBy.XPATH, locator))
        return count > 0

    def click_element_with_id(self, element: str, wait_time: int = 0) -> None:
        log.info(f"click element with id = {element}")
        try:
            click_wait_time = wait_time + self.get_click_wait_time()
            self.wait.until(EC.presence_of_element_located((AppiumBy.ID, element)))
            self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, element)))
            self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, element)))
            element = self.driver.find_element(AppiumBy.ID, element)
            if click_wait_time:
                time.sleep(click_wait_time)
            element.click()
        except Exception as e:
            log.error(f"button click by xpath failed with an error = {e}")
            assert False

    def click_element_with_classname(self, element: str, wait_time: int = 0):
        log.info(f"click element with class name = {element}")
        try:
            click_wait_time = wait_time + self.get_click_wait_time()
            self.wait.until(EC.presence_of_element_located((AppiumBy.CLASS_NAME, element)))
            self.wait.until(EC.visibility_of_element_located((AppiumBy.CLASS_NAME, element)))
            self.wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, element)))
            element = self.driver.find_element(AppiumBy.CLASS_NAME, element)
            if click_wait_time:
                time.sleep(click_wait_time)
            element.click()
        except Exception as e:
            log.error(f"button click by classname failed with an error = {e}")
            assert False

    def send_keys(self, element: str, value):
        displayed_value = "*****" if 'password' in element.lower() else value
        log.info(f'send keys: {element}, {displayed_value}')
        self.wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, element)))
        self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, element)))
        element = self.driver.find_element(AppiumBy.XPATH, element).clear()
        element.send_keys(value)

    def click_element_with_accessibility_id(self, element: str, wait_time: int = 0) -> None:
        log.info(f"click element with id = {element}")
        try:
            click_wait_time = wait_time + self.get_click_wait_time()
            self.wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, element)))
            self.wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, element)))
            self.wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, element)))
            element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, element)
            if click_wait_time:
                time.sleep(click_wait_time)
            element.click()
        except Exception as e:
            log.error(f" click by ACCESSIBILITY_ID failed with an error = {e}")
            assert False

    def button_click_until_element_is_selected(self, element: str) -> WebElement:
        for i in range(0, 5):
            clicked_button = self.button_click(element)
            if clicked_button.get_attribute("selected") == "true":
                break
        return clicked_button

    def button_click_until_xpath_web_view_element_is_not_present(self, xpath: str, element_text: str) -> WebElement:
        button_present = True
        for i in range(0, 1):
            button = self.find_xpath_element_with_text(xpath, element_text)
            button.click()
            if button is not None:
                button_present = True
            else:
                button_present = False
                break
        return button_present

    def find_xpath_element_with_text(self, xpath: str, element_text: str) -> WebElement:
        elements = self.driver.find_elements(AppiumBy.XPATH, xpath)
        for i, element in enumerate(elements):
            if element.text == element_text:
                return element

    def find_elements_by_xpath(self, element):
        time.sleep(5)
        return self.driver.find_elements(AppiumBy.XPATH, element)

    def button_click_until_found_element_is_not_present(self, element: object) -> WebElement:
        button_present = True
        for i in range(0, 2):
            element.click()
            if element is not None:
                button_present = True
            else:
                button_present = False
                break
        return button_present

    def button_long_click(self, element: str) -> WebElement | None:
        print("Button long click {}".format(element))
        try:
            button = self.wait_for_element_visibility(element)
            actions = ActionChains(self.driver)
            actions.click_and_hold(button)
            actions.pause(10)
            actions.perform()
            return button
        except WebDriverException:
            return None

    def get_text_of_element(self, locator):
        log.info(f'get text of element: {locator}')
        self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        return self.driver.find_element(By.XPATH, locator).text

    def check_if_element_displayed(self, locator) -> bool:
        log.info(f'check if element displayed: {locator}')
        self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        return self.driver.find_element(By.XPATH, locator).is_displayed()

    def clear_input(self, locator):
        log.info(f'clear input: {locator}')
        self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        element = self.driver.find_element(By.XPATH, locator)
        time.sleep(1)
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACKSPACE)

    def wait_for_element_to_have_text(self, element: object) -> WebElement:
        log.info(f"wait for element to have text and element = {element}")
        try:
            for i in range(0, 5):
                if len(element.text) > 0:
                    log.info(f"Text found !! and text = {element.text}")
                    return element
                else:
                    sleep(.5)
        except WebDriverException:
            assert False

    def retry_wait_for_element(self, element: str) -> WebElement:

        locator = self.prepare_locator(element)
        for i in range(0, 5):
            try:
                found_element = WebDriverWait(self.driver, env.DEFAULT_DELAY).until(
                    EC.presence_of_element_located(locator))
                if found_element is not None:
                    return found_element
            except WebDriverException:
                pass

    def is_element_visible_by_accessibility_id(self, element: str, wait_time: int = env.DEFAULT_DELAY) -> bool:
        try:
            return WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located([AppiumBy.ACCESSIBILITY_ID, element])).is_displayed()
        except WebDriverException:
            return False

    def wait_for_element_by_id(self, element: str) -> WebElement:
        try:
            return WebDriverWait(self.driver, env.DEFAULT_DELAY).until(
                EC.presence_of_element_located([AppiumBy.ID, element]))
        except WebDriverException:
            assert False

    def take_screen_shot(self) -> None:
        log.info("Capturing screenshot")
        screenshot_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        try:
            sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name="CLOUDCALL_" + screenshot_time,
                          attachment_type=AttachmentType.PNG)
        except Exception as e:
            log.error("capture screen shot method failed with an error ==> {}".format(e))

    def wait_for_element_by_classname(self, element: str, delay=env.DEFAULT_DELAY) -> WebElement:
        try:
            return WebDriverWait(self.driver, delay).until(
                EC.presence_of_element_located([AppiumBy.CLASS_NAME, element]))
        except WebDriverException:
            assert False

    def wait_until_element_is_not_available(self, element, wait_time: int = env.DEFAULT_DELAY):
        """
        Wait until the element specified by the XPath is not available.

        """
        try:
            return WebDriverWait(self.driver, wait_time).until(
                EC.invisibility_of_element_located((AppiumBy.XPATH, element)))
        except WebDriverException:
            return False

    def make_screenshot(self, locator: str) -> str:
        element = self.wait_for_element_visibility(locator)
        return element.screenshot_as_base64

    def click_element_by_locator_and_index(self, locator: str, index: int) -> WebElement:
        """Find elements by locator, then among elements found click single element by text"""
        self.wait_for_element_visibility(locator)
        elements = self.driver.find_elements(By.ACCESSIBILITY_ID, locator)
        elements[index].click()
        return elements[index]

    def wait_until_element_is_stale(self, element: WebElement, delay: env.DEFAULT_DELAY):
        try:
            WebDriverWait(self.driver, delay).until(EC.staleness_of(element))
        except WebDriverException:
            return False

    @staticmethod
    def get_xpath_by_platform_from_dictionary(xpath_dict, element_key):
        """
        Returns the XPath for the given element key based on the current platform.
        """
        platform = PlatformConfig.platform  # Assign the imported platform variable

        platform_xpaths = xpath_dict.get(platform, {})

        return platform_xpaths.get(element_key)

    def hide_keyboard(self):
        self.driver.hide_keyboard()

    def wait_for_element_clickable_by_xpath(self, element: str, wait_time: int = env.DEFAULT_DELAY) -> WebElement:
        try:
            return WebDriverWait(self.driver, wait_time).until(
                EC.element_to_be_clickable([AppiumBy.XPATH, element]))
        except WebDriverException:
            assert False

    def scroll_up(self):

        screen_size = self.driver.get_window_size()
        screen_width = screen_size['width']
        screen_height = screen_size['height']

        start_x = screen_width / 2
        start_y = screen_height * 0.8
        end_y = screen_height * 2

        self.driver.swipe(start_x, start_y, start_x, end_y, 800)

        for _ in range(3):
            self.driver.swipe(start_x, start_y, start_x, end_y, 800)

    def scroll_down(self):

        screen_size = self.driver.get_window_size()
        screen_width = screen_size['width']
        screen_height = screen_size['height']

        start_x = screen_width / 2
        start_y = screen_height * 0.8
        end_y = screen_height * 0.2

        self.driver.swipe(start_x, start_y, start_x, end_y, 800)

        for _ in range(5):
            self.driver.swipe(start_x, start_y, start_x, end_y, 800)
