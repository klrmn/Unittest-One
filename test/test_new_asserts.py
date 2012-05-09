#!/usr/bin/env python

# Copyright (C) 2012 Hot Studio

# Project Lead: Leah Klearman
# Contributing authors: Leah Klearman (lklrmn@gmail.com)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import pytest
from unittestone import Assert
import re
from testmania.expect import Expectation

class TestNewAsserts:

    # tests for contains
    def test_contains_failure_with_message(self):
        try:
            Assert.contains("a", "bcd", msg="failure message")
        except AssertionError as e:
            Assert.equal(e.msg, "a is not found in bcd. failure message")

    def test_contains_failure_without_message(self):
        try:
            Assert.contains("a", "bcd")
        except AssertionError as e:
            Assert.equal(e.msg, "a is not found in bcd. ")

    # tests for does_not_contain
    def test_string_does_not_contain_letter(self):
        Assert.does_not_contain('a', 'bcd')

    def test_list_of_strings_does_not_contain_string(self):
        Assert.does_not_contain('turtle', ['dog', 'cat', 'guiny pig'])

    def test_list_of_dicts_does_not_contain_dict(self):
        dict1 = {
                'a': 'avalue',
                'b': 'bvalue',
                'c': 'cvalue',
            }
        dict2 = {
                'a': 'dvalue',
                'b': 'evalue',
                'c': 'fvalue',
            }
        dict3 = {
                'd': 'dvalue',
                'e': 'evalue',
                'f': 'fvalue',
            }
        list_of_dicts = [ dict1, dict2 ]
        Assert.does_not_contain(dict3, list_of_dicts)

    def test_dict_does_not_contain_key(self):
        Assert.does_not_contain('a', { 'b': 'bvalue', 'c': 'cvalue', 'd': 'dvalue' })

    def test_list_of_dicts_does_not_contain_dict_failure_no_message(self):
        dict1 = {
                'a': 'avalue',
                'b': 'bvalue',
                'c': 'cvalue',
            }
        dict2 = {
                'a': 'dvalue',
                'b': 'evalue',
                'c': 'fvalue',
            }
        dict3 = {
                'd': 'dvalue',
                'e': 'evalue',
                'f': 'fvalue',
            }
        list_of_dicts = [ dict1, dict2, dict3 ]
        try:
            Assert.does_not_contain(dict3, list_of_dicts)
        except AssertionError as e:
            Assert.equal(e.msg, "%s should not be found in %s. " % (dict3, list_of_dicts))

    def test_dict_does_not_contain_key_failure_with_message(self):
        dict3 = {
                'd': 'dvalue',
                'e': 'evalue',
                'f': 'fvalue',
            }
        try:
            Assert.does_not_contain('d', dict3, msg="failure message")
        except AssertionError as e:
            Assert.equal(e.msg, "%s should not be found in %s. failure message" % ('d', dict3))

    # tests for nearly
    def test_nearly_integer(self):
        Assert.nearly(2345, 2346, 1)

    def test_nearly_float(self):
        Assert.nearly(3.14, 3.14379, 0.005)

    def test_nearly_failure_with_message(self):
        try:
            Assert.nearly(3.15, 3.14159265, "pi rounded improperly")
        except AssertionError as e:
            Assert.equal(e.msg, "3.15 is not within 0.005 of 3.14159256. pi rounded improperly")

    def test_nearly_failure_without_message(self):
        try:
            Assert.nearly(34, 42, 3)
        except AssertionError as e:
            Assert.equal(e.msg, "34 is not within 3 of 42. ")

    # tests for rounded
    def test_rounded_up(self):
        Assert.rounded(11, 10.8)
        Assert.rounded(14.53, 14.529)

    def test_rounded_down(self):
        Assert.rounded(14.53, 14.534)
        Assert.rounded(11, 11.3)

    def test_rounded_failure_with_message(self):
        try:
            Assert.rounded(13, 19, msg="failure message")
        except AssertionError as e:
            Assert.equal(e.msg, "neither 13 nor 19 is a round of the other. failure message")

    def test_rounded_failure_no_message(self):
        try:
            Assert.rounded(14.983, 14.985)
        except AssertionError as e:
            Assert.equal(e.msg, "neither 14.983 nor 14.985 is a round of the other. ")

    # tests for matches
    # use by match if you want to have special flags
    def test_matches_by_match(self):
        matcher = re.compile('ab.*', re.IGNORECASE)
        Assert.matches("Absolutely", matcher)

    def test_matches_by_match_failure_with_message(self):

        matcher = re.compile('ab.*')
        try:
            Assert.matches("Absolutely", matcher, msg="failure message")
        except AssertionError as e:
            Assert.equal(e.msg, "'Absolutely' did not match 'ab.*'. failure message")

    # or it will compile the pattern for you
    def test_matches_by_string_begining(self):
        Assert.matches('absolutely', '^ab')

    def test_matches_by_string_end(self):
        Assert.matches('absolutely', 'ly$')

    def test_matches_by_string_failure_no_message(self):
        try:
            Assert.matches('Absolutely', '^sol')
        except AssertionError as e:
            Assert.equal(e.msg, "'Absolutely' did not match '^sol'. ")

    # test Assert.complex with Expectation
    @pytest.mark.xfail(reason="not implemented yet")
    def test_complex_dict_failure_too_many_keys(self):
        actual = {
            'an_integer': 32,
            'a_string': 'stupendous',
            'a_float': 14.34,
            'a_list': 'dog',
            'a_thing': 'thing'
        }
        expected = {
            'an_integer': Expectation(Assert.nearly, 30, 2,),
            'a_string': Expectation(Assert.matches, '.*ous$',),
            'a_float': Expectation(Assert.rounded, 14.342,),
            'a_list': Expectation(Assert.contains, ['cat', 'dog', 'mouse']),
        }
        Assert.equal(actual, expected, msg="not complexly equal")

    @pytest.mark.xfail(reason="not implemented yet")
    def test_complex_dict_failure_missing_key(self):
        actual = {
            'an_integer': 32,
            'a_string': 'stupendous',
            'a_list': 'dog',
        }
        expected = {
            'an_integer': Expectation(Assert.nearly, 30, 2,),
            'a_string': Expectation(Assert.matches, '.*ous$',),
            'a_float': Expectation(Assert.rounded, 14.342,),
            'a_list': Expectation(Assert.contains, ['cat', 'dog', 'mouse']),
        }
        Assert.equal(actual, expected, msg="not complexly equal")

    @pytest.mark.xfail(reason="not implemented yet")
    def test_complex_ignore_extra_keys(self):
        # don't try to do it this way, it doesn't work
        # this is why we need Assert.complexly that does IGNORE_EXTRA_KEYS
        actual = {
            'an_integer': 32,
            'a_string': 'stupendous',
            'a_float': 14.34,
            'a_list': 'dog',
        }
        expected = {
            'a_string': Expectation(Assert.matches, '.*ous$',),
        }
        Assert.contains(expected, actual)

    @pytest.mark.xfail(reason="not implemented yet")
    def test_complex_list_contains_dict(self):
        dict1 = {
            'an_integer': 32,
            'a_string': 'stupendous',
            'a_float': 14.34,
            'a_list': 'dog',
            'a_thing': 'thing'
        }
        dict2 = {
            'key1': 'valuea',
            'key2': 'valueb',
            'key3': 'valuec',
        }
        dict3 = {
            'key1': 1,
            'key2': 2,
            'key3': 3,
        }
        actual = [ dict1, dict2, dict3 ]
        expected = {
            'an_integer': Expectation(Assert.nearly, 30, 2,),
            'a_string': Expectation(Assert.matches, '.*ous$',),
            'a_float': Expectation(Assert.rounded, 14.342,),
            'a_list': Expectation(Assert.contains, ['cat', 'dog', 'mouse']),
        }
        Assert.contains(expected, actual, msg="expectation in value only")
        expected = {
            Expectation(Assert.matches('^\w1$')): Expectation(Assert.less(2)),
            Expectation(Assert.matches('^\w2$')): Expectation(Assert.more(1)),
            Expectation(Assert.matches('^\w3$')): 3,
        }
        Assert.contains(expected, actual, msg="expectation in key and value")