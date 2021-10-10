import random
import string

import re

from qbay.models import register, login, create_product, update_user_profile, update_product


def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''

    assert register('r17u0', 'r171test0@test.com', '123456Aa*') is True
    assert register('r17u0', 'r172test1@test.com', '123456Aa*') is True
    assert register('r17u1', 'r172test1@test.com', '123456Aa*') is False


def test_r1_1_user_register():
    # R1-1: Both the email and password cannot be empty.
    assert register('u0r11','','') is False


def test_r1_3_user_register():
    # 1-3: The email has to follow addr-spec defined in RFC 5322
    # (see https://en.wikipedia.org/wiki/Email_address for a human-friendly
    assert register('r13u0', 'asdwaff@@', '123456aA*') is False
    assert register('r13u0', 'caijixiaomc@gmail.com', '123456aA*') is True


def test_r1_4_user_register():
    # R1-4: Password has to meet the required complexity: minimum length 6,
    # at least one upper case, at least one lower case, and at least 1 special char
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
    # R1-6: User name has to be longer than 2 characters and less than 20 characters.
    # less than 3 chars
    assert register('1', 'test0r161@test.com', '12345aA%') is False
    assert register('12', 'test0r162@test.com', '12345aA%') is False
    # longer than 20 chars
    assert register('1212314123123124asdadwfvafgasd', 'test0@testr163.com', '12345aA%') is False
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
    # R1-10: Balance should be initialized as 100 at the time of registration. (free $100 dollar signup bonus).
    k = float(100)
    register('r110', 'r110test@test.com', '123456Aa*')
    user = login('r110test@test.com', '123456Aa*')
    assert (user.balance == k) is True



#-----------
# login case

def test_r2_1_login():
    '''
    Testing R2-1: A user can log in using her/his email address
      and the password.
    (will be tested after the previous test, so we already have u0,
      u1 in database)
    '''
    register('r21', 'testr21@test.com', '123456Aa*')
    # correctly logged in
    user = login('testr21@test.com', '123456Aa*')
    assert user is not None

    # incorrect password
    user = login('testr21@test.com', '1234567')
    assert user is None


def test_r2_2_login():
    # R2-2: The login function should check if the supplied inputs meet
    # the same email/password requirements as above, before checking the database.
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

    # A user is only able to update his/her user name, shipping_address, and postal_code
    assert update_user_profile('123321r31@qq.com', 'Jake', 'Ontario55St', 'K7L 5E3') is True
    # Shipping_address should be non-empty, alphanumeric-only, and no special characters such as !
    assert update_user_profile('123321r31@qq.com', 'Jake', '', 'K7L 5E3') is False
    assert update_user_profile('123321r31@qq.com', 'Jake', 'Ontario55St!!', 'K7L 5E3') is False
    # Postal code has to be a valid Canadian postal code
    assert update_user_profile('123321r31@qq.com', 'Jake', 'Ontario55St', 'K7L 2Y1') is True
    assert update_user_profile('123321r31@qq.com', 'Jake', 'Ontario55St', '0k0 0k0') is False
    # User name follows the requirements above.
    # user name less than 2 chars
    assert update_user_profile('123321r31@qq.com', 'J', 'Ontario55St', 'K7L 5E3') is False
    # user name longer than 20 chars
    twentyoneboy = ''.join((random.choice(string.ascii_lowercase) for x in range(21)))
    assert update_user_profile('123321r31@qq.com', twentyoneboy, 'Ontario55St', 'K7L 5E3') is False



