import json
import logging
import env
import pdb as pd
from appium import webdriver as appium_webdriver
from appium.options.android import UiAutomator2Options
from selenium.common import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

log = logging.getLogger(__name__)


class PlatformConfig:
    """This class required for keeping platforms configurations"""

    drivers = {}
    platform = ""
    is_signed_in = False
    driver_object = ""
    log.debug(f"Drivers instance {drivers} and platform value {platform}")

    def open_app(self, platform: str, reset: bool = False):
        first_launch = False
        """Open application and select desired capabilities for Appium depends on selected platform"""
        log.debug(f"Running open_app with platform name {platform} and with reset status as {reset}")
        if platform and PlatformConfig.platform != platform and platform not in PlatformConfig.drivers:
            PlatformConfig.platform = platform
            caps_dict = {
                env.ANDROID_PLATFORM_NAME.lower(): env.ANDROID_DESIRED_CAPABILITIES,
            }
            caps = caps_dict[platform.lower()]
            caps["fullReset"] = reset
            log.info(f"Desired capabilities of the application {caps}")
            options = UiAutomator2Options()
            options.load_capabilities(caps)
            log.debug("Initiating appium driver instance")
            PlatformConfig.driver_object = appium_webdriver.Remote(env.APPIUM_SERVER_HOST, options=options)
            first_launch = True
        PlatformConfig.drivers[PlatformConfig.platform] = PlatformConfig.driver_object
        log.info("PlatformConfig dict values are ==> {}".format(PlatformConfig.drivers))
        log.info("first launch = {} ".format(first_launch))
        return first_launch

    @staticmethod
    def quit():
        log.debug("quit driver instance")
        try:
            PlatformConfig.drivers[PlatformConfig.platform].quit()
            PlatformConfig.drivers = {}
            PlatformConfig.platform = ""
        finally:
            PlatformConfig.is_signed_in = False
        log.info(f"is_signed_in status after quit {PlatformConfig.is_signed_in}")
        log.debug("PlatformConfig.drivers {} & PlatformConfig.platform {}".format(PlatformConfig.drivers,
                                                                                  PlatformConfig.platform))

    @staticmethod
    def quit_all():
        log.debug("quit all driver instance")
        try:
            for driver in PlatformConfig.drivers:
                PlatformConfig.drivers[driver].quit()
                PlatformConfig.drivers = {}
                PlatformConfig.platform = ""
        finally:
            PlatformConfig.is_signed_in = False
            log.info(f"is_signed_in status after quit all {PlatformConfig.is_signed_in}")
