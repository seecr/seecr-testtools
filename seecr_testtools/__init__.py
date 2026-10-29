## begin license ##
#
# Seecr Testtools provides tools for creating pytests
#
# Copyright (C) 2024-2026 Seecr (Seek You Too B.V.) https://seecr.nl
#
# This file is part of "Seecr Testtools"
#
# "Seecr Testtools" is released under the MIT License.
# See the LICENSE file for the full license text.
#
# SPDX-License-Identifier: MIT
#
## end license ##

__all__ = ["anything", "VERSION", "login_user"]
from ._any import anything
from .wui import login_user
from ._version import __version__

VERSION = __version__.split("+")[0]
