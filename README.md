# Overview #

This project's intention is to extend the unittestzero package to include methods to verify complex data types. The unittestzero project can be found [on github](https://github.com/AutomatedTester/unittest-zero) and it's documentation can be found [here](http://automatedtester.github.com/unittest-zero/).

## Example ##

    from unittestone import Assert


    class TestSomethingCool:

        def test_equals(self):
            Assert.equal(1, 1)

## How to run the tests against this frame work ##

py.test -p no:mozwebqa .