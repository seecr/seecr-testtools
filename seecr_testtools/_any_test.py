## begin license ##
#
# Seecr Testtools provides tools for creating pytests
#
# Copyright (C) 2024, 2026 Seecr (Seek You Too B.V.) https://seecr.nl
#
# This file is part of "Seecr Testtools"
#
# "Seecr Testtools" is released under the MIT License.
# See the LICENSE file for the full license text.
#
# SPDX-License-Identifier: MIT
#
## end license ##

from ._any import anything
from random import randint


def test_anything():
    assert anything == anything
    assert anything == "something"
    assert anything(lambda x: "thing" in x) == "something"
    assert anything(lambda x: "thing" in x) != "unequal"


def test_anything_repr():
    def verify(x):
        return "thing" in x

    assert repr(anything) == "*"
    assert repr(anything(verify)) == "verify(...)"


def test_anything_usecase():
    data = {
        "anumber": randint(0, 100),
        "astring": "hello",
        "alist": [1, 2, 3],
        "adict": {"a": 1, "b": 2, "c": randint(0, 100)},
    }

    assert data == {
        "anumber": anything,
        "astring": "hello",
        "alist": [1, 2, 3],
        "adict": {"a": 1, "b": 2, "c": anything(lambda x: x < 100)},
    }
