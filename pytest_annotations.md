## What is PyTest?

* PyTest is a python unit testing framework
* it provides the ability to create Tests, Test Modules, and Test Fixtures
* Uses the built-in python assert statement
* Has command line parameters to help filter which tests are executed and in what order.

## Test Discovery

* pytest will automatically dicover test when you execute based on a standard naming convention
* Test functions should include "test" at the beginning of the functions name.
* Classes with tests in them should have "Test" at the beginning of the Classes name and not 
have an "__ini__" methdo
* Filenames of test modules should start or end with "test".. "test_example.py"


## XUnit Style etup and Teardown
```
def setup_module():
def teardown_module():
def setup_function():
def teardown_function():
def setup_class():
def teardown_class():
def setup_method():
def teardown_method():
```

* XUnit style setup/teardown functions will execute code before and after:
* Test Modules
* Test Functions
* Test Classes
* Test Methods in Test Casses

* This help to reduce code duplicate
* look into file "test_example_class.py and test_example_setup_teardown.py"

## Test Fixtures
```
@pytes.fixture()
```

