import random
import string

import re

from qbay.models import register, login, create_product, \
    update_user_profile, update_product


def test_r1_7_user_register():
    """
    Testing R1-7: If the email has been used, the operation failed.
    """

    assert register('r17u0', 'r171test0@test.com', '123456Aa*') is True
    assert register('r17u0', 'r172test1@test.com', '123456Aa*') is True
    assert register('r17u1', 'r172test1@test.com', '123456Aa*') is False


def test_r1_1_user_register():
    # R1-1: Both the email and password cannot be empty.
    assert register('u0r11', '', '') is False


def test_r1_3_user_register():
    # 1-3: The email has to follow addr-spec defined in RFC 5322
    # (see https://en.wikipedia.org/wiki/Email_address for a human-friendly
    assert register('r13u0', 'asdwaff@@', '123456aA*') is False
    assert register('r13u0', 'caijixiaomc@gmail.com', '123456aA*') is True


def test_r1_4_user_register():
    # R1-4: Password has to meet the required complexity: minimum length 6,
    # at least one upper case, at least one lower case,
    # and at least 1 special char
    assert register('r14u0', 'r141test0@test.com', '12345') is False
    assert register('r14u0', 'r142test0@test.com', '123456') is False
    assert register('r14u0', 'r143test0@test.com', '123456A') is False
    assert register('r14u0', 'r144test0@test.com', '123456Aa') is False
    assert register('r14u0', 'r145test0@test.com', '123456a') is False
    assert register('r14u0', 'r146test5@test.com', '123456aA*') is True


def test_r1_5_user_register():
    # R1-5: User name has to be non-empty, alphanumeric-only,
    # and space allowed only if it is not as the prefix or suffix.
    # empty name
    assert register('', 'r151test0@test.com', '12345aA%') is False
    # invalid name with special chars
    assert register('*&&*^', 'r152test0@test.com', '12345aA%') is False
    # prefix space invalid
    assert register(' 123asd', 'r153test0@test.com', '12345aA%') is False
    # surfix space invalid
    assert register('123asd ', 'r154test0@test.com', '12345aA%') is False
    # interspersed space allowed
    assert register('123 qwe', 'r155test0@test.com', '12345aA%') is True


def test_r1_6_user_register():
    # R1-6: User name has to be longer than 2 characters
    # and less than 20 characters.
    # less than 3 chars
    assert register('1', 'test0r161@test.com', '12345aA%') is False
    assert register('12', 'test0r162@test.com', '12345aA%') is False
    # longer than 20 chars
    assert register('1212314123123124asdadwfvafgasd',
                    'test0@testr163.com', '12345aA%') is False
    # valid
    assert register('123124asd', 'test0r164@test.com', '12345aA$') is True


def test_r1_8_user_register():
    # R1-8: Shipping address is empty at the time of registration
    register('r18', 'r18test@test.com', '123456Aa*')
    user = login('r18test@test.com', '123456Aa*')
    assert user.address is None


def test_r1_9_user_register():
    # R1-9: Postal code is empty at the time of registration.
    register('r19', 'r19test@test.com', '123456Aa*')
    user = login('r19test@test.com', '123456Aa*')
    assert user.postcode is None


def test_r1_10_user_register():
    # R1-10: Balance should be initialized as 100 at the time of registration.
    # (free $100 dollar signup bonus).
    k = float(100)
    register('r110', 'r110test@test.com', '123456Aa*')
    user = login('r110test@test.com', '123456Aa*')
    assert (user.balance == k) is True


# login case


def test_r2_1_login():
    """
    Testing R2-1: A user can log in using her/his email address
      and the password.
    (will be tested after the previous test, so we already have u0,
      u1 in database)
    """
    register('r21', 'testr21@test.com', '123456Aa*')
    # correctly logged in
    user = login('testr21@test.com', '123456Aa*')
    assert user is not None

    # incorrect password
    user = login('testr21@test.com', '1234567')
    assert user is None


def test_r2_2_login():
    # R2-2: The login function should check if the supplied inputs meet
    # the same email/password requirements as above,
    # before checking the database.
    register('123h', 'r221test@test.com', '123456Aa!')
    register('123c', 'r222test@test.com', 'Aa111111@')

    # check email format
    # invalid email
    assert login('r221test@@test.com', "123456Aa!") is None

    assert login('', "123456Aa!") is None
    # invalid but not match
    assert login('r221testnotmatch@test.com', "123456Aa!") is None
    # logged in with correct email and password
    assert login('r221test@test.com', "123456Aa!") is not None

    # check password format
    # null password
    assert login('r222test@test.com', "") is None
    # all capital password
    assert login('r222test@test.com', "AAAAAAAA") is None
    # no special char
    assert login('r222test@test.com', "A1a") is None
    # lower only
    assert login('r222test@test.com', "aaaaaaaaaaaa") is None
    # incorrect password
    assert login('r222test@test.com', "Aa111111!") is None
    # successfully logged in
    assert login('r222test@test.com', "Aa111111@") is not None


