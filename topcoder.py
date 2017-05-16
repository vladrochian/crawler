from base import *
from typing import List, Tuple
from bs4 import BeautifulSoup
from bs4.element import Tag


def get_ranking(url: str) -> List[Tuple[str, int]]:
    html = get_html(url)

    soup = BeautifulSoup(html, 'lxml')

    table = soup.find_all('table', class_='mainContent')
    print(table)
    return []
