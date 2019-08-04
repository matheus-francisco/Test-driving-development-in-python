def setup_module(module):
    print("Setup Module!")


def teardown_module(module):
    print("Teardown Module")


def setup_function(function):
    if function == test1:
        print("\nSetting up test1")
    elif function == test2:
        print("\nSetting up test2")
    else:
        print("\nSetting up unkown test!")


def teardown_function(function):
    if function == test1:
        print("\nTearing down test1")
    elif function == test2:
        print("\nTearing down test2")
    else:
        print("\nTearing down unknown test!")


def test1():
    assert sum([1, 2]) == 3, "should be 3"


def test2():
    # print("Executing test2!")
    assert sum([1, 1]) == 2, "should be 2"
