from .mock import Mock


def test_mock():
    m = Mock.blank()
    assert m.do_something(42) is None
    assert len(m.calls("do_something")) == 1
    call = m.calls("do_something")[0]
    assert call.args == (42,)
    assert call.kwargs == {}

    m = Mock.blank()
    m.mock_method("answer", value=42)
    assert m.calls("answer") == []
    assert (
        m.answer(21, question="the meaning of life, the universe and everything") == 42
    )
    assert len(m.calls("answer")) == 1

    call = m.calls("answer")[0]
    assert call.args == (21,)
    assert call.kwargs == {
        "question": "the meaning of life, the universe and everything",
    }
    assert (
        str(call)
        == "answer(21, question='the meaning of life, the universe and everything')"
    )


def test_mock_default():
    m = Mock.blank(answer=42)
    assert m.calls("answer") == []
    assert (
        m.answer(21, question="the meaning of life, the universe and everything") == 42
    )
    assert len(m.calls("answer")) == 1

    call = m.calls("answer")[0]
    assert call.args == (21,)
    assert call.kwargs == {
        "question": "the meaning of life, the universe and everything",
    }
    assert (
        str(call)
        == "answer(21, question='the meaning of life, the universe and everything')"
    )


def test_immitate():
    class A:
        def method_True(self):
            return True

        def method_False(self):
            return True

    a = A()

    m = Mock.immitate(a)
    assert m.method_True() is True
    assert len(m.calls("method_True")) == 1
    assert m.method_True() is True
    assert len(m.calls("method_True")) == 2
    assert m.method_False() is True
    assert len(m.calls("method_False")) == 1


def test_immitate_override():
    class A:
        def method_True(self):
            return True

        def method_False(self):
            return True

    a = A()

    m = Mock.immitate(a)
    m.mock_method("method_True", 42)
    assert m.method_True() == 42
    assert len(m.calls("method_True")) == 1

    try:
        m.mock_method("method_Bool", 42)
    except RuntimeError as e:
        assert str(e) == "Method not found for immitating: method_Bool"


def test_immitate_override_called():
    class A:
        def method_True(self):
            return True

        def method_False(self):
            return self.method_True()

    a = A()

    m = Mock.immitate(a)
    m.mock_method("method_True", 42)
    assert m.method_False() == 42
    assert len(m.calls("method_True")) == 1
    assert len(m.calls("method_False")) == 1


async def test_async_mock():
    m = Mock()
    m.mock_method("answer", value=42, is_async=True)

    assert m.calls("answer") == []
    assert (
        await m.answer(21, question="the meaning of life, the universe and everything")
        == 42
    )
    assert len(m.calls("answer")) == 1

    call = m.calls("answer")[0]
    assert call.args == (21,)
    assert call.kwargs == {
        "question": "the meaning of life, the universe and everything",
    }
    assert (
        str(call)
        == "answer(21, question='the meaning of life, the universe and everything')"
    )


async def test_async_immitate_override():
    class A:
        async def method_True(self):
            return True

        def method_False(self):
            return True

    a = A()

    m = Mock.immitate(a)
    m.mock_method("method_True", 42)
    assert await m.method_True() == 42
    assert len(m.calls("method_True")) == 1

    m.mock_method("method_False", 42)
    assert m.method_False() == 42
    assert len(m.calls("method_False")) == 1
