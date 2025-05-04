# Accepting Arguments from command line
import sys

name = sys.argv[1]

print("Hello " + name)

#py AcceptingArguments.py Andy 25
#Hello Andy


#py AcceptingArguments.py Andy 25
#Esto es lo que sale de la consola
#['AcceptingArguments.py', 'Andy', '25']

import argparse

parser = argparse.ArgumentParser(
  description="This program prints the name of my dogs"
)

parser.add_argument('-c', '--color', metavar='color', required=True,choices={'red', 'yellow'} ,help='the color to search for')

args = parser.parse_args()

print(args.color)

# py AcceptingArguments.py -c red 
#red