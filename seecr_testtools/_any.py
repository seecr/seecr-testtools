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
