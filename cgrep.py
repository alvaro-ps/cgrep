#!/usr/bin/python 
# -*- encoding: utf-8 -*- 
from __future__ import print_function
import sys 
import re 
import argparse 
from itertools import chain

from termcolor import colored, COLORS, HIGHLIGHTS
 
ALL_COLORS = list(chain(COLORS, HIGHLIGHTS))

def parse_arguments(): 
    parser = argparse.ArgumentParser('cgrep') 
    parser.add_argument(
        'regexes',
        nargs='+'
    ) 
    parser.add_argument(
        '--colors',
        nargs='+',
        default=None
    ) 
    return parser.parse_args(sys.argv[1:]) 
  
def replace_color(regex, string, color): 
    str_list = regex.findall(string) 
    for str_color in str_list: 
        new_string = string.replace(str_color, colored(str_color, color))
        string = new_string 
      
        return string 

if __name__ == '__main__':
    args = parse_arguments()
    regexes = [re.compile(regex) for regex in args.regexes]
    colors = args.colors
    for line in sys.stdin:
        for regex, color in zip(regexes, colors):
            print(replace_color(regex, line, color), end='')
