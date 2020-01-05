#!/usr/bin/env python3

import random

from sportsreference.nfl.teams import Teams
from sportsreference.nfl.roster import Roster

def list_team_names(my_year):

    try:
        allTeams = Teams(year=my_year)
    except:
        print ("No data for Year %s" % my_year)
        return

    for team in allTeams:
        print("%-22s %3s" % (team.name, team.abbreviation))

def run_hangman_game(year):
    lastAbbrevName = ""
    while 1:
        name = input("Team Name (l/list/q/quit/stop): ")
        name = name.upper()

        if (name == "") or (name == "Q") or (name == "QUIT") or (name == "STOP"):
            break

        if (name == "L") or (name == "LIST"):
            list_team_names(year)
            continue

        print("Getting Roster for %s, year %s" % (name, year))

        # only get roster is not same as last one
        if lastAbbrevName != name:
            try:
                roster = Roster(name, year=year)
                lastAbbrevName = name
            except:
                print("Unknown Team Name Abbreviations, use list to display Team and Abbreviations")
                continue

        numPlayers = len(roster.players)

        print("Ready to start guessing Players name len=%d ..." % numPlayers)

        # generate a random number between 0 and the number of players on the roster-1
        index = random.randint(0, numPlayers-1)

        #here we set the secret
        player = roster.players[index]

        #creates an variable with an single value of space ' '
        guesses = ' '

        name = player.name
        print("name is: %s index is: %d" % (name, index))

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
             run_hangman_game(year)
        elif (cmd=="y") or (cmd=="year"):
            year = input("year : ")


if __name__ == '__main__':
     run_trivia()
