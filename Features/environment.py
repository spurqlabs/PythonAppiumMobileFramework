import json
from appium import webdriver
from allure_commons.types import AttachmentType
from allure_commons._allure import attach
from Features.Pages.BasePage import Basepage
from Features.Pages.android_Calculator_Page import android_Calculator_Page
from Features.Pages.iOS_Calculator_Page import iOS_Calculator_Page

data = json.load(open("Features/Resources/config.json"))


def before_feature(context, feature):
    tags = str(feature.tags)
    print("Tags " + tags)
    context.config.userdata["deviceType"] = tags
    print("Device Type :" + context.config.userdata["deviceType"])


def before_scenario(context, scenario):
    if context.config.userdata["executionMode"] == "Browserstack":
        if context.config.userdata["deviceType"] == "['iOS']":
            print(context.config.userdata["deviceType"])
            context.driver = webdriver.Remote(
                command_executor='https://' + context.config.userdata["userName"] + ':' + context.config.userdata[
                    "accessKey"] + '@hub-cloud.browserstack.com/wd/hub',
                desired_capabilities={
                    "platformName": "iOS",
                    "build": context.config.userdata["iOS_browserstack_build"],
                    "deviceName": context.config.userdata["iOS_browserstack_device"],
                    "os_version": context.config.userdata["iOS_device_os_version"],
                    "app": context.config.userdata["iOS_browserstack_appUrl"],

                }
            )
        else:
            context.driver = webdriver.Remote(
                command_executor='https://' + context.config.userdata["userName"] + ':' + context.config.userdata[
                    "accessKey"] + '@hub-cloud.browserstack.com/wd/hub',
                desired_capabilities={
                    "platformName": "android",
                    "build": context.config.userdata["android_browserstack_build"],
                    "deviceName": context.config.userdata["android_browserstack_device"],
                    "os_version": context.config.userdata["android_device_os_version"],
                    "app": context.config.userdata["android_browserstack_appUrl"],

                }
            )
    # elif context.config.userdata["executionMode"] == "Emulator":
    #     context.driver = webdriver.Remote(
    #         command_executor="http://localhost:4723/wd/hub",
    #         desired_capabilities={
    #             "platformName": context.config.userdata["platformName"],
    #             "deviceName": context.config.userdata["Emulator_deviceName"],
    #             "app": context.config.userdata["Emulator_app"],
    #             "appPackage": context.config.userdata["appPackage"],
    #             "appActivity": context.config.userdata["appActivity"]
    #
    #         }
    #     )
    # elif context.config.userdata["executionMode"] == "RealDevice":
    #     context.driver = webdriver.Remote(
    #         command_executor="http://localhost:4723/wd/hub",
    #         desired_capabilities={
    #             "platformName": context.config.userdata["platformName"],
    #             "build": context.config.userdata["realdevice_build"],
    #             "deviceName": context.config.userdata["realdevice_deviceName"],
    #             "os_version": context.config.userdata["realdevice_os_version"],
    #             "appPackage": context.config.userdata["appPackage"],
    #             "appActivity": context.config.userdata["appActivity"],
    #             "noReset": context.config.userdata["realdevice_noReset"],
    #             "newCommandTimeout": context.config.userdata["realdevice_newCommandTimeout"],
    #             "automationName": context.config.userdata["automationName"]
    #         })
    else:
        print("...")
    context.driver.switch_to.context('NATIVE_APP')
    baseobject = Basepage(context.driver)
    context.android_cal = android_Calculator_Page(baseobject)
    context.iOS_cal = iOS_Calculator_Page(baseobject)
    context.stepid = 1


def after_step(context, step):
    attach(context.driver.get_screenshot_as_png(), name=str(context.stepid), attachment_type=AttachmentType.PNG)
    context.stepid = context.stepid + 1


def after_scenario(context, scenario):
    context.driver.reset()
    context.driver.quit()
