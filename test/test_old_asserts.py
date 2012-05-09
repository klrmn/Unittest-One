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
from unittestzero import Assert
import re
from testmania.expect import Expectation

class TestOldAsserts:

    # some tests missing in unittestzero
    def test_that_lists_are_equal(self):
        Assert.equal(["1","3","7","11"], ["1","3","7","11"])

    def test_that_lists_are_equal_failure(self):
        try:
            Assert.equal(["1","3","7","11"], ["1","11","3","7"])
        except AssertionError, e:
            pass

    def test_that_dicts_are_equal(self):
        Assert.equal({ 'key1': 'value1', 'key2': 'value2'}, { 'key1': 'value1', 'key2': 'value2'})

    def test_that_dicts_are_equal_failure(self):
        try:
            Assert.equal({ 'key1': 'value1', 'key2': 'value2'}, { 'key1': 'value3', 'key2': 'value4'})
        except AssertionError, e:
            pass
        try:
            Assert.equal({ 'key1': 'value1', 'key2': 'value2'}, { 'key1': 'value1', 'key3': 'value4'})
        except AssertionError, e:
            pass

    # tests for contains
    def test_that_dict_contain_key(self):
        Assert.contains("key", { 'key': 'value'})

    def test_that_contains_only_looks_at_keys(self):
        try:
            Assert.contains("value", { 'key': 'value'})
        except AssertionError as e:
            pass

    def test_that_dict_does_not_contain_key(self):
        try:
            Assert.contains("key1", { 'key': 'value'})
        except AssertionError as e:
            pass

    def test_list_contains_dict(self):
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
        Assert.contains(dict1, list_of_dicts)
        Assert.contains(dict2, list_of_dicts)

    def test_list_contains_dict_failures(self):
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
        try:
            Assert.contains( dict3, list_of_dicts)
        except AssertionError:
            pass
        # if it were only looking at keys, this would fail
        list_of_dicts = [ dict1, dict3 ]
        try:
            Assert.contains( dict2, list_of_dicts)
        except AssertionError:
            pass

    # Expectation objects have some shortcomings
    def test_expectations_in_dict_values(self):
        actual = {
            'an_integer': 32,
            'a_string': 'stupendous',
            'a_float': 14.34,
            'a_list': 'dog',
        }
        expected = {
            'an_integer': Expectation(Assert.greater, 30,),
            'a_string': Expectation(Assert.contains, 'stupendously',),
            'a_float': Expectation(Assert.less, 14.342,),
            'a_list': Expectation(Assert.contains, ['cat', 'dog', 'mouse']),
        }
        Assert.equal(actual, expected)

    @pytest.mark.xfail(reason="Expectations don't work in keys because of ordering")
    def test_expectations_in_dict_keys(self):
        actual = {
            'an_integer': 32,
            'a_string': 'stupendous',
            'a_float': 14.34,
            'a_list': 'dog',
        }
        expected = {
            Expectation(Assert.equal, 'an_integer'): 32,
            Expectation(Assert.equal, 'a_string'): 'stupendous',
            Expectation(Assert.equal, 'a_float'): 14.34,
            Expectation(Assert.equal, 'a_list'): 'dog',
        }
        Assert.equal(actual, expected)

    def test_expectations_dict_failure(self):
        actual = {
            'an_integer': 32,
            'a_string': 'stupendous',
            'a_float': 14.34,
            'a_list': 'dog',
        }
        expected = {
            'an_integer': Expectation(Assert.greater, 30,),
            'a_string': Expectation(Assert.contains, 'stupendously', msg="not an adjective"),
            'a_float': Expectation(Assert.less, 14.342,),
            'a_list': Expectation(Assert.contains, ['cat', 'dog', 'mouse']),
        }
        Assert.equal(actual, expected,)

    def test_expectation_list_contains(self):
        actual = [
            'this',
            'that',
            'the other',
            'superfluous'
        ]
        expected = Expectation(Assert.contains, 'superfluously',)
        Assert.contains(expected, actual)
