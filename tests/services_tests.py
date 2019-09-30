from ptest.decorator import TestClass, Test


@TestClass()
class ServicesTests:

    @Test()
    def dummy_test(self):
        assert 1 == 1
