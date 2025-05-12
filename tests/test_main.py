import pytest


from src.main import hello


def test_hello_default():
    assert hello() == "Hello, GitHub Actions!"


def test_hello_custom():
    assert hello("EPSI") == "Hello, EPSI!"


def test_hello_type_error():
    with pytest.raises(TypeError):
        hello(123)


def test_hello_performance():
    import time
    start = time.time()
    for _ in range(1000):
        hello("EPSI")
    assert time.time() - start < 1

