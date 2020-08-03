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
    def test_scalar(self):
        l = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sodium'))
        self.assertTrue(l is not None)

if __name__ == "__main__":
    # Generate reference bit lists for tests.
    test_oblivious = Test_oblivious()
