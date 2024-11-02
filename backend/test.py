import dns.resolver

def is_domain_valid(email):
    domain = email.split('@')[-1]
    try:
        dns.resolver.resolve(domain, 'MX')
        return True
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return False

print(is_domain_valid("a@a.com"))
print(is_domain_valid("sssss@gmail.com"))
print(is_domain_valid("a@abc.com"))
print(is_domain_valid("asjhdjhsdkjhsjkhjkdshkjhsdkh@gmail.com"))