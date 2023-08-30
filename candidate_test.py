import unittest
from HomeWork5 import Candidate

class CandidateTestCase(unittest.TestCase):
    def setUp(self):
        self.candidate = Candidate("Bob", "Williams", "bob@example.com", ["Java", "Spring"], "Java", "Senior")

    def test_full_name(self):
        self.assertEqual(self.candidate.full_name, 'Bob Williams')

    def test_generate_candidates(self):
        candidates = Candidate.generate_candidates("test_candidates.csv")
        self.assertEqual(len(candidates), 2)

