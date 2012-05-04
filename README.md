# Licensing #
The code in this module is Copyright (C) 2012 Hot Studio and covered by the [MIT license](http://www.opensource.org/licenses/MIT).
unittestzero, required by this module, is covered by the [MPL license](http://mozilla.org/MPL/2.0/).

# Overview #

This project's intention is to extend the unittestzero package to include methods to verify complex data types. The unittestzero project can be found [on github](https://github.com/AutomatedTester/unittest-zero) and it's documentation can be found [here](http://oss.theautomatedtester.co.uk/unittest-zero/epydoc/index.html).

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

## How to update the installed package from source

(sudo) pip uninstall unittestone
(sudo) python setup.py develop
