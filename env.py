"""File to store environment variables"""
import os

# Common variables
DEFAULT_DELAY = 3
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# Common UI variables
APPIUM_SERVER_HOST = "http://127.0.0.1:4723"
ANDROID_PLATFORM_NAME = "Android"

# Desired capabilities variables
ANDROID_DESIRED_CAPABILITIES = {
    "appium:platformName": ANDROID_PLATFORM_NAME,
    "appium:udid": "emulator-5554",
    "appium:platformVersion": "11",
    "appium:app": ROOT_DIR + "/builds/ScopeX-699.apk",
    "appium:ensureWebviewsHavePages": False,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True,
    "appium:autoGrantPermissions": True,
    "allowInvisibleElements": True,
    "appium:automationName": "UiAutomator2"
}