def test_r3_updateprofile():
    register('Jhon', '123321r31@qq.com', 'Qwert@')

    # A user is only able to update his/her user name,
    # shipping_address, and postal_code
    assert update_user_profile('123321r31@qq.com',
                               'Jake', 'Ontario55St', 'K7L 5E3') is True
    # Shipping_address should be non-empty,
    # alphanumeric-only, and no special characters such as !
    assert update_user_profile('123321r31@qq.com',
                               'Jake', '', 'K7L 5E3') is False
    assert update_user_profile('123321r31@qq.com',
                               'Jake', 'Ontario55St!!', 'K7L 5E3') is False
    # Postal code has to be a valid Canadian postal code
    assert update_user_profile('123321r31@qq.com',
                               'Jake', 'Ontario55St', 'K7L 2Y1') is True
    assert update_user_profile('123321r31@qq.com',
                               'Jake', 'Ontario55St', '0k0 0k0') is False
    # User name follows the requirements above.
    # user name less than 2 chars
    assert update_user_profile('123321r31@qq.com',
                               'J', 'Ontario55St', 'K7L 5E3') is False
    # user name longer than 20 chars
    twentyoneboy = \
        ''.join((random.choice(string.ascii_lowercase) for x in range(21)))
    assert update_user_profile('123321r31@qq.com',
                               twentyoneboy, 'Ontario55St', 'K7L 5E3') is False


def test_r4_1_createproduct():
    testdescription = 'this is a test string and is more than 20 characters!!!'
    testprice = 88.8
    testdate = '2022-01-02'

    # the title should be alphanumeric-only and
    # space allowed only if it is not as prefix and suffix.

    # number only
    assert create_product('1411', testdescription, testprice, testdate,
                          'test_r4_1_createproduct1@test.com') is False
    # character only
    assert create_product('rinva', testdescription, testprice, testdate,
                          'test_r4_1_createproduct2@test.com') is False
    # regular
    assert create_product('r413', testdescription, testprice, testdate,
                          'test_r4_1_createproduct3@test.com') is True
    # space interspersed
    assert create_product('r4 14', testdescription, testprice, testdate,
                          'test_r4_1_createproduct4@test.com') is True
    # space at front
    assert create_product(' r415', testdescription, testprice, testdate,
                          'test_r4_1_createproduct5@test.com') is False
    # space at end
    assert create_product('r416 ', testdescription, testprice, testdate,
                          'test_r4_1_createproduct6@test.com') is False


def test_r4_2_createprodcut():
    # generate a string more than 80 chars for invalid title
    testtitle = \
        ''.join((random.choice(string.ascii_lowercase) for x in range(81)))
    testdescription = 'this is a test string and is more than 80 characters!!!'
    testprice = 88.8
    testdate = '2022-01-02'

    # The title of the product is no longer than 80 characters.
    assert create_product('r422', testdescription, testprice, testdate,
                          'test_r4_2_createprodcut1@test.com') is True
    # insert long title
    assert create_product(testtitle, testdescription, testprice, testdate,
                          'test_r4_2_createprodcut2@test.com') is False


def test_r4_3_createproduct():
    testprice = 88.8
    testdate = '2022-01-02'
    testdescription = 'abcdabcdabcdabcdacbadeabcedabdebeabdabbdaebdbabeadbb'
    string1 = ''.join(random.choice(string.ascii_letters) for i in range(2001))
    # The description of the product can be arbitrary characters,
    # with a minimum length of 20 characters and a maximum
    # of 2000 characters.
    assert create_product('abcdr43', testdescription, testprice, testdate,
                          'test_r4_3_createproduct1@test.com') is True
    # description less than 20 chars
    assert create_product('abcdr432', 'desr43', testprice, testdate,
                          'test_r4_3_createproduct2@test.com') is False
    # description longer than 2000 chars
    assert create_product('abcdr433', string1, testprice, testdate,
                          'test_r4_3_createproduct3@test.com') is False


def test_r4_4_createproduct():
    # normal title
    testtitle = 'abcdr441'
    # long title
    eightyboy = \
        ''.join((random.choice(string.ascii_lowercase) for x in range(80)))
    # 30 chars description
    thirtyboy = \
        ''.join((random.choice(string.ascii_lowercase) for x in range(30)))
    testprice = 88.8
    testdate = '2022-01-02'

    # Description has to be longer than the product's title.
    # normal title and description
    assert create_product(testtitle, thirtyboy, testprice, testdate,
                          'test_r4_4_createproduct1@test.com') is True
    # title longer than description
    assert create_product(eightyboy, thirtyboy, testprice, testdate,
                          'test_r4_4_createproduct2@test.com') is False


def test_r4_5_create_product():
    # R4-5: Price has to be of range [10, 10000].
    # create_product(title, description, price, date, owner_email)
    assert create_product('testr45createproduct1',
                          'test_r4_5_create_product1_description',
                          20,
                          '2021-10-09',
                          'test_r4_5_create_product1@test.com') is True
    # invalid price 9 < 10
    assert create_product('testr45createproduct1',
                          'test_r4_5_create_product1_description',
                          9,
                          '2021-10-09',
                          'test_r4_5_create_product1@test.com') is False
    # invalid price 10001 > 10000
    assert create_product('testr45createproduct1',
                          'test_r4_5_create_product1_description',
                          10001,
                          '2021-10-09',
                          'test_r4_5_create_product1@test.com') is False


