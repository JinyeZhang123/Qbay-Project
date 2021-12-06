import time

from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User

"""
This file defines all integration tests for the frontend homepage.
"""


class FrontEndHomePageTest(BaseCase):
    def test_buy_product_input_fail_balance(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "final00@qq.com")
        self.type("#name", "final00")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "final00@qq.com")
        self.type("#password", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open update product page
        self.open(base_url + '/create_product')

        self.type("#title", "327final00")
        bp_test0 = "kylekylekylekylekylekylekyleky" + \
                   "lekylekylekylekylekylekylekyle"
        self.type("#description", bp_test0)
        self.type("#price", "250.1")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "final00@qq.com")

        self.click('input[type="submit"]')

        # -----------------------------------------------------
        # create the second product on market
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "final01@qq.com")
        self.type("#name", "final01")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "final01@qq.com")
        self.type("#password", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        self.open(base_url + '/create_product')

        self.type("#title", "327final01")
        bptest1 = "kylekylekylekylekylekylekyleky" + \
                  "lekylekylekylekylekylekylekyle"
        self.type("#description", bptest1)
        self.type("#price", "50.1")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "final01@qq.com")

        self.click('input[type="submit"]')

        self.open(base_url + '/market')
        self.type("#title", "327final00")
        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#message")
        bp_message1 = "Purchase failed, check the product" + \
                      " title and your balance"
        self.assert_text(bp_message1, "#message")
        # other available APIs

    def test_buy_product_input_fail_seller(self, *_):
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "final02@qq.com")
        self.type("#name", "final02")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "final02@qq.com")
        self.type("#password", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open update product page
        self.open(base_url + '/create_product')
        bptest1 = "kylekylekylekylekylekylekyleky" + \
                  "lekylekylekylekylekylekylekyle"
        self.type("#title", "327final02")
        self.type("#description", bptest1)
        self.type("#price", "250.1")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "final02@qq.com")

        self.click('input[type="submit"]')

        # -----------------------------------------------------
        # create the second product on market
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "final03@qq.com")
        self.type("#name", "final03")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "final03@qq.com")
        self.type("#password", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        self.open(base_url + '/create_product')

        self.type("#title", "327final03")
        bptest2 = "kylekylekylekylekylekylekyleky" + \
                  "lekylekylekylekylekylekylekyle"
        self.type("#description", bptest2)
        self.type("#price", "50.1")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "final03@qq.com")

        self.click('input[type="submit"]')

        self.open(base_url + '/market')
        self.type("#title", "327final03")
        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#message")
        bp_message2 = "Purchase failed, check the product" + \
                      " title and your balance"
        self.assert_text(bp_message2, "#message")

    def test_buy_product_input_success(self, *_):
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "final04@qq.com")
        self.type("#name", "final04")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "final04@qq.com")
        self.type("#password", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open update product page
        self.open(base_url + '/create_product')

        self.type("#title", "327final04")
        bptest3 = "kylekylekylekylekylekylekyleky" + \
                  "lekylekylekylekylekylekylekyle"
        self.type("#description", bptest3)
        self.type("#price", "30.1")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "final04@qq.com")

        self.click('input[type="submit"]')

        # -----------------------------------------------------
        # create the second product on market
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "final05@qq.com")
        self.type("#name", "final05")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "final05@qq.com")
        self.type("#password", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        self.open(base_url + '/create_product')

        self.type("#title", "327final05")
        self.type("#description", bptest3)
        self.type("#price", "50.1")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "final05@qq.com")

        self.click('input[type="submit"]')

        self.open(base_url + '/market')
        self.type("#title", "327final04")
        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Order has been placed! check your account",
                         "#message")

    def test_buy_product_output_fail_seller(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "final06@qq.com")
        self.type("#name", "final06")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "final06@qq.com")
        self.type("#password", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open update product page
        self.open(base_url + '/create_product')

        self.type("#title", "327final06")
        bptest4 = "kylekylekylekylekylekylekyleky" + \
                  "lekylekylekylekylekylekylekyle"
        self.type("#description", bptest4)
        self.type("#price", "250.1")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "final06@qq.com")

        self.click('input[type="submit"]')

        # -----------------------------------------------------
        # create the second product on market
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "final07@qq.com")
        self.type("#name", "final07")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "final07@qq.com")
        self.type("#password", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open update product page
        self.open(base_url + '/create_product')

        self.type("#title", "327final07")

        self.type("#description", bptest4)
        self.type("#price", "50.1")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "final07@qq.com")

        self.click('input[type="submit"]')

        self.open(base_url + '/market')
        self.type("#title", "327final07")
        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text(
            "Purchase failed, check the product title and your balance",
            "#message")
        # other available APIs

    def test_buy_product_output_success(self, *_):
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "final08@qq.com")
        self.type("#name", "final08")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "final08@qq.com")
        self.type("#password", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open update product page
        self.open(base_url + '/create_product')

        self.type("#title", "327final08")
        bptest5 = "kylekylekylekylekylekylekyleky" + \
                  "lekylekylekylekylekylekylekyle"
        self.type("#description", bptest5)
        self.type("#price", "30.1")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "final08@qq.com")

        self.click('input[type="submit"]')

        # -----------------------------------------------------
        # create the second product on market
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "final09@qq.com")
        self.type("#name", "final09")
        self.type("#password", "1234567Aa!")
        self.type("#password2", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "final09@qq.com")
        self.type("#password", "1234567Aa!")
        # click enter button
        self.click('input[type="submit"]')

        self.open(base_url + '/create_product')

        self.type("#title", "327final09")

        self.type("#description", bptest5)
        self.type("#price", "50.1")
        self.type("#date", "2021-10-30")
        self.type("#owner_email", "final09@qq.com")

        self.click('input[type="submit"]')

        self.open(base_url + '/market')
        self.type("#title", "327final08")
        self.click('input[type="submit"]')

        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Order has been placed! check your account",
                         "#message")
