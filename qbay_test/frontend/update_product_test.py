import time

from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User

"""
This file defines all integration tests for the frontend homepage.
"""


class FrontEndHomePageTest(BaseCase):
    def test_update_product_input_success(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        self.open(base_url + '/register')
            # fill email and password
        self.type("#email", "shabi01@test.com")
        self.type("#name", "shabi001")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
            # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "shabi01@test.com")
        self.type("#password", "1234567Aa!")
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

        # open update product page
        self.open(base_url + '/create_product')

        self.type("#title", "nanshoua01")
        self.type("#description", "kylekylekylekylekylekylekylekylekylekylekylekylekylekylekyle")
        self.type("#price", "122.2")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "shabi01@test.com")

        self.click('input[type="submit"]')

        self.open(base_url + '/update_product')

        self.type("#title", "nanshoua01")
        self.type("#new_title", "nanshoua02")
        self.type("#description", "this iss a kyle kyle kyle kyle product!!!!")
        self.type("#price", "888.81")



        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Welcome shabi001 !", "#welcome-header")
        # other available APIs

    def test_update_product_input_title_fail(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "shabi02@test.com")
        self.type("#name", "shabi002")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "shabi02@test.com")
        self.type("#password", "1234567Aa!")
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

        # open update product page
        self.open(base_url + '/create_product')

        self.type("#title", "nanshoua03")
        self.type("#description", "kylekylekylekylekylekylekylekylekylekylekylekylekylekylekyle")
        self.type("#price", "122.2")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "shabi02@test.com")

        self.click('input[type="submit"]')

        self.open(base_url + '/update_product')

        self.type("#title", "nanshoua03")
        self.type("#new_title", "nanshoua")
        self.type("#description", "this iss a kyle kyle kyle kyle product!!!!")
        self.type("#price", "888.81")

        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Product update failed.", "#message")
        # other available APIs


    def test_update_product_input_description_fail(self, *_):
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "shabi03@test.com")
        self.type("#name", "shabi003")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "shabi03@test.com")
        self.type("#password", "1234567Aa!")
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

        # open update product page
        self.open(base_url + '/create_product')

        self.type("#title", "nanshoua04")
        self.type("#description", "kylekylekylekylekylekylekylekylekylekylekylekylekylekylekyle")
        self.type("#price", "122.2")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "shabi03@test.com")

        self.click('input[type="submit"]')

        self.open(base_url + '/update_product')

        self.type("#title", "nanshoua04")
        self.type("#new_title", "nanshoua05")
        self.type("#description", "this!")
        self.type("#price", "888.81")

        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Product update failed.", "#message")

    def test_update_product_input_price_fail(self, *_):
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "shabi04@test.com")
        self.type("#name", "shabi004")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "shabi04@test.com")
        self.type("#password", "1234567Aa!")
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

        # open update product page
        self.open(base_url + '/create_product')

        self.type("#title", "nanshoua07")
        self.type("#description", "kylekylekylekylekylekylekylekylekylekylekylekylekylekylekyle")
        self.type("#price", "122.2")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "shabi04@test.com")

        self.click('input[type="submit"]')

        self.open(base_url + '/update_product')

        self.type("#title", "nanshoua07")
        self.type("#new_title", "nanshoua08")
        self.type("#description", "this iss a kyle kyle kyle kyle product!!!!")
        self.type("#price", "3")

        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Product update failed.", "#message")

    def test_update_product_output_success(self, *_):
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "shabi05@test.com")
        self.type("#name", "shabi005")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "shabi05@test.com")
        self.type("#password", "1234567Aa!")
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

        # open update product page
        self.open(base_url + '/create_product')

        self.type("#title", "nanshou01")
        self.type("#description", "kylekylekylekylekylekylekylekylekylekylekylekylekylekylekyle")
        self.type("#price", "122.2")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "shabi05@test.com")

        self.click('input[type="submit"]')

        self.open(base_url + '/update_product')

        self.type("#title", "nanshou01")
        self.type("#new_title", "nanshoua11")
        self.type("#description", "this iss a kyle kyle kyle kyle product!!!!")
        self.type("#price", "888.81")

        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Welcome shabi005 !", "#welcome-header")


    def test_update_product_output_fail(self, *_):
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "shabi06@test.com")
        self.type("#name", "shabi006")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "shabi06@test.com")
        self.type("#password", "1234567Aa!")
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

        # open update product page
        self.open(base_url + '/create_product')

        self.type("#title", "nanshou6")
        self.type("#description", "kylekylekylekylekylekylekylekylekylekylekylekylekylekylekyle")
        self.type("#price", "122.2")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "shabi06@test.com")

        self.click('input[type="submit"]')

        self.open(base_url + '/update_product')

        self.type("#title", "nanshoua6")
        self.type("#new_title", "nansh")
        self.type("#description", "this iss a kyle kyle kyle kyle product!!!!")
        self.type("#price", "3")

        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Product update failed.", "#message")
    def test_update_product_functionality_success(self, *_):

        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "shabi07@test.com")
        self.type("#name", "shabi007")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "shabi07@test.com")
        self.type("#password", "1234567Aa!")
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

        # open update product page
        self.open(base_url + '/create_product')

        self.type("#title", "haonanshoua01")
        self.type("#description", "kylekylekylekylekylekylekylekylekylekylekylekylekylekylekyle")
        self.type("#price", "122.2")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "shabi07@test.com")

        self.click('input[type="submit"]')

        self.open(base_url + '/update_product')

        self.type("#title", "haonanshoua01")
        self.type("#new_title", "nansho18980")
        self.type("#description", "this iss a kyle kyle kyle kyle product!!!!")
        self.type("#price", "888.81")

        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Welcome shabi007 !", "#welcome-header")

    def test_update_product_functionality_fail(self, *_):
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "shabi08@test.com")
        self.type("#name", "shabi008")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "shabi08@test.com")
        self.type("#password", "1234567Aa!")
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

        # open update product page
        self.open(base_url + '/create_product')

        self.type("#title", "finally01")
        self.type("#description", "kylekylekylekylekylekylekylekylekylekylekylekylekylekylekyle")
        self.type("#price", "122.2")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "shabi08@test.com")

        self.click('input[type="submit"]')

        self.open(base_url + '/update_product')

        self.type("#title", "finally01")
        self.type("#new_title", "naoua")
        self.type("#description", "this iss a kyle kyle kyle kyle product!!!!")
        self.type("#price", "888.81")

        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Product update failed.", "#message")
        # other available APIs