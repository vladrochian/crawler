import urllib.request


def get_html(url, user_agent='Chrome/33.0.1750.117'):
    req = urllib.request.Request(url, headers={'User-Agent': user_agent})
    response = urllib.request.urlopen(req)
    html = response.read()
    return html
