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

__all__ = ["anything"]


class _Any:
    def __init__(self, f=None):
        self.f = f

    def __call__(self, *args, **kwargs):
        return _Any(*args, **kwargs)

    def __eq__(self, other):
        return self.f is None or self.f(other)

    def __repr__(self):
        return "*" if self.f is None else self.f.__name__ + "(...)"


anything = _Any()
