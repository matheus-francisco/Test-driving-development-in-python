import pytest


@pytest.fixture()
def setup1():
    print("\nSetup 1")
    yield
    print("\nTeardown 1")


@pytest.fixture()
def setup2(request):
    print("\n Setup 2")

    def teardown_a():
        print("\n Teardown A")

    def teardown_b():
        print("\n Teardown B")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)


def test_1(setup):
    assert True


@pytest.mark.usefixtures("setup")
def test_2():
    assert True
