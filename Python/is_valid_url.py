import re
def is_valid_url(url):
    pattern = r'^(http|https)://[a-zA-Z0-9.-]+.[a-zA-Z]{2,}'
    return re.match(pattern, url) is not None
