#!/usr/bin/env python3
import facts
import trivia

def main ():

    while 1:
        cmd = input ("(f/facts) (t/trivia) (q/quit/stop): ")
        cmd = cmd.lower()

        if  (cmd=="") or (cmd=="q") or (cmd=="quit") or (cmd=="stop"):
            break
        elif (cmd=="f") or (cmd=="facts"):
            facts.run_facts()
        elif (cmd=="t") or (cmd=="trivia"):
            trivia.run_trivia()

if __name__ == '__main__':
    print("Welcome to Sports App")
    main()
