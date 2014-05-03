# -*- coding:utf-8 -*- 
# Author: Zichuan Wang
# Last Update: 5/1/2014

import sys, os
from subprocess import Popen, PIPE, STDOUT

def get_parse_tree(cmds):
    input_file_path, output_file_path = cmds
    p = Popen(['java', '-cp', 'stanford-parser.jar', '-mx200m',
        'edu.stanford.nlp.parser.lexparser.LexicalizedParser',
        '-retainTMPSubcategories', '-outputFormat', 'penn',
        'englishPCFG.ser.gz',  input_file_path], stdout = PIPE)

    output_lines = []
    while True:
        line = p.stdout.readline()
        if line.startswith('Loading parser'): continue
        if line.startswith('Parsing file'): continue
        if line.startswith('Parsing ['): continue
        if line == '':
            break
        output_lines.append(line + '\r\n');

    output_file = open(output_file_path, 'w')
    try:
        output_file.writelines(output_lines)
    finally:
        output_file.close()

def check_input_validity(cmds):
    if len(cmds) != 2:
        return False
    return True

if __name__ == "__main__":
    if check_input_validity(sys.argv[1:]):
        get_parse_tree(sys.argv[1:])
    else:
        print "Usage: python parse_tree.py INPUTFILE OUTPUTFILE"