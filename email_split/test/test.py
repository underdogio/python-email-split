# Load in our dependencies
from unittest import TestCase
from email_split import email_split


# Define our tests
class TestEmailSplitFunction(TestCase):
    def test_top_level_domain(self):
        """
        email-split splitting an email with a top-level domain
            returns the local part
            returns the domain part
        """
        email = email_split('todd@underdog.io')
        self.assertEqual(email.local, 'todd')
        self.assertEqual(email.domain, 'underdog.io')

    def test_subdomain(self):
        """
        email-split splitting an email on a subdomain
            returns the local part
            returns the domain part (including subdomain)
        """
        email = email_split('you@are.super.cool')
        self.assertEqual(email.local, 'you')
        self.assertEqual(email.domain, 'are.super.cool')
