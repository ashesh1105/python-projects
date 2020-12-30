import unittest
from unittest.mock import patch
import requests

from employee import Employee

"""
1) setUpClass first and once per test class.
2) tearDownClass runs at the end of all the tests run.
3) setUp runs once per every test and before the test runs.
4) tearDown runs once per test and after the test runs.
If you upcomment print statements from class below, you'll see:
from setUpClass
from setUp
from test_apply_raise
from tearDown
from setUp
from test_email
from tearDown
from setUp
from test_fullname
from tearDown
from tearDownClass
"""
class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('from setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('from tearDownClass')

    # setUp is called each time a test method runs and tearDown is called after that test method is done
    # Uncomment the print statements to see how setUp and tearDown is run for each of test methods!
    # Another thing, tests do not necessarily run in order, so they must be independent of each other
    def setUp(self):
        print('from setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        print('from tearDown')

    def test_email(self):
        print('from test_email')

        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('from test_fullname')

        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('from test_apply_raise')

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):

        """
        patch target: 'package.module.ClassName'
        - package must be importable from the test class where patch is used!
        - patch where the object is used and not where it is defined!
        - There are 3 ways of patching:
        1) Context Manager, as in the example below in this method.
           Smallest Scope - lives only for a part of a function.
        2) Decorators (Function and Class)
           Function level: Lives for entire life of a single function
           Class Level: Lives for scope of entire class. Test test_monthly_schedule_another below demos that!
        3) Manual start / stop - when there are multiple mocks to deal with!
           Scope is, whatever we define it to be. Normally a class
           You can add them in setUp and stop them in tearDown but since it is so important to stop the mocks,
           it is better to add a cleanup test method that will stop all the mocks and call it at the end of setUp
           this way:
           def setUp(self):
              mock_name = patch('my_module.name').start()
              mock_bday = patch('my_module.birth_day').start()
              mock_addr = patch('my_module.address').start()
              self.addCleanup(patch.stopall)

        """

        # Context Manager way of mocking something, in this case, call to http://www.company.com
        # Note: your mock target needs to be where a functionality is used,
        # in this case it is in employee.py -> requests.get
        # You need to assign results of mock to a variable, in below it is mocked_get
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            # Positive test case
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            # Negative test case, say, when website is down
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')

    # Example of patch(ing) with decorator. You can add return_value as well as second argument on @patch
    @patch('employee.requests.get')
    def test_monthly_schedule_another(self, mocked_get):
        mocked_get.return_value.ok = True
        mocked_get.return_value.text = 'Some valid response!'

        schedule = self.emp_1.monthly_schedule('Jan')
        mocked_get.assert_called_with('http://company.com/Schafer/Jan')
        self.assertEqual(schedule, 'Some valid response!')




# Allows this file to be run as a normal python file: python test_employee.py
if __name__ == '__main__':
    unittest.main()