# Licensing #
The code in this module is Copyright (C) 2012 Leah Klearman and covered by the [MIT license](http://www.opensource.org/licenses/MIT).
unittestzero, required by this module, is covered by the [MPL license](http://mozilla.org/MPL/2.0/).
testmania, required by this module, is covered by the [MIT license](http://www.opensource.org/licenses/MIT).

# Overview #
This project's intention is to extend the unittestzero package to include methods to verify complex data types found in APIs. The unittestzero project can be found [on github](https://github.com/AutomatedTester/unittest-zero) and it's documentation can be found [here](http://oss.theautomatedtester.co.uk/unittest-zero/epydoc/index.html). The testmania project can be found [on github](https://github.com/nailxx/testmania) and its documentation can be found [here](http://nailxx.github.com/testmania/).

## Installation ##

This package is not yet available on pypy. Please build it from source.

(sudo) python setup.py install

## Example ##

    from unittestone import Assert


    class TestSomethingCool:

        def test_equals(self):
            Assert.equal(1, 1)

## How to run the tests against this frame work ##

    py.test -p no:mozwebqa .
or
    python runtests.py

## How to update the installed package from source

(sudo) pip uninstall unittestone
(sudo) python setup.py install

## Continuous Integration ##

[![Build
Status](https://secure.travis-ci.org/klrmn/Unittest-One.png?branch=master)](http://travis-ci.org/klrmn/Unittest-One)
