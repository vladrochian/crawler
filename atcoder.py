import requests


class user:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank


def get_user(data, pos):
    act = user("", 0)
    # get the rank
    pos = data.find("rank", pos)
    if pos == -1:
         return -1, act

    while data[pos].isdigit() == False:
        pos += 1
    aux = ""
    while data[pos].isdigit() == True:
        aux += data[pos]
        pos += 1
    act.rank = int(aux)

    # get the name
    pos = data.find("user_screen_name", pos)
    pos += 19

    while data[pos] != '''"''':
        act.name += data[pos]
        pos += 1

    return pos, act


def get_ranking(site):
    page = requests.get(site)
    data = page.text
    ord = {}

    pos = 0
    while 1:
        act = user("", 0)
        pos, act = get_user(data, pos)
        if pos == -1:
            break
        ord[act.name] = act.rank

    return ord

site = input('Give me the site :')
data = get_ranking(site)

order = []

fin = open("atcoder", "r")
for contestant in fin.read().split("\n"):
    try:
        order.append((data[contestant], contestant))
    except:
        pass

order.sort()
for contestant in order:
    print(str(contestant[0]) + " - " + contestant[1])
