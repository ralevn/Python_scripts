class Error(Exception):
    """ Base error"""
    pass


class NameTooShort(Error):
    """User name must be more than three characters"""


class MustContainAtSymbolError(Error):
    """Mail must have "@" symbol"""


class InvalidDomainError(Error):
    """Domain must be one of .com, .bg, .org, .net"""


def validate_name(txt):
    name = txt.split('@')[0]
    if len(name) <= 4:
        raise NameTooShort("Name must be more than 4 characters")


def validate_at_symbol(txt):
    if ("@" not in txt) or \
            ("@" in txt.split('.')[-1]):
        raise MustContainAtSymbolError("Email must contain @ and it must not be in domain")


def validate_domain(txt, domain_set):
    domain = txt.split('.')[-1]
    if domain not in domain_set:
        raise InvalidDomainError(f"Domain must be one of the following: .{', .'.join(domain_set)}")

while True:
    line = input()
    valid_domains = ('com', 'bg', 'net', 'org')
    if line == "End":
        break

    validate_name(line)
    validate_at_symbol(line)
    validate_domain(line, valid_domains)
    print("Email is valid")
