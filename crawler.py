from io import TextIOWrapper
from typing import List, Tuple

import atcoder
import codeforces
import infoarena

ALL_PLATFORMS = [atcoder, codeforces, infoarena]


def get_ranking(url_name: str) -> List[Tuple[str, int]]:
    for platform in ALL_PLATFORMS:
        if platform.matches(url_name):
            return platform.get_ranking(url_name)
    return []


def get_file_name(url_name: str) -> str:
    for platform in ALL_PLATFORMS:
        if platform.matches(url_name):
            return platform.get_file_name()


def filter_ranking(ranking: List[Tuple[str, int]], users: List[str]) -> List[Tuple[str, int]]:
    lowercase_names = list(map(lambda name: str.lower(name), users))

    filtered = []
    for (name, rank) in ranking:
        if str.lower(name) in lowercase_names:
            filtered.append((name, rank))
    return filtered


points = [
    [12, 10, 8, 7, 6, 5, 4, 3, 2],
    [9, 7, 6, 5, 4, 3, 2],
    [6, 4, 3, 2]
]


def get_scores(ranking: List[Tuple[str, int]], division_no: int) -> List[Tuple[str, int]]:
    division_points = points[division_no - 1]
    scores = []
    for i in range(len(ranking)):
        if i < len(division_points):
            score = division_points[i]
        else:
            score = 1
        if i > 0 and ranking[i][1] == ranking[i - 1][1]:
            score = scores[i - 1][1]
        scores.append((ranking[i][0], score))
    return scores


def read_users(file: TextIOWrapper) -> List[str]:
    return file.read().splitlines()


def get_contest_scores(url_name: str, division_no: int) -> List[Tuple[str, int]]:
    with open(get_file_name(url_name), 'r') as infile:
        users = read_users(infile)

    ranking = filter_ranking(get_ranking(url_name), users)
    return get_scores(ranking, division_no)


def print_contest_scores(url_name: str, division_no: int):
    scores = get_contest_scores(url_name, division_no)
    for contestant in scores:
        print(contestant[0], contestant[1], sep=' ', end='\n')


def valid_url(url_name: str) -> bool:
    for platform in ALL_PLATFORMS:
        if platform.matches(url_name):
            return True
    return False


def __main__():
    url = input("Copy&paste the url: ").strip()
    while valid_url(url):
        division = int(input("What division?"))
        print_contest_scores(url, division)
        url = input("Copy&paste the url: ")


__main__()
