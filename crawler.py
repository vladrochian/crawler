from typing import List, Tuple, TextIO
import topcoder
import codeforces
import infoarena


def get_ranking(url: str) -> List[Tuple[str, int]]:
    if url.find('topcoder.com') != -1:
        return topcoder.get_ranking(url)
    if url.find('codeforces.com') != -1:
        return codeforces.get_ranking(url)
    if url.find('infoarena.ro') != -1:
        return infoarena.get_ranking(url)
    return []


def get_file_name(url:str) -> str:
    if url.find('topcoder.com') != -1:
        return 'topcoder';
    if url.find('codeforces.com') != -1:
        return 'codeforces'
    if url.find('infoarena.ro') != -1:
        return 'infoarena'


def filter_ranking(ranking: List[Tuple[str, int]], users: List[str]) -> List[Tuple[str, int]]:
    filtered = []
    for contestant in ranking:
        if contestant[0] in users:
            filtered.append(contestant)
    return filtered


points = [
    [12, 10, 8, 7, 6, 5, 4, 3, 2],
    [9, 7, 6, 5, 4, 3, 2],
    [6, 4, 3, 2]
]


def get_scores(ranking: List[Tuple[str, int]], division: int) -> List[Tuple[str, int]]:
    division_points = points[division - 1]
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


def read_users(file: TextIO) -> str:
    return file.read().splitlines()


def get_contest_scores(url: str, division: int) -> List[Tuple[str, int]]:
    with open(get_file_name(url), 'r') as infile:
        users = read_users(infile)

    ranking = filter_ranking(get_ranking(url), users)
    return get_scores(ranking, division)


def print_contest_scores(url: str, division: int):
    scores = get_contest_scores(url, division)
    for contestant in scores:
        print(contestant[0], contestant[1], sep=' ', end='\n')


def valid_url(url: int) -> bool:
    return (url.find('topcoder.com') != -1 or \
        url.find('codeforces.com') != -1 or \
        url.find('infoarena.ro') != -1)

url = input("Copy&paste the url: ")
while valid_url(url):
    division = int(input("What division?"))
    print_contest_scores(url, division)
    url = input("Copy&paste the url: ")

