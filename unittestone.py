#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from decimal import Decimal
from unittestzero import Assert as A

class Assert(A):

    @classmethod
    def contains(self, needle, haystack, msg=''):
        try:
            assert needle in haystack
        except AssertionError:
            raise AssertionError('%s is not found in %s. %s' % (needle, haystack, msg))

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
