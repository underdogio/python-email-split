# Define an email class
class Email(object):
    def __init__(self, local, domain):
        # local is content before `@` in email
        # domain is content after `@` in email
        self.local = local
        self.domain = domain

    @classmethod
    def split_email(cls, email):
        """Break up an email and initialize a new class"""
        # Break up our email at its `@`
        # https://docs.python.org/2/library/stdtypes.html#str.partition
        local, _, domain = email.partition('@')

        # Initialize and return our class
        return Email(local=local, domain=domain)


# Define our main export
email_split = Email.split_email
