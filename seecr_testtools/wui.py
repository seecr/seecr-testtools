## begin license ##
#
# Seecr Testtools provides tools for creating pytests
#
# Copyright (C) 2026 Seecr (Seek You Too B.V.) https://seecr.nl
#
# This file is part of "Seecr Testtools"
#
# "Seecr Testtools" is released under the MIT License.
# See the LICENSE file for the full license text.
#
# SPDX-License-Identifier: MIT
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
