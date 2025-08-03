import string, random, re

def is_valid_url(url):
    return re.match(r"^https?://[^\s/$.?#].[^\s]*$", url) is not None

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
