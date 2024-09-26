## begin license ##
#
# Seecr Testtools provides tools for creating pytests
#
# Copyright (C) 2024 Seecr (Seek You Too B.V.) http://seecr.nl
#
# This file is part of "Seecr Testtools"
#
# "Seecr Testtools" is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# "Seecr Testtools" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "Seecr Testtools".  If not, see <http://www.gnu.org/licenses/>.
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
