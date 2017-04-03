from typing import List, Tuple
import json


# could be more than one participant in a team
def get_handle(item: dict) -> str:
    return item['party']['members'][0]['handle']


def get_score(item: dict) -> str:
    return item['points']


def get_ranking(url: str) -> List[Tuple[str, int]]:
    response = urllib.request.urlopen(url)
    str_response = response.read().decode('utf-8')
    data = json.loads(str_response)

    lst = []
    for item in data['result']['rows']:
        lst.append((get_handle(item), get_score(item)))

    lst.sort(key=lambda x: x[1], reverse=True)
    return lst
