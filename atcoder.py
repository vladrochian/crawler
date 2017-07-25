import json
from typing import Tuple, List

import urllib.request
import regex as re


def get_ranking(url_name: str) -> List[Tuple[str, int]]:
    if list(url_name)[-1] != '/':
        url_name += "/"
    url_name += "standings/"

    print(url_name)
    html = urllib.request.urlopen(url_name).read()
    json_string = "[" + (re.search('ATCODER\.standings = {.*data: \[(.*)\].*};',
                                   str(html), re.IGNORECASE).group(1)) + "]"
    json_obj = json.loads(json_string)

    ret = []
    for participant in json_obj:
        ret.append((participant['user_screen_name'], participant['rank']))
    return ret


def matches(url: str) -> bool:
    return url.find("atcoder.jp") != -1


def get_file_name() -> str:
    return "atcoder"
