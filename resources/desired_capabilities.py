from appium import webdriver

def get_desired_capabilities():
    desired_caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "app": "C:/Users/georg/Desktop/SoarInterview/mobileAppAutomation/WikipediaSample.apk",
        "appPackage": "org.wikipedia.alpha",
        "appActivity": "org.wikipedia.main.MainActivity",
        "deviceName": "Pixel2",
        "platformVersion": "9.0.0",
        "udid": "emulator-5554"
    }
    return desired_caps