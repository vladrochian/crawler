from typing import List, Tuple
from base import *
from bs4 import BeautifulSoup
from bs4.element import Tag


def get_handle(item: Tag) -> str:
    children = item('div')
    for child in children:
        spans = child('span')
        for span in spans:
            if span['class'] == ['username']:
                return str((span.find('a').contents[0]))


def get_score(item: Tag) -> str:
    score = 0
    children = item('td', class_='number score')
    for child in children:
        score = max(score, int((child.contents[0]).string))
    return score


def get_ranking(url: str) -> List[Tuple[str, int]]:
    url = url.rstrip()
    url += '?rankings_display_entries=500'

    html = get_html(url)

    soup = BeautifulSoup(html, 'lxml')

    tr = soup.find_all('tr', class_='odd')
    tr += soup.find_all('tr', class_='even')

    lst = []
    for item in tr:
        lst.append([get_handle(item), get_score(item)])
    lst.sort(key=lambda x: x[1], reverse=True)
    return lst
