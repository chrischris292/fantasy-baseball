from pprint import pprint
from espn_api import EspnApi
import sys
import pickle
import requests

from lineup_settings import LineupSettings


def password(user):
    with open(user + "_pass.txt", "w+") as pass_file:
        return pass_file.read()


username = sys.argv[1]
password = password(username)

api = EspnApi(username, password)

# print('fetching all lineups...')
# resp = api.all_info()
# pickle.dump(resp, open("all_info.p", "wb+"))

league = api.league()

for team in league.teams:
    print(team.team_id)
    print(team.stats.era())


# lineup = api.lineup()
#
#
# def print_lineup(l):
#     for slot, players in l.player_dict.items():
#         print(slot)
#         for p in players:
#             print(p)
#
#
# settings = api.lineup_settings()
# # lineup = pickle.load(open("lineup.p", "rb"))
# # settings = LineupSettings(pickle.load(open("settings.p", "rb")).slot_counts)  # for casting str->str to int->int
#
#
# possibles = lineup.possible_lineups(settings)
# # lineup_dict = dict()
# # for poss_lineup in possibles:
# #     benched = poss_lineup.benched()
# #     lineups_same_benched = lineup_dict.get(benched, list())
# #     lineups_same_benched.append(poss_lineup)
# #     lineup_dict[benched] = lineups_same_benched
#
# # print("{} different configurations of benched players".format(len(lineup_dict)))
#
#
# def low_transition_lineup(cur, possible_lineups):
#     for l in possible_lineups:
#         if len(cur.transitions(l)) == 3:
#             return l
#
# rand_lineup = low_transition_lineup(lineup, possibles)
# transitions = lineup.transitions(rand_lineup)
# for t in transitions:
#     print("{} {} {}".format(t[0], t[1], t[2]))
#
# pprint(api.set_lineup(rand_lineup))

"""
GOAL:
    - set lineup each day based on ideal lineup (fantasy points)
        * get current roster
        * get lineup settings
        * scan (all possible?) lineups
        * determine projections for each player
        * determine fantasy points generated by ea/ lineup (based on % to next guy?)
        * set best lineup
    
    Data types:
    Roster = [Player, ...]
        (Roster LineupSettings) -> [Lineup, ...] all possible lineups
        
    Player = {
        name: ...
        id: ...
        position?: ...
        possibleSlots: [Num, ...]
    }
    
    LineupSettings = {
        slot_id: count,
        ...
    }
    
    Lineup = {
        0: [Player, ...]
        1: [Player, ...]
        ...
    }
        (Lineup LineupSettings? Projections) -> Statistics
    
    Projections = { Player: Statistics }
    
    ScoringSettings: [(id, reverse?), ...]
    
    Statistics: {
        id: value,
        ...
    }
    
    League: [Team, ...]
    
    Team: {
        id: Int,
        lineup: Lineup,
        year_stats: Statistics,
    }
    

"""



