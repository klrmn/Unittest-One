#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestone import Assert


class TestNewAsserts:

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

    def test_that_items_are_not_equal(self):
        Assert.not_equal("a", "b")
        Assert.not_equal(1, 2)

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