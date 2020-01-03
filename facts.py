#!/usr/bin/env python3

from sportsreference.nfl.teams import Teams
from sportsreference.nfl.schedule import Schedule


def list_team_names(my_year):

    try:
        allTeams = Teams(year=my_year)
    except:
        print ("No data for Year %s" % my_year)
        return

    for team in allTeams:
        print("%-22s %-3s" % (team.name, team.abbreviation))

def display_teams(my_year):
    try:
        allTeams = Teams(year=my_year)
    except:
        print ("No data for Year %s" % my_year)
        return

    sortedTeams = sorted(allTeams, key=lambda team: team.wins)

    for team in sortedTeams:
        print("%-20s %-11s Won: %2d Lost: %2d pts+: %-3d pts-: %-3d ptdiff: %-4d" %
        (team.name,
         team.abbreviation,
         team.wins,
         team.losses,
         team.points_for,
         team.points_against,
         team.points_difference))


def display_results(my_year):
    abbrevName2Name = {}

    # games returned have opponents listed w/abbrev name
    # walk through all the teams, saving a dictionary of abbrev name to actual team name
    allTeams = Teams(year=my_year)
    for team in allTeams:
        abbrevName2Name[team.abbreviation] = team.name

    while 1:
        name = input("Team Name (l/list/q/quit/stop): ")
        name = name.upper()

        if (name== "") or (name== "Q") or (name== "QUIT") or (name== "STOP"):
            break
        if (name== "L") or (name=="LIST"):
            list_team_names(my_year)
            continue



def run_facts():
    year=""

    while 1:
        cmd = input ("(l/list) (t/team) (r/results) (y/year) (q/quit/stop): ")
        cmd = cmd.lower()

        if  (cmd=="") or (cmd=="q") or (cmd=="quit") or (cmd=="stop"):
            break
        elif (cmd=="l") or (cmd=="list"):
             list_team_names(year)
        elif (cmd=="t") or (cmd=="team"):
             display_teams(year)
        elif (cmd=="r") or (cmd=="results"):
             display_results(year)
        elif (cmd=="y") or (cmd=="year"):
            year = input("year : ")


if __name__ == '__main__':
     run_facts()
