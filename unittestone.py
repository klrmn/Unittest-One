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


from decimal import Decimal
from unittestzero import Assert as A
import re

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
        difference = abs(first - second)
        assert difference <= variance, "%s is not within %s of %s. %s" % (first, variance, second, msg)

    # matches actually uses re.search, rather than re.match, because you can specify begining of string
    @classmethod
    def matches(self, string, regex, msg=''):
        if (type(regex).__name__ != "SRE_Pattern"):
            regex = re.compile(regex)
        found = regex.search(string)
        try:
            self.not_none(found)
        except AssertionError:
            raise AssertionError("'%s' did not match '%s'. %s" % 
                (string, regex.pattern, msg))
