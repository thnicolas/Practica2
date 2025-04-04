def iniciar_ranking(nombres):
    stats = {'kills': 0, 'assists': 0, 'deaths': 0, 'MVPs': 0, 'score': 0}
    rank = {}
    for nombre in nombres:
        rank[nombre] = dict(stats)
    return rank