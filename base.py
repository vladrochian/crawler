import urllib.request


def get_html(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Chrome/33.0.1750.117'})
    response = urllib.request.urlopen(req)
    html = response.read()
    return html
