#!/usr/bin/python 
# -*- encoding: utf-8 -*- 
from __future__ import print_function
import sys 
import re 
import argparse 

from termcolor import colored
 
def parseArguments(): 
  parser = argparse.ArgumentParser('cgrep') 
  parser.add_argument('regex', type=str) 
  parser.add_argument('--color', type=str, default='red') 
  return parser.parse_args(sys.argv[1:]) 
  
def replace_color(regex, string, color): 
  str_list = regex.findall(string) 
  for str_color in str_list: 
    new_string = string.replace(str_color, colored(str_color, color))
    string = new_string 
  
  return string 

if __name__ == '__main__':
  args = parseArguments()
  regex = re.compile(args.regex)
  color = args.color
  for line in sys.stdin:
    print(replace_color(regex, line, color), end='')
