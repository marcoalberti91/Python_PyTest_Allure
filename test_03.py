from unittest import TestCase
import pytest

@pytest.mark.nrt
class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)
