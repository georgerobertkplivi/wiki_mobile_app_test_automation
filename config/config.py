class Config:
    CAPABILITIES = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "app": "C:/Users/georg/Desktop/SoarInterview/mobileAppAutomation/WikipediaSample.apk",
        "appPackage": "org.wikipedia.alpha",
        "appActivity": "org.wikipedia.main.MainActivity",
        "deviceName": "Pixel2",
        "platformVersion": "9.0.0",
        "udid": "emulator-5554"
    }
    
    APPIUM_SERVER = "http://localhost:4723/wd/hub"
    
    IMPLICIT_WAIT = 10 