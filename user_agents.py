import random

HEADERS = {
    1: {
        "user-agent": "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/5350 (KHTML, like Gecko) Chrome/39.0.870.0 Mobile Safari/5350",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    },
    2: {
        "user-agent": "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_8_7 rv:3.0) Gecko/20200806 Firefox/36.0",
        "accept": "*/*"
    },
    3: {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_5 rv:4.0; en-US) AppleWebKit/533.39.2 (KHTML, like Gecko) Version/4.0.2 Safari/533.39.2",
        "accept": "*/*"
    },
    4: {
        "user-agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/534.12.4 (KHTML, like Gecko) Version/4.1 Safari/534.12.4",
        "accept": "*/*"
    },
    5: {
        "user-agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/533.44.1 (KHTML, like Gecko) Version/5.0 Safari/533.44.1",
        "accept": "*/*"
    },
    6: {
        "user-agent" : "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    },
    7: {
        "user-agent" : "Apache/2.4.34 (Ubuntu) OpenSSL/1.1.1 (internal dummy connection)",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    },
    8: {
        "user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    },
    9: {
        "user-agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    },
    10: {
        "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    },
}

def get_header():
    result = {}
    i = random.randint(1, len(HEADERS))
    result = HEADERS[i]
    return result



