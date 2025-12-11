import os 
import sys

input=sys.argv[1]
print(f"Part 2 - Reading {input}")
file = open( input,'r')
lines = file.readlines()