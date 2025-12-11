import os 
import sys

input=sys.argv[1]
print(f"Part 1 - Reading {input}")
file = open( input,'r')
lines = file.readlines()