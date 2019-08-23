from collections import defaultdict
from string import ascii_uppercase as au


def landing_site(obstacles):

    all_hexes = {c+str(r) for c in au[:12] for r in range(1, 10)}

    def adjacent_6_hexes(hex):
        c, r = au.index(hex[0]), int(hex[1])
        h1 = [au[c+cd] + str(r+rd) for cd in (1, -1) for rd in [-(1-c % 2), c % 2]]
        h2 = [au[c] + str(r+rd) for rd in (1, -1)]
        return set(map(lambda h: h if h in all_hexes else None, h1+h2))

    def search_adjacent_hexes(start_hex):
        radius = 0
        done_hexes = {start_hex}
        next_hexes = {start_hex}
        while next_hexes:
            for nx in set(next_hexes):
                adj_hexes = adjacent_6_hexes(nx)
                if None in adj_hexes or obstacles & adj_hexes:
                    return radius, done_hexes
                next_hexes |= adj_hexes
            next_hexes -= done_hexes
            done_hexes |= next_hexes
            radius += 1

    site_dic = defaultdict(set)
    area_dic = defaultdict(set)
    for tgt_hex in all_hexes - obstacles:
        r, hexes = search_adjacent_hexes(tgt_hex)
        site_dic[r].add(tgt_hex)
        area_dic[r] |= hexes

    max_r = max(site_dic, default=0)
    if max_r:
        return sorted(site_dic[max_r]), list(area_dic[max_r])
    else:
        return [], []

