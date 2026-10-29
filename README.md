# Seecr Testtools

Small helpers for writing pytest tests, used across [Seecr](https://seecr.nl) projects.

[![Tests](https://github.com/seecr/seecr-testtools/actions/workflows/test.yml/badge.svg)](https://github.com/seecr/seecr-testtools/actions/workflows/test.yml)
[![PyPI](https://img.shields.io/pypi/v/seecr-testtools.svg)](https://pypi.org/project/seecr-testtools/)

## Installation

```sh
pip install seecr-testtools
```

Requires Python 3.11 or newer. Installs `pytest` and `pytest-asyncio`.

## What's inside

### `anything`: wildcards in assertions

`anything` equals every value, so you can compare whole structures while
ignoring the parts you don't care about. Pass a function to check a value
instead of ignoring it.

```python
from seecr_testtools import anything

assert response == {
    "id": anything,                           # any value
    "name": "Alice",
    "age": anything(lambda age: age >= 18),   # must satisfy the check
}
```

### `Mock`: record calls and fake return values

```python
from seecr_testtools.mock import Mock

store = Mock.blank(get={"a": 1}.get, save=None)
store.get("a")              # 1: a callable value is called
store.save(1, force=True)   # None: other values are returned as is
store.whatever()            # unknown methods return None
store.calls("save")         # [save(1, force=True)]
store.calls("save")[0].kwargs  # {'force': True}
```

`Mock.imitate(obj)` wraps a real object. Methods you override with
`mock_method` are replaced on the object itself, so the object's own code
calls the fake too. Coroutine methods automatically get an async fake.

```python
class Repository:
    def load(self):
        return "from database"

    def report(self):
        return self.load().upper()

repo = Repository()
mock = Mock.imitate(repo)
mock.mock_method("load", "fake")

assert mock.report() == "FAKE"   # report() runs for real, load() is faked
assert len(mock.calls("load")) == 1
```

For a blank mock, use `mock_method(name, value, is_async=True)` to get an
async method.

### `login_user`

Logs a user in on a test client for Seecr web applications and keeps the
session cookie: `login_user(env, username, password)`. It expects `env` to
provide `client` and `actions`.

## Development

```sh
python -m venv env --prompt seecr-testtools
source env/bin/activate
pip install -e .
pytest
```

Tests live next to the code as `<module>_test.py`. Async tests need no
decorator: pytest-asyncio runs in auto mode.

## License

Copyright (C) 2024-2026 Seecr (Seek You Too B.V.)

Licensed under the [MIT License](LICENSE).
