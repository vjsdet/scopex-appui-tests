# Scopex-MobileApp-Tests

Automated tests fot Scopex project

- UI tests

## Setup

Tests requires [Python](https://www.python.org/) v3.10+ to run.

[Android Studio](https://developer.android.com/studio) is required.

run Android Studio:

- In upper menu press "Tools" -> "Troubleshoot Device Connections"
- Press "Rescan devices" button
- After rescaning the name of the devices ready for debugging will be listed
- If the name is different with "emulator-5554", update variable **"ANDROID_SIMULATOR_DEVICE"** in [env.py](./env.py) file

## Running Appium Server and Appium Inspector

For opening Android application in simulator, Appium must be configured before.

In settings of the Appium Server the paths for Environment variables **"ANDROID_HOME"** and **"JAVA_HOME"** must be provided.<br>
The server should be started on **localhost** with **4723** port (as by default)

In Appium Inspector following desired capabilities are required for Android simulator session:
```json
{
  "platformName": "Android",
  "appium:udid": "emulator-5554",
  "appium:platformVersion": "11",
  "appium:app": "path\\to\\apk\\file.apk"
}
```
## Install Requirements
To required python packages
```shell
pip install -r requirements.txt
```

## Run tests
For running tests there are two ways:
1. Run all tests
```shell
behave --no-logcapture --no-capture -t @sanity
```
2. Run specified test
```shell
behave --no-logcapture --no-capture -i ui/features/sign_in_page_navigations.feature
```

## Allure report
For creating allure report after tests run command
```shell
allure serve ./allure-results/
```
