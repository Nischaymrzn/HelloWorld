import hashlib
def shorten_url(url):
    return hashlib.md5(url.encode()).hexdigest()[:6]
