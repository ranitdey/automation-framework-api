from ptest.decorator import BeforeSuite, TestClass, AfterSuite, BeforeClass
from ptest.plogger import preporter

from library.test_dependency_util import DependencyTracker


@TestClass()
class BaseTest(DependencyTracker):

    @BeforeSuite()
    def before_suite(self):
        preporter.info("========================Starting API automation suite========================")

    @AfterSuite(always_run=True)
    def after_suite(self):
        preporter.info("========================End of API automation suite========================")

    @BeforeClass()
    def before_class(self):
        preporter.info("Getting authorization token")
        # Getting auth token flow goes here
