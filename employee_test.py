import unittest
from HomeWork5 import Employee

class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("John Doe", 100, "john@example.com")

    def test_work(self):
        self.assertEqual(self.employee.work(), 'I come to the office.')

    def test_check_salary(self):
        self.assertEqual(self.employee.check_salary(10), 500)

    def test_str(self):
        self.assertEqual(str(self.employee), "Employee: John Doe")

    def test_eq(self):
        employee2 = Employee("Jane Smith", 100, "jane@example.com")
        self.assertTrue(self.employee == employee2)