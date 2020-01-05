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
        # print("name is: %s index is: %d" % (name, index))
        misses = 0
        maxMisses = 5
        myMisses = ''

        while misses < maxMisses:
            unknownLetters = 0

            # for every character in secret_name
            for char in name.lower():
                # see if the character is in the players guess
                if char in guesses:
                    print(char, end=" ")
                else:
                    print("_", end=" ")
                    unknownLetters += 1

            print("(misses: %s)" % myMisses)

            if unknownLetters == 0:
                print()
                print("Correct ... with %d misses! " % misses)
                break

            guess = input("guess a letter: ").lower()
            guesses += guess

            if guess not in name.lower():
                myMisses += guess.lower()
                misses = misses + 1
                print("Wrong")

            print("You have %d misses out of %d" % (misses, maxMisses))

            if misses == maxMisses:
                print("You Lose, name was: %s" % name.lower())

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
