"""
Caching module for simulated OS.
"""

class Cache:
    def __init__(self):
        self.cache_store = {}

    def get(self, key):
        return self.cache_store.get(key)

    def set(self, key, value):
        self.cache_store[key] = value

    def clear(self):
        self.cache_store.clear()
