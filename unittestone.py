#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from decimal import Decimal
from unittestzero import Assert as A

class Assert(A):

    @classmethod
    def raises(self, exception, caller, msg=None, *args, **kwargs):
        """
        Asserts that an Error is raised when calling a method

        :Args:
         - Error class
         - method to be called
         - Message that will be printed if it fails
         - args that will be passed to the caller
         - kwargs that will be passed to the caller
        """
        try:
            caller(*args, **kwargs)
        except exception:
            return

        if hasattr(exception, '__name__'):
            excName = exception.__name__
        else:
            excName = str(exception)

        raise AssertionError("%s was not raised\n%s" % (excName, msg))

    @classmethod
    def rounded(self, first, second, msg=''):
        a = Decimal(str(first))
        b = Decimal(str(second))
        variance = Decimal('0.5')

        # is it float? if so, move the digits and change the variance
        if (abs(first - second) < variance):
            print "initial dif is %s" % abs(first - second)
            variance = 5
            # Keep multiplying the numbers by 10 until there are no more decimal places in at least one of them
            while ( (a != int(a)) and (b != int(b)) ):
                a *= 10
                b *= 10
 
        print "numbers used for comparison: %s, %s. variance: %s" % (int(a), int(b), variance)
        # The integer part of these numbers must be less than 5 points apart
        assert abs(int(a) - int(b)) < variance, "neither %s nor %s is a round of the other. %s" % (first, second, msg)

    @classmethod
    def nearly(self, first, second, variance=None, msg=''):
        difference = abs(first - second)
        assert difference <= variance, "%s is not within %s of %s. %s" % (first, variance, second, msg)

    @classmethod
    def deep_equal(self, actual, expected, msg=''):
        pass

