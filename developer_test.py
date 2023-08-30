import unittest
from HomeWork5 import Developer

class DeveloperTestCase(unittest.TestCase):
    def setUp(self):
        self.developer = Developer("Jane Smith", 150, ["Python", "Django"], "jane@example.com")

    def test_work(self):
        self.assertEqual(self.developer.work(), 'I come to the office and start coding.')

    def test_position(self):
        self.assertEqual(self.developer.position(), 'Developer: Jane Smith')

    def test_add_developers(self):
        developer1 = Developer("Alice Johnson", 120, ["Python", "Flask"], "alice@example.com")
        combined_developer = self.developer + developer1
        self.assertEqual(combined_developer.name, 'Jane Smith Alice Johnson')
        self.assertEqual(combined_developer.tech_stack, ['Django', 'Flask'])
        self.assertEqual(combined_developer._day_salary, 150)

