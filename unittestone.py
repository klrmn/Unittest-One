#!/usr/bin/env python

# Copyright (C) 2012 Leah Klearman

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


import re
from decimal import Decimal

from unittestzero import Assert as A
from testmania import assert_deep_equal, Expectation as E

class Assert(A):

    @classmethod
    def contains(self, needle, haystack, msg=''):
        try:
            assert needle in haystack
        except AssertionError:
            raise AssertionError('%s is not found in %s. %s' % (needle, haystack, msg))

    @classmethod
    def does_not_contain(self, needle, haystack, msg=''):
        try:
            assert needle not in haystack
        except AssertionError:
            raise AssertionError('%s should not be found in %s. %s' % (needle, haystack, msg))

    @classmethod
    def rounded(self, first, second, msg=''):
        '''Class method. Asserts unless one number is a rounded version of the other.
        :Args:
        - first - a number (for example pi to 5 places)
        - second - another number (for example pi to 6 places)
        - msg - (optional) message to print with assert
        '''
        a = Decimal(str(first))
        b = Decimal(str(second))
        variance = Decimal('0.5')

        # is it float? if so, move the digits and change the variance
        if (abs(first - second) < variance):
            variance = 5
            # Keep multiplying the numbers by 10 until there are no more decimal places in at least one of them
            while ( (a != int(a)) and (b != int(b)) ):
                a *= 10
                b *= 10
 
        # The integer part of these numbers must be less than 5 points apart
        assert abs(int(a) - int(b)) < variance, "neither %s nor %s is a round of the other. %s" % (first, second, msg)

    @classmethod
    def nearly(self, first, second, variance=None, msg=''):
        '''Class method. Asserts if the absolute value of the first parameter minus the second parameter
        is larger than the variance.
        :Args:
        - first - a number
        - second - another number
        - variance - the permitted difference between the two values
        - msg - (optional) message to print with assert
        '''
        difference = abs(first - second)
        assert difference <= variance, "%s is not within %s of %s. %s" % (first, variance, second, msg)

    @classmethod
    def between(self, actual, lower, upper, msg=''):
        '''Class method. Asserts if actual is not between (not inclusive of) lower and upper values.
        :Args:
        - actual - value being checked
        - lower - lower bound
        - upper - upper bound
        - msg - (optional) message to print with assert
        '''
        assert lower < actual < upper, "%s is not between %s and %s. %s" % (actual, lower, upper, msg)

    # matches actually uses re.search, rather than re.match, because you can specify begining of string
    @classmethod
    def matches(self, string, regex, msg=''):
        '''Class method. Asserts if string does not match regex.
        :Args:
        - string - the string to evaluate
        - regex - regular expression as string or SRE_Pattern
        - msg - (optional) message to print with assert
        '''
        if (type(regex).__name__ != "SRE_Pattern"):
            regex = re.compile(regex)
        found = regex.search(string)
        try:
            self.not_none(found)
        except AssertionError:
            raise AssertionError("'%s' did not match '%s'. %s" % 
                (string, regex.pattern, msg))

    @classmethod
    def deep_equal(self, actual, expected, ignore_extra_keys=False, msg=''):
        '''Class method. Asserts if any of the assertations defiend as the dictionaries values fail.
        :Args:
        - actual - dictionary to evaluate
        - expected - dictionary with the same keys as actual, but with Asserts in the values
        - ignore_extra_keys - (default False) do not raise error if the actual has more keys than the expected

        For more documentation, see http://nailxx.github.com/testmania/
        '''
        assert_deep_equal(actual, expected, ignore_extra_keys=ignore_extra_keys, msg=msg)

    @classmethod
    def iterate(self, assertion, the_list, template, **kwargs):
        '''Class method. Performs assertion on each member of the_list against the template.
        :Args:
        - assertion - what Assert method (as string) to use (defaults to Assert.equal if empty string)
        - the_list - list of actual values
        - template - the thing to compare the list items with (typically the 'second' parameter
            in Assert methods)
        - kwargs - any other keyword args that the assertion may take, including msg.
        '''
        if assertion == '':
            assertion = Assert.equal
        for item in the_list:
            assertion(item, template, kwargs)

class Expectation(E):
    pass