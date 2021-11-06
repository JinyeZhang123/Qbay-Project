import time

from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User

"""
This file defines all integration tests for the frontend homepage.
"""


class FrontEndHomePageTest(BaseCase):
    def test_register_success_input(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "test2@test.com")
        self.type("#name", "r00r02")
        self.type("#password", "123456Aa!")
        self.type("#password2", "123456Aa!")
        # click enter button
        self.click('input[type="submit"]')

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Please login", "#message")
        # other available APIs

    """
    False case: invalid email
    """

    def test_register_email_fail_input(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "test0")
        self.type("#name", "r00r01")
        self.type("#password", "123456Aa!")
        self.type("#password2", "123456Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # after clicking on the browser (the line above)
        # the front-end code is activated
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics.
        # so we patch the backend to return a specific user instance,
        # rather than running that program. (see @ annotations above)

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Registration failed.", "#message")

    def test_register_name_fail_input(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "test1@qq.com")
        self.type("#name", "1")
        self.type("#password", "123456Aa!")
        self.type("#password2", "123456Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # after clicking on the browser (the line above)
        # the front-end code is activated
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics.
        # so we patch the backend to return a specific user instance,
        # rather than running that program. (see @ annotations above)

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Registration failed.", "#message")

    def test_register_password_fail_input(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "test0@qq.com")
        self.type("#name", "r00r00")
        self.type("#password", "123456Aa!")
        self.type("#password2", "12345")
        # click enter button
        self.click('input[type="submit"]')

        # after clicking on the browser (the line above)
        # the front-end code is activated
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics.
        # so we patch the backend to return a specific user instance,
        # rather than running that program. (see @ annotations above)

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")

    def test_register_success_output(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "1test0@test01.com")
        self.type("#name", "1r00r0")
        self.type("#password", "123456Aa!")
        self.type("#password2", "123456Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # after clicking on the browser (the line above)
        # the front-end code is activated
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics.
        # so we patch the backend to return a specific user instance,
        # rather than running that program. (see @ annotations above)

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

    def test_register_fail_output(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "tgttttt")
        self.type("#name", "2r00r0")
        self.type("#password", "123456Aa!")
        self.type("#password2", "123456Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # after clicking on the browser (the line above)
        # the front-end code is activated
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics.
        # so we patch the backend to return a specific user instance,
        # rather than running that program. (see @ annotations above)

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Registration failed.", "#message")

    def test_register_register_fail_functionality(self, *_):
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "michael1")
        self.type("#name", "asd87a8")
        self.type("#password", "123456Aa!")
        self.type("#password2", "123456Aa!")
        # click enter button
        self.click('input[type="submit"]')

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Registration failed.", "#message")

    def test_register_register_success_functionality(self, *_):
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "caijixiaomc876@gmail.com")
        self.type("#name", "ioubtgvo9")
        self.type("#password", "123456Aa!")
        self.type("#password2", "123456Aa!")
        # click enter button
        self.click('input[type="submit"]')

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

# Login input test
    def test_login_success_input(self, *_):
        # open register page to create account
        self.open(base_url + '/register')
        # type email
        self.type("#email", "caijixiaomc2@gmail.com")
        # type user name
        self.type("#name", "caijixiaomc2")
        # type password
        self.type("#password", "123456Aa!")
        # retype password
        self.type("#password2", "123456Aa!")
        # click enter button
        self.click('input[type="submit"]')
        # type email
        self.type("#email", "caijixiaomc2@gmail.com")
        # type password
        self.type("#password", "123456Aa!")
        # click submit
        self.click('input[type="submit"]')

        time.sleep(1)

        self.assert_element("#welcome-header")
        self.assert_text("Welcome caijixiaomc2 !", "#welcome-header")

    def test_login_fail_email_input(self, *_):
        self.open(base_url + '/register')
        # open register page to create account
        self.type("#email", "caijixiaomc3@gmail.com")
        # type email
        self.type("#name", "caijixiaomc3")
        # type user name
        self.type("#password", "123456Aa!")
        # type password
        self.type("#password2", "123456Aa!")
        # retype password
        self.click('input[type="submit"]')
        # click enter button

        self.type("#email", "caijixiao3")
        # type email
        self.type("#password", "123456Aa!")
        # type password
        self.click('input[type="submit"]')
        # click submit

        time.sleep(1)
        # test if the page loads correctly

        self.assert_element("#message")
        self.assert_text("login failed", "#message")

    def test_login_fail_password_input(self, *_):
        self.open(base_url + '/register')
        # open register page to create account
        self.type("#email", "caijixiaomc4@gmail.com")
        # type email
        self.type("#name", "caijixiaomc4")
        # type user name
        self.type("#password", "123456Aa!")
        # type password
        self.type("#password2", "123456Aa!")
        # retype password
        self.click('input[type="submit"]')
        # click enter button

        self.type("#email", "caijixiaomc4@gmail.com")
        # type email
        self.type("#password", "1")
        # type password
        self.click('input[type="submit"]')
        # click submit

        time.sleep(1)

        self.assert_element("#message")
        self.assert_text("login failed", "#message")

# Login output test

    def test_login_success_input1(self, *_):
        self.open(base_url + '/register')
        # open register page to create account
        self.type("#email", "caijixiaomc5@gmail.com")  # type email
        self.type("#name", "caijixiaomc5")  # type user name
        self.type("#password", "123456Aa!")  # type password
        self.type("#password2", "123456Aa!")  # retype password
        self.click('input[type="submit"]')  # click enter button

        self.type("#email", "caijixiaomc5@gmail.com")  # type email
        self.type("#password", "123456Aa!")  # type password
        self.click('input[type="submit"]')  # click submit

        time.sleep(1)  # test if the page loads correctly

        self.assert_element("#welcome-header")
        self.assert_text("Welcome caijixiaomc5 !", "#welcome-header")

    def test_login_fail_input(self, *_):
        self.open(base_url + '/register')
        # open register page to create account
        self.type("#email", "caijixiaomc6@gmail.com")
        # type email
        self.type("#name", "caijixiaomc6")
        # type user name
        self.type("#password", "123456Aa!")
        # type password
        self.type("#password2", "123456Aa!")
        # retype password
        self.click('input[type="submit"]')
        # click enter button

        self.type("#email", "caijixiaomc6@gmail.com")
        # type email
        self.type("#password", "12456Aa!")
        # type password
        self.click('input[type="submit"]')
        # click submit

        time.sleep(1)

        self.assert_element("#message")
        self.assert_text("login failed", "#message")

    # Login functionality test

    def test_login_login_success_functionality(self, *_):
        self.open(base_url + '/register')
        # open register page to create account
        self.type("#email", "caijixiaomc7@gmail.com")
        # type email
        self.type("#name", "caijixiaomc7")
        # type user name
        self.type("#password", "123456Aa!")
        # type password
        self.type("#password2", "123456Aa!")
        # retype password
        self.click('input[type="submit"]')
        # click enter button

        self.type("#email", "caijixiaomc7@gmail.com")
        # type email
        self.type("#password", "123456Aa!")
        # type password
        self.click('input[type="submit"]')
        # click submit

        time.sleep(1)

        self.assert_element("#welcome-header")
        self.assert_text("Welcome caijixiaomc7 !", "#welcome-header")

    def test_login_login_fail_functionality(self, *_):
        self.open(base_url + '/register')
        # open register page to create account
        self.type("#email", "caijixiaomc8@gmail.com")
        # type email
        self.type("#name", "caijixiaomc8")
        # type user name
        self.type("#password", "123456Aa!")
        # type password
        self.type("#password2", "123456Aa!")
        # retype password
        self.click('input[type="submit"]')
        # click enter button

        self.type("#email", "caijixiaomc8@gmail.com")
        # type email
        self.type("#password", "12456Aa!")
        # type password
        self.click('input[type="submit"]')
        # click submit

        time.sleep(1)

        self.assert_element("#message")
        self.assert_text("login failed", "#message")

    # Update user profile input test
    def test_UpdateUserProfile_success_input(self, *_):
        self.open(base_url + '/register')
        # open register page to create account
        self.type("#email", "caijixiaomc11@gmail.com")
        # type email
        self.type("#name", "caijixiaomc11")
        # type user name
        self.type("#password", "123456Aa!")
        # type password
        self.type("#password2", "123456Aa!")
        # retype password
        self.click('input[type="submit"]')
        # click enter button

        self.open(base_url + '/login')
        # open register page to create account
        self.type("#email", "caijixiaomc11@gmail.com")
        # type email
        self.type("#password", "123456Aa!")
        # type password
        self.click('input[type="submit"]')
        # click submit
        self.open(base_url + '/update_user_profile')

        # enter home

        """
        Click Update User Profile 
        """
        # enter update user profile
        self.type("#email", "caijixiaomc11@gmail.com")
        # type email
        self.type("#name", "caijixiaomc11")
        # type user name
        self.type("#address", "58elm")
        # type address
        self.type("#postcode", "K7L 2Y1")
        # type postcode
        self.click('input[type="submit"]')
        # click submit

        # test if the page loads correctly

        self.assert_element("#welcome-header")
        self.assert_text("Welcome caijixiaomc11 !", "#welcome-header")

    def test_UpdateUserProfile_fail_email_input(self, *_):
        self.open(base_url + '/register')
        # open register page to create account
        self.type("#email", "caijixiaomc12@gmail.com")
        # type email
        self.type("#name", "caijixiaomc12")
        # type user name
        self.type("#password", "123456Aa!")
        # type password
        self.type("#password2", "123456Aa!")
        # retype password
        self.click('input[type="submit"]')
        # click enter button

        self.open(base_url + '/login')
        # open register page to create account
        self.type("#email", "caijixiaomc12@gmail.com")
        # type email
        self.type("#password", "123456Aa!")
        # type password
        self.click('input[type="submit"]')
        # click submit
        self.open(base_url + '/update_user_profile')
        # click href

        # enter home
        # enter update user profile
        self.type("#email", "caijixiaomc12")
        # type email
        self.type("#name", "caijixiaomc12")
        # type user name
        self.type("#address", "58elm")
        # type address
        self.type("#postcode", "K7L 2Y1")
        # type postcode
        self.click('input[type="submit"]')
        # click submit
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Update failed.", "#message")

    def test_UpdateUserProfile_fail_username_input(self, *_):
        self.open(base_url + '/register')
        # open register page to create account
        self.type("#email", "caijixiaomc13@gmail.com")
        # type email
        self.type("#name", "caijixiaomc13")
        # type user name
        self.type("#password", "123456Aa!")
        # type password
        self.type("#password2", "123456Aa!")
        # retype password
        self.click('input[type="submit"]')
        # click enter button
        self.open(base_url + '/login')
        # open register page to create account
        self.type("#email", "caijixiaomc13@gmail.com")
        # type email
        self.type("#password", "123456Aa!")
        # type password
        self.click('input[type="submit"]')
        # click submit
        self.open(base_url + '/update_user_profile')

        # enter home
        # enter update user profile
        self.type("#email", "caijixiaomc13@gmail.com")
        # type email
        self.type("#name", "c")
        # type user name
        self.type("#address", "58elm")
        # type address
        self.type("#postcode", "K7L 2Y1")
        # type postcode
        self.click('input[type="submit"]')
        # click submit
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Update failed.", "#message")

    def test_UpdateUserProfile_fail_address_input(self, *_):
        self.open(base_url + '/register')
        # open register page to create account
        self.type("#email", "caijixiaomc14@gmail.com")
        # type email
        self.type("#name", "caijixiaomc14")
        # type user name
        self.type("#password", "123456Aa!")
        # type password
        self.type("#password2", "123456Aa!")
        # retype password
        self.click('input[type="submit"]')
        # click enter button
        self.open(base_url + '/login')
        # open register page to create account
        self.type("#email", "caijixiaomc14@gmail.com")
        # type email
        self.type("#password", "123456Aa!")
        # type password
        self.click('input[type="submit"]')
        # click submit
        self.open(base_url + '/update_user_profile')

        # enter home
        # enter update user profile
        self.type("#email", "caijixiaomc14@gmail.com")
        # type email
        self.type("#name", "caijixiaomc14")
        # type user name
        self.type("#address", "&^%")
        # type address
        self.type("#postcode", "K7L 2Y1")
        # type postcode
        self.click('input[type="submit"]')
        # click submit
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Update failed.", "#message")

    def test_UpdateUserProfile_fail_postcode_input(self, *_):
        self.open(base_url + '/register')
        # open register page to create account
        self.type("#email", "caijixiaomc15@gmail.com")
        # type email
        self.type("#name", "caijixiaomc15")
        # type user name
        self.type("#password", "123456Aa!")
        # type password
        self.type("#password2", "123456Aa!")
        # retype password
        self.click('input[type="submit"]')
        # click enter button
        self.open(base_url + '/login')
        # open register page to create account
        self.type("#email", "caijixiaomc15@gmail.com")
        # type email
        self.type("#password", "123456Aa!")
        # type password
        self.click('input[type="submit"]')
        # click submit
        self.open(base_url + '/update_user_profile')

        # enter home
        # enter update user profile
        self.type("#email", "caijixiaomc15@gmail.com")
        # type email
        self.type("#name", "caijixiaomc15")
        # type user name
        self.type("#address", "58elm")
        # type address
        self.type("#postcode", "lpllp")
        # type postcode
        self.click('input[type="submit"]')
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Update failed.", "#message")

# Update user profile output test

    def test_UpdateUserProfile_success_output(self, *_):
        self.open(base_url + '/register')
        # open register page to create account
        self.type("#email", "caijixiaomc16@gmail.com")
        # type email
        self.type("#name", "caijixiaomc16")
        # type user name
        self.type("#password", "123456Aa!")
        # type password
        self.type("#password2", "123456Aa!")
        # retype password
        self.click('input[type="submit"]')
        # click enter button

        self.open(base_url + '/login')
        # open register page to create account
        self.type("#email", "caijixiaomc16@gmail.com")
        # type email
        self.type("#password", "123456Aa!")
        # type password
        self.click('input[type="submit"]')
        # click submit
        self.open(base_url + '/update_user_profile')

        # enter home
        # enter update user profile
        self.type("#email", "caijixiaomc16@gmail.com")
        # type email
        self.type("#name", "caijixiaomc16")
        # type user name
        self.type("#address", "58elm")
        # type address
        self.type("#postcode", "K7L 2Y1")
        # type postcode
        self.click('input[type="submit"]')
        # click submit

        # test if the page loads correctly

        self.assert_element("#welcome-header")
        self.assert_text("Welcome caijixiaomc16 !", "#welcome-header")

    def test_UpdateUserProfile_fail_output(self, *_):
        self.open(base_url + '/register')
        # open register page to create account
        self.type("#email", "caijixiaomc17@gmail.com")
        # type email
        self.type("#name", "caijixiaomc17")
        # type user name
        self.type("#password", "123456Aa!")
        # type password
        self.type("#password2", "123456Aa!")
        # retype password
        self.click('input[type="submit"]')
        # click enter button
        self.open(base_url + '/login')
        # open register page to create account
        self.type("#email", "caijixiaomc17@gmail.com")
        # type email
        self.type("#password", "123456Aa!")
        # type password
        self.click('input[type="submit"]')
        # click submit
        self.open(base_url + '/update_user_profile')

        # enter home
        # enter update user profile
        self.type("#email", "caijixiaomc17@gmail.com")
        # type email
        self.type("#name", "caijixiaomc17")
        # type user name
        self.type("#address", "58elm")
        # type address
        self.type("#postcode", "lpllp")
        # type postcode
        self.click('input[type="submit"]')
        # click submit
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Update failed.", "#message")

# Update User Profile Functionality Test
    def test_UpdateUserProfile_success_functionlity(self, *_):

        self.open(base_url + '/register')
        # open register page to create account
        self.type("#email", "caijixiaomc18@gmail.com")
        # type email
        self.type("#name", "caijixiaomc18")
        # type user name
        self.type("#password", "123456Aa!")
        # type password
        self.type("#password2", "123456Aa!")
        # retype password
        self.click('input[type="submit"]')
        # click enter button

        self.open(base_url + '/login')
        # open register page to create account
        self.type("#email", "caijixiaomc18@gmail.com")
        # type email
        self.type("#password", "123456Aa!")
        # type password
        self.click('input[type="submit"]')
        # click submit
        self.open(base_url + '/update_user_profile')

        # enter home
        # enter update user profile
        self.type("#email", "caijixiaomc18@gmail.com")
        # type email
        self.type("#name", "caijixiaomc18")
        # type user name
        self.type("#address", "58elm")
        # type address
        self.type("#postcode", "K7L 2Y1")
        # type postcode
        self.click('input[type="submit"]')
        # click submit

        # test if the page loads correctly

        self.assert_element("#welcome-header")
        self.assert_text("Welcome caijixiaomc18 !", "#welcome-header")

    def test_UpdateUserProfile_fail_functionality(self, *_):
        self.open(base_url + '/register')
        # open register page to create account
        self.type("#email", "caijixiaomc19@gmail.com")
        # type email
        self.type("#name", "caijixiaomc19")
        # type user name
        self.type("#password", "123456Aa!")
        # type password
        self.type("#password2", "123456Aa!")
        # retype password
        self.click('input[type="submit"]')
        # click enter button

        self.open(base_url + '/login')
        # open register page to create account
        self.type("#email", "caijixiaomc19@gmail.com")
        # type email
        self.type("#password", "123456Aa!")
        # type password
        self.click('input[type="submit"]')
        # click submit
        self.open(base_url + '/update_user_profile')

        # enter home
        # enter update user profile
        self.type("#email", "caijixiaomc19@gmail.com")
        # type email
        self.type("#name", "caijixiaomc19")
        # type user name
        self.type("#address", "58elm")
        # type address
        self.type("#postcode", "lpllp")
        # type postcode
        self.click('input[type="submit"]')
        # click submit
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Update failed.", "#message")
