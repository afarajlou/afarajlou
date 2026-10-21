import unittest
from experiment import roofline_gflops
class Tests(unittest.TestCase):
    def test_bandwidth(self):
        self.assertEqual(roofline_gflops(1, 100, 20), 20)
    def test_compute(self):
        self.assertEqual(roofline_gflops(10, 100, 20), 100)
if __name__ == "__main__":
    unittest.main()
