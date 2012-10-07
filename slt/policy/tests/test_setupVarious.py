import mock
import unittest


class TestCase(unittest.TestCase):
    """Test function: setupVarious."""

    def test(self):
        from slt.policy.setuphandlers import setupVarious
        context = mock.Mock()
        context.readDataFile.return_value = None
        setupVarious(context)
        context.readDataFile.assert_call_with('slt.policy_various.txt')
