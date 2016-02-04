from unittest import TestCase
from email_split import email_split


class TestRunFunction(TestCase):
    def test_run_exists(self):
        self.assertTrue(bool(email_split.run))
