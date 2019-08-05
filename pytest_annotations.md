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

* Test Fixtures can have the following four different scopes which specify how often the fixture will be called:

* function - run the fixture once for each testing
* class - run the fixture once for each class of Tests
* module - run once when the module goes in scopes
* session - the fixture runs once when pytest start

## What are test doubles?

* Almost all code depends (i.e. collaborates) with other parts of the
system.
* Those other parts of the system are not always easy to replicate in
the unit test environment or would make tests slow if used directly.
* Test doubles are objects that are used in unit tests as replacements
to the real production system collaborators.

### Types of test doubles
* Dummy - Objects that can be passed around as necessary but do
not have any type of test implementation and should never be used.

* Fake - These object generally have a simplified functional
implementation of a particular interface that is adequate for testing
but not for production.

* Stub - These objects provide implementations with canned answers
that are suitable for the test.

* Spies - These objects provide implementations that record the
values that were passed in so they can be used by the test.

* Mocks - These objects are pre-programmed to expect specific
calls and parameters and can throw exceptions when necessary
