# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

`seecr-testtools` is a small Python (>=3.11) library of pytest helpers shared across Seecr projects: `anything` (a wildcard that compares equal to any value, or to values passing a check function), `Mock` (records calls and fakes return values, sync and async), and `login_user` (logs in on a Seecr web-app test client). Runtime dependencies are `pytest` and `pytest-asyncio`; `setuptools_scm` is only a build dependency.

## Commands

A virtualenv lives in `env/`.

```sh
env/bin/python -m pytest                                              # all tests
env/bin/python -m pytest seecr_testtools/mock_test.py                 # one file
env/bin/python -m pytest seecr_testtools/mock_test.py::test_mock      # one test
```

Pytest is configured in `pyproject.toml` under `[tool.pytest]`: pytest-asyncio runs in auto mode, so `async def test_...` needs no marker.

## Conventions

- Tests sit next to the module they test as `<module>_test.py`, written as plain pytest functions.
- Every source file starts with the MIT `## begin license ## ... ## end license ##` header (template data in `doc/license.conf`). Copy it into new files and keep the copyright year(s) current.
- Versions come from git tags via `setuptools_scm` (tags like `0.4.1`); `seecr_testtools/_version.py` is generated and git-ignored — don't edit it. The package root imports it, so the package must be installed (`pip install -e .`) before tests run.
- Pushing a version tag to GitHub publishes that version to PyPI (`.github/workflows/publish.yml`), and PyPI never accepts a version twice. Don't push tags unless asked.
- `anything` and `login_user` are exported from the package root; `Mock` is imported from `seecr_testtools.mock`.
- `Mock.immitate` is the original misspelling of `Mock.imitate` and is kept as an alias for existing users; use `imitate` in new code.
- `Mock.imitate(obj)` replaces overridden methods on the real object with `setattr`, so the object's own calls go through the fake. Methods only reached through the real object, not through the mock, are not recorded, and `calls(name)` raises `KeyError` for a method the mock never saw.