def test_r4_6_create_product():
    # R4-6: last_modified_date must be after 2021-01-02 and before 2025-01-02
    # create_product(title, description, price, date, owner_email)
    assert create_product('testr46createproduct1',
                          'test_r4_6_create_product1_description',
                          20,
                          '2021-10-09',
                          'test_r4_6_create_product1@test.com') is True
    # invalid date 2020 before 2021
    assert create_product('testr46createproduct2',
                          'test_r4_6_create_product2_description',
                          20,
                          '2010-10-09',
                          'test_r4_6_create_product2@test.com') is False
    # invalid date 2077 after 2025
    assert create_product('testr46createproduct3',
                          'test_r4_6_create_product3_description',
                          20,
                          '2077-10-09',
                          'test_r4_6_create_product3@test.com') is False


def test_r4_7_create_product():
    # R4-7: owner_email cannot be empty.
    # The owner of the corresponding product must exist in the database
    # create_product(title, description, price, date, owner_email)
    assert create_product('testr47createproduct1',
                          'test_r4_7_create_product1_description',
                          20,
                          '2021-10-09',
                          'test_r4_7_create_product1@test.com') is True
    # empty owner email
    assert create_product('testr47createproduct2',
                          'test_r4_7_create_product2_description',
                          20,
                          '2021-10-09',
                          None) is False


def test_r4_8_create_product():
    # R4-8: A user cannot create products that have the same title.
    # create_product(title, description, price, date, owner_email)
    assert create_product('testr48createproduct1',
                          'test_r4_8_create_product1_description',
                          20,
                          '2021-10-09',
                          'test_r4_8_create_product1@test.com') is True
    # redundant title as above
    assert create_product('testr48createproduct1',
                          'test_r4_8_create_product1redundant_description',
                          20,
                          '2021-10-09',
                          'test_r4_8_create_product1redundant\
                          @test.com') is False


# update case

"""
def test_r5_1_4_update_product():
    # R5-1: One can update all attributes of the product,
    # except owner_email and last_modified_date
    # R5-4: When updating an attribute,
    # one has to make sure that it follows the same requirements as above
    # update_product(title, description, price, owner_email)

    # generate a string more than 80 chars for invalid title
    smallboy = \
        ''.join((random.choice(string.ascii_lowercase) for x in range(81)))
    # generate a string more than 80 chars (than title) for valid description
    smallboydes = \
        ''.join((random.choice(string.ascii_lowercase) for x in range(100)))
    # generate a string more than 200 chars for invalid description
    longboy = \
        ''.join((random.choice(string.ascii_lowercase) for x in range(2001)))

    # create a product for update
    # date is set to 2021-10-07 for date update testing
    create_product('testr51updateproduct1',
                   'testr51_update_product1_description',
                   20,
                   '2021-10-07',
                   'test_r5_1_update_product1@test.com')
    # update title, description, price
    assert update_product('testr51updateproduct1update1',
                          'test_r5_1_update_product1_description_update1',
                          36,
                          'test_r5_1_update_product1@test.com') is True
    # invalid title with special characters
    assert update_product('testr51updateproduct1update2!@#$%^&',
                          'test_r5_1_update_product1_description_update1',
                          36,
                          'test_r5_1_update_product1@test.com') is False
    # invalid title more than 80 char
    assert update_product(smallboy,
                          smallboydes,
                          36,
                          'test_r5_1_update_product1@test.com') is False
    # invalid description less than 20 char
    assert update_product('updater51',
                          'update_r512',
                          36,
                          'test_r5_1_update_product1@test.com') is False
    # invalid description more than 2000 char
    assert update_product('testr51updateproduct1update3',
                          longboy,
                          36,
                          'test_r5_1_update_product1@test.com') is False
    # invalid description less than title
    assert update_product('testr51updateproduct1update4',
                          'update',
                          36,
                          'test_r5_1_update_product1@test.com') is False


def test_r5_2_update_product():
    # R5-2: Price can be only increased but cannot be decreased
    # update_product(title, description, price, owner_email)

    # create a product for update
    # date is set to 2021-10-07 for date update testing

    create_product('testr52updateproduct1',
                   'test_r5_2_update_product1_description',
                   20,
                   '2021-10-07',
                   'test_r5_2_update_product1@test.com')
    # update with valid price more than before
    assert update_product('testr52updateproduct1update1',
                          'test_r5_2_update_product1_description_update1',
                          36,
                          'test_r5_2_update_product1@test.com') is True
    # update with invalid price less than before
    assert update_product('testr52updateproduct1update1',
                          'test_r5_2_update_product1_description_update1',
                          16,
                          'test_r5_2_update_product1@test.com') is False

"""