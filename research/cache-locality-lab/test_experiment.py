import unittest
from experiment import simulate
class Tests(unittest.TestCase):
    def test_hits(self):
        self.assertEqual(simulate([1, 2, 1, 3, 1], 2)["hits"], 2)
    def test_empty(self):
        self.assertEqual(simulate([], 2)["hit_rate"], 0)
if __name__ == "__main__":
    unittest.main()
