from pprint import pprint
from espn_api import EspnApi
from fangraphs_api import FangraphsApi
import sys
import pickle
import requests

from lineup_settings import LineupSettings

#
# def password(user):
#     with open(user + "_pass.txt", "w+") as pass_file:
#         return pass_file.read()
#
#
# username = sys.argv[1]
# password = password(username)
#
# api = EspnApi(username, password)
#
# league = api.league()
# settings = api.scoring_settings()
#
# points = league.points(settings)
# for (team_id, points) in points.items():
#     print("{}\t{}\n".format(team_id, points))

proj = FangraphsApi().pitcher_projections()
print(proj.items())
name_and_average = list(map(lambda n: (n[0], n[1].whip()), proj.items()))
for name, stats in sorted(name_and_average, key=lambda na: na[1]):
    print("{}\t{}\n".format(name, stats))

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
    
    Now, calculate optimal lineup:
    
    Given:
    * League
    * Team Id
    * Projections
    * Scoring Settings
    * set of starters
    
    Determine:
    * point value of those starters
    
    Approach:
    - calculate all others' stats based on curr lineup, projections
    - save my curr year stats
    - calc my stats with daily projections
    - for each stat, calc my % difference vs. all others ... ? sum to total points
    
    
    

"""



