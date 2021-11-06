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

    """
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    """
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
