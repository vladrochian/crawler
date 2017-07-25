from typing import List, Tuple

from bs4 import BeautifulSoup
import urllib.request


def get_ranking(url: str) -> List[Tuple[str, int]]:

    html: str = urllib.request.urlopen(url).read()


    return []
