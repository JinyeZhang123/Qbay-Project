import time

from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User

"""
This file defines all integration tests for the frontend homepage.
"""


class FrontEndHomePageTest(BaseCase):

    def test_create_product_input_success(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """

        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "01kyle@test.com")
        self.type("#name", "kyle001")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "01kyle@test.com")
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

        # open create product page
        self.open(base_url + '/create_product')

        self.type("#title", "queens01")
        self.type("#description", "this is akylekyel kyle kyle\
                                    kyle kyle product!!!!")
        self.type("#price", "888.8")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "01kyle@test.com")

        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Welcome kyle001 !", "#welcome-header")
        # other available APIs

    def test_create_product_input_title_false(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """

        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "02kyle@test.com")
        self.type("#name", "kyle002")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "02kyle@test.com")
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

        # open create product page
        self.open(base_url + '/create_product')

        self.type("#title", "hahaha")
        self.type("#description", "this aaaais a kyle kyle\
                                    kyle kyle product!!!!")
        self.type("#price", "888.8")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "02kyle@test.com")

        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Creation Failed", "#message")
        # other available APIs

    def test_create_product_input_description_false(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "03kyle@test.com")
        self.type("#name", "kyle003")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "03kyle@test.com")
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

        # open create product page
        self.open(base_url + '/create_product')

        self.type("#title", "kyle615")
        self.type("#description", "kyle")
        self.type("#price", "888.8")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "03kyle@test.com")

        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Creation Failed", "#message")
        # other available APIs

    def test_create_product_input_price_false(self, *_):

        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "04kyle@test.com")
        self.type("#name", "kyle004")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "04kyle@test.com")
        self.type("#password", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')
        self.open(base_url + '/create_product')

        self.type("#title", "kyle0615")
        self.type("#description", "kylekylekylekylekylekylekyleky\
                                    lekylekylekylekylekylekylekyle")
        self.type("#price", "1")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "04kyle@test.com")

        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Creation Failed", "#message")
        # other available APIs

    def test_create_product_input_date_false(self, *_):
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "05kyle@test.com")
        self.type("#name", "kyle005")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "05kyle@test.com")
        self.type("#password", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')
        self.open(base_url + '/create_product')

        self.type("#title", "kyle0615")
        self.type("#description", "kylekylekylekylekylekylekyleky\
                                    lekylekylekylekylekylekylekyle")
        self.type("#price", "111.12")
        self.type("#date", "2030-10-30")
        self.type("#owner_email", "05kyle@test.com")

        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Creation Failed", "#message")
        # other available APIs

    def test_create_product_input_owner_false(self, *_):
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "06kyle@test.com")
        self.type("#name", "kyle006")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "06kyle@test.com")
        self.type("#password", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')
        self.open(base_url + '/create_product')

        self.type("#title", "kyle061511")
        self.type("#description", "kylekylekylekylekylekylekylekyl\
                                    ekylekylekylekylekylekylekyle")
        self.type("#price", "111.111")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "yes bitch")

        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Creation Failed", "#message")
        # other available APIs

    def test_create_product_output_success(self, *_):

        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "07kyle@test.com")
        self.type("#name", "kyle007")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "07kyle@test.com")
        self.type("#password", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')
        self.open(base_url + '/create_product')

        self.type("#title", "1kyle0615")
        self.type("#description", "kylekylekylekylekylekylekyleky\
                                    lekylekylekylekylekylekylekyle")
        self.type("#price", "122.2")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "07kyle@test.com")

        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Welcome kyle007 !", "#welcome-header")
        # other available APIs

    def test_create_product_output_fail(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "08kyle@test.com")
        self.type("#name", "kyle008")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "08kyle@test.com")
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

        # open create product page
        self.open(base_url + '/create_product')

        self.type("#title", "kyle70615")
        self.type("#description", "kylekylekylekylekylekylekylekyl\
                                    ekylekylekylekylekylekylekyle")
        self.type("#price", "1")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "08kyle@test.com")

        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Creation Failed", "#message")

    def test_create_product_functionality_success(self, *_):

        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "09kyle@test.com")
        self.type("#name", "kyle009")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "09kyle@test.com")
        self.type("#password", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')
        self.open(base_url + '/create_product')

        self.type("#title", "1yle0615")
        self.type("#description", "kylekylekylekylekylekylekylekyle\
                                    kylekylekylekylekylekylekyle")
        self.type("#price", "122.2")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "09kyle@test.com")

        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Welcome kyle009 !", "#welcome-header")
        # other available APIs

    def test_create_product_functionality_fail(self, *_):
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "10kyle@test.com")
        self.type("#name", "kyle010")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "10kyle@test.com")
        self.type("#password", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')
        self.open(base_url + '/create_product')

        self.type("#title", "12le0615")
        self.type("#description", "kylekylekylekylekylekylekylekyle\
                                    kylekylekylekylekylekylekyle")
        self.type("#price", "2")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "10kyle@test.com")

        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Creation Failed", "#message")

