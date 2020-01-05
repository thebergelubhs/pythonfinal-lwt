#!/usr/bin/env python3

from sportsreference.nfl.teams import Teams

def list_team_names(my_year):

    try:
        allTeams = Teams(year=my_year)
    except:
        print ("No data for Year %s" % my_year)
        return

    for team in allTeams:
        print("%-22s %3s" % (team.name, team.abbreviation))

def run_trivia():
    year=""

    while 1:
        cmd = input ("(l/list) (h/hangman) (y/year) (q/quit/stop): ")
        cmd = cmd.lower()

        if  (cmd=="") or (cmd=="q") or (cmd=="quit") or (cmd=="stop"):
            break
        elif (cmd=="l") or (cmd=="list"):
             list_team_names(year)
        elif (cmd=="h") or (cmd=="hangman"):
             display_results(year)
        elif (cmd=="y") or (cmd=="year"):
            year = input("year : ")


if __name__ == '__main__':
     run_trivia()
