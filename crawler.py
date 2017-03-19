import topcoder
import codeforces
import infoarena


def get_ranking(url):
    if url.find('topcoder.com') != 1:
        return topcoder.get_ranking(url)
    if url.find('codeforces.com') != -1:
        return codeforces.get_ranking(url)
    if url.find('infoarena.ro') != -1:
        return infoarena.get_ranking(url)
    return []


def filter_ranking(ranking, users):
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


def get_scores(ranking, division):
    division_points = points[division - 1]
    scores = []
    for i in range(len(ranking)):
        score = division_points[0]
        if i > 0 and ranking[i][1] == ranking[i - 1][1]:
            score = scores[i - 1][1]
        scores.append((ranking[i][0], score))
    return scores


def read_users(file):
    file_input = open(file, 'r')
    return file_input.readlines()


def get_contest_scores(url, users_file, division):
    users = read_users(users_file)
    ranking = filter_ranking(get_ranking(url), users)
    return get_scores(ranking, division)


def print_contest_scores(url, users_file, division):
    scores = get_contest_scores(url, users_file, division)
    for contestant in scores:
        print(contestant[0], contestant[1], sep=' ', end='\n')
