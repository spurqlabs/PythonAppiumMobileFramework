from behave import *

use_step_matcher("parse")


@given("I am on calculator home page")
def step_impl(context):
    print("User is on Homepage")


@when("I enter '{number}'")
def step_impl(context, number):
    str = context.config.userdata["deviceType"]
    print("str " + str)
    if str == "['iOS']":
        context.iOS_cal.iOS_tap_number1(number)
    else:
        context.android_cal.tap_number1()


@step("I enter operator of addition")
def step_impl(context):
    str = context.config.userdata["deviceType"]
    print("str " + str)
    if str == "['iOS']":
        context.iOS_cal.iOS_tap_operator()
    else:
        context.android_cal.tap_operator()


@step("Enter number '{number}'")
def step_impl(context, number):
    str = context.config.userdata["deviceType"]
    print("str " + str)
    if str == "['iOS']":
        context.iOS_cal.iOS_tap_number1(number)
    else:
        context.android_cal.tap_number2()


@step("I enter operator '{operator}'")
def step_impl(context, operator):
    str = context.config.userdata["deviceType"]
    print("str " + str)
    if str == "['iOS']":
        context.iOS_cal.iOS_equals(operator)
    else:
        context.android_cal.equals()


@then("I see result as '{result}'")
def step_impl(context, result):
    str = context.config.userdata["deviceType"]
    print("str " + str)
    if str == "['iOS']":
        flag = context.iOS_cal.iOS_verify_result()
        assert flag == True
    else:
        flag = context.android_cal.verify_result()
        assert flag == True
