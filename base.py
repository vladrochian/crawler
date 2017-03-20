import urllib.request


def get_html(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Chrome/33.0.1750.117'})
    response = urllib.request.urlopen(req)
    html = response.read()
    return html


def get_first_tag(html):
    if html[0] != '<':
        return None
    pos = html.find('>')
    if pos == -1:
        return None
    return html[:pos + 1], html[pos + 1:]


def get_first_text_element(html):
    pos = html.find('<')
    if pos == -1:
        return html, ''
    return html[:pos], html[pos:]


def is_tag(element):
    return element[0] == '<' and element[-1] == '>'


def is_self_closing(tag):
    return tag[-2] == '/' or tag[1] == '!'


def is_closing_tag(tag):
    return tag[1] == '/'


def get_first_element(html):
    if html[0] != '<':
        return get_first_text_element(html)
    result, html = get_first_tag(html)
    if is_self_closing(result):
        return result
    level = 1
    while html != '' and level > 0:
        if html[0] == '<':
            tag, html = get_first_tag(html)
            if is_closing_tag(tag):
                level -= 1
            elif not is_self_closing(tag):
                level += 1
        else:
            tag, html = get_first_text_element(html)
        result += tag
    return result, html


def get_element_content(element):
    if not is_tag(element) or is_closing_tag(element):
        return ''
    return element[element.find('>') + 1:element.rfind('<')]


def find_element(html, type):
    pass
