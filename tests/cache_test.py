import unittest

from sys_path_utils import cymake_in_syspath

with cymake_in_syspath():
    from cymake.cache import Cache

class TestCache(unittest.TestCase):
    def setUp(self) -> None:
        self.cache = Cache()

    def test_get_set(self):
        self.cache.set('foo', 'bar')
        self.cache.set('lol', 1)
        self.cache.set('kek', 42)

        self.assertEqual(self.cache.get('lol'), 1)
        self.assertEqual(self.cache.get('foo'), 'bar')
        self.assertEqual(self.cache.get('kek'), 42)