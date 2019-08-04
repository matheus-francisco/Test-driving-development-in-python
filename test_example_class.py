class TestClass:
    @classmethod
    def setup_class(cls):
        print("Setup TestClass!")

    @classmethod
    def teardown_class(cls):
        print("Teardown TestClass!")

    def setup_method(self, method):
        if method == self.test1:
            print("\nSetting up test1")
        elif method == self.test2:
            print("\nSetting up test2")
        else:
            print("\nSetting up unkown test!")

    def teardown_method(self, method):
        if method == self.test1:
            print("\nTearing down test1")
        elif method == self.test2:
            print("\nTearing down test2")
        else:
            print("\nTearing down unknown test!")

    def test1(self):
        assert sum([1, 2, 3]) == 6, "Should be 6"

    def test2(self):
        assert sum([0, 2, 3]) == 5, "Should be 5"
