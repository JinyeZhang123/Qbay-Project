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
