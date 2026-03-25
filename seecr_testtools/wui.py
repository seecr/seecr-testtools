## begin license ##
#
# Seecr Testtools provides tools for creating pytests
#
# Copyright (C) 2026 Seecr (Seek You Too B.V.) http://seecr.nl
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

__all__ = ["login_user"]


def login_user(env, username, password):
    response = env.client.post(
        env.actions.register("login"), data={"username": username, "password": password}
    )
    assert response.status_code == 200 and response.json()["success"]
    env.client.cookies.clear()
    env.client.cookies["session"] = response.cookies["session"]
