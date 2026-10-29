## begin license ##
#
# Seecr Testtools provides tools for creating pytests
#
# Copyright (C) 2026 Seecr (Seek You Too B.V.) https://seecr.nl
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

from inspect import ismethod, iscoroutinefunction


class Mock:

    @classmethod
    def immitate(cls, obj):
        return cls(obj=obj)

    @classmethod
    def blank(cls, **kwargs):
        mock = cls(obj=None)
        for name, value in kwargs.items():
            mock.mock_method(name, value)
        return mock

    def __init__(self, obj=None):
        self._obj = obj
        self._methods = {}

    def mock_method(self, name, value, is_async=False):
        if self._obj is not None:
            if (method := getattr(self._obj, name, None)) is None:
                raise RuntimeError(f"Method not found for immitating: {name}")
            is_async = iscoroutinefunction(method)

        method = MockAsyncMethod(name, value) if is_async else MockMethod(name, value)
        self._methods[name] = method

        if self._obj is not None:
            setattr(self._obj, name, method)

        return method

    def calls(self, name):
        return self._methods[name].calls

    def __getattr__(self, name):
        if self._obj is not None:
            if name in self._methods:
                return self._methods.get(name)

            if (method := getattr(self._obj, name)) is not None:
                return self.mock_method(name, method)

        if name not in self._methods:
            return self.mock_method(name, None)

        return self._methods.get(name)


class MockMethod:
    def __init__(self, name, value):
        self._name = name
        self._value = value
        self._calls = []

    def __call__(self, *args, **kwargs):
        self._calls.append(MockCall(self, *args, **kwargs))
        if callable(self._value):
            return self._value(*args, **kwargs)
        return self._value

    @property
    def calls(self):
        return self._calls


class MockAsyncMethod(MockMethod):

    async def __call__(self, *args, **kwargs):
        self._calls.append(MockCall(self, *args, **kwargs))
        if callable(self._value):
            return await self._value(*args, **kwargs)
        return self._value


class MockCall:
    def __init__(self, method, *args, **kwargs):
        self.method = method
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        args = []
        if len(self.args) > 0:
            args.append(", ".join(str(arg) for arg in self.args))
        if len(self.kwargs) > 0:
            args.append(", ".join(f"{k}={repr(v)}" for k, v in self.kwargs.items()))
        return self.method._name + "(" + ", ".join(args) + ")"
