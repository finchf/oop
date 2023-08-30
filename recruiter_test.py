import unittest
from HomeWork5 import Recruiter

class RecruiterTestCase(unittest.TestCase):
    def setUp(self):
        self.recruiter = Recruiter("John Doe", 100, "john@example.com")

    def test_work(self):
        self.assertEqual(self.recruiter.work(), 'I come to the office and start hiring.')

    def test_position(self):
        self.assertEqual(self.recruiter.position(), 'Recruiter: John Doe')
