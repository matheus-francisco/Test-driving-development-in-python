import pytest


@pytest.fixture()
def setup():
    print("\nSetup")


def test_1(setup):
    assert True


@pytest.mark.usefixtures("setup")
def test_2():
    assert True
