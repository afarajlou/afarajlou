import unittest
from experiment import kv_cache_bytes
class Tests(unittest.TestCase):
    def test_formula(self):
        self.assertEqual(kv_cache_bytes(1, 2, 3, 4, 5, 2), 480)
    def test_scaling(self):
        a = kv_cache_bytes(1, 128, 4, 8, 64, 2)
        self.assertEqual(kv_cache_bytes(1, 256, 4, 8, 64, 2), 2*a)
if __name__ == "__main__":
    unittest.main()
