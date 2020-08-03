import ctypes
import ctypes.util
from parts import parts
from bitlist import bitlist
from fountains import fountains
from unittest import TestCase

from oblivious import *

def check_or_generate(self, fs, bits):
    if bits is not None:
        self.assertTrue(all(fs)) # Check that all tests succeeded.
    else:
        return bitlist(list(fs)).hex() # Return target bits for this test.

def check_or_generate_operation(self, fun, lengths, bits):
    fs = fountains(sum(lengths), seed=0, limit=256, bits=bits, function=fun)
    return check_or_generate(self, fs, bits)

class Test_oblivious(TestCase):
    def test_1(self):
        l = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sodium'))
        self.assertTrue(l is not None)

    def test_2(self):
        l = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sodium'))
        self.assertTrue(hasattr(l, 'crypto_box_publickeybytes')
        self.assertTrue(hasattr(l, 'crypto_box_secretkeybytes')

    def test_3(self):
        l = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sodium'))
        self.assertTrue(hasattr(l, 'crypto_core_ristretto255_bytes')

    def test_4(self):
        l = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sodium'))
        self.assertTrue(hasattr(l, 'crypto_core_ristretto255_scalar_random')

    def test_5(self):
        l = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sodium'))
        self.assertTrue(hasattr(l, 'crypto_scalarmult_ristretto255_base')

    def test_6(self):
        l = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sodium'))
        self.assertTrue(hasattr(l, 'crypto_scalarmult_ristretto255')

    def test_7(self):
        l = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sodium'))
        self.assertTrue(hasattr(l, 'crypto_core_ristretto255_add')

    def test_8(self):
        l = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sodium'))
        self.assertTrue(hasattr(l, 'crypto_core_ristretto255_sub')

    def test_9(self):
        l = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sodium'))
        self.assertTrue(hasattr(l, 'crypto_core_ristretto255_sub')

    #def test_scalar2(self):
    #    self.assertTrue(sodium is not None)

if __name__ == "__main__":
    # Generate reference bit lists for tests.
    test_oblivious = Test_oblivious()
