# -*- coding:utf-8 -*- 
# Author: Zichuan Wang
# Last Update: 5/2/2014
import sys, re
import sentiment_score as ss

map_file = open('NegatingWordList.txt', 'r')
try:
    map_lines = map_file.readlines()
finally:
    map_file.close()

negation_map = {}
for line in map_lines:
    negation_map[line.strip()] = True

class ParseTree:
    def __init__(self, name, subtrees):
        self.name = name
        #print len(subtrees)
        self.subtrees = subtrees
        self.containsVP = False

        self.stopsign = False
        for tree in self.subtrees:
            if isinstance(tree, WordElement):
                if tree.word == '@@@@@':
                    self.stopsign = True
            elif tree.stopsign:
                self.stopsign = True

        if self.name == 'VP':
            self.iter_assign_containsVP()
        else:
            for tree in self.subtrees:
                if isinstance(tree, ParseTree) and tree.containsVP:
                    self.containsVP = True            

        self.negation = False
        for tree in self.subtrees:
            if isinstance(tree, WordElement):
                if tree.word in negation_map:
                    self.negation = True

        if self.name == 'VP':
            for tree in self.subtrees:
                if isinstance(tree, ParseTree) and tree.negation:
                    self.negation = True


    def iter_assign_containsVP(self):
        self.containsVP = True
        for tree in self.subtrees:
            if isinstance(tree, ParseTree):
                tree.iter_assign_containsVP()

    def calculate_score(self):
        #if not self.containsVP:
        #    return 0
        result = 0
        for subtree in self.subtrees:
            result += subtree.calculate_score()
        #print self.name, str(self.negation), str(result)
        result = result * -1 if self.name == 'VP' and self.negation else result
        return result
        

class WordElement:
    def __init__(self, word, pos):
        self.word = word
        self.pos = pos
    
    def calculate_score(self):
        score = ss.calculate_score(self.word, self.pos)
        return score

def getParseTree(line):
    if re.match('^\([a-zA-Z0-9\-]+\s\(.+\)\)$', line):
        name, subline = line[1:-1].split(' ', 1)
        #print '1:' + name + ' ' + subline
        subtrees = getParseTree(subline)
        if not isinstance(subtrees, list):
            return ParseTree(name, [subtrees])
        else:
            #print '4:' + str(len(subtrees))
            #for tree in subtrees:
            #    if isinstance(tree, ParseTree):
            #        print tree.name, str(tree.containsVP)
            return ParseTree(name, subtrees)
    elif re.match('^\([^\(\)]+\)$', line):
        pos, word = line[1:-1].split(' ', 1)
        #print '2:' + pos + ' ' +  word
        return WordElement(word, pos)
    else:
        level, start, end = 0, 0, 0
        sublines = []
        for i in range(0, len(line)):
            if line[i] == '(':
                if level == 0:
                    start = i
                level += 1
            elif line[i] == ')':
                level -=1
                if level == 0:
                    end = i + 1
                    sublines.append(line[start:end])
        #print sublines
        return [getParseTree(subline) for subline in sublines]

def getParseTrees(lines):
    result = []
    concat_lines = []
    need_break = False
    for i in range(0, len(lines)):
        line = lines[i].strip()
        if len(line) > 0:
            concat_lines.append(line)
            need_break = False
            if i == len(lines) - 1:
                tree = getParseTree(' '.join(concat_lines))
                result.append(tree)
        else:
            if need_break or i == len(lines) - 1:
                tree = getParseTree(' '.join(concat_lines))
                if isinstance(tree, ParseTree):
                    result.append(tree)
                concat_lines = []
                need_break = False                
            else:
                need_break = True
    return result

def partition_tree_into_document(trees):
    result = []
    start, end = 0, 0
    for i in range(0, len(trees)):
        tree = trees[i]
        if tree.stopsign:
            end = i
            result.append(trees[start:end])
            start = i + 1
    return result

def analyze():
    in_path = sys.argv[1]
    in_file = open(in_path, 'r')
    try:
        in_lines = in_file.readlines()
    finally:
        in_file.close()
    trees = getParseTrees(in_lines)
    parititioned_trees = partition_tree_into_document(trees)

    result_scores = []
    for ptrees in parititioned_trees:
        pscore = 0
        pcount = 0
        for tree in ptrees:
            score = tree.calculate_score()
            pcount += 1 if score != 0 else 0
            pscore += score
        result_scores.append(float(pscore) / pcount if pcount != 0 else 0)

    print result_scores
    output_results(result_scores)

def output_results(result_scores):
    outlines = []
    for score in result_scores:
        label = 'NEU'
        if score > 0.15:
            label = 'POS'
        elif score < -0.05:
            label = 'NEG'
        outlines.append(label + '\r\n')
    out_file = open(sys.argv[2], 'w')
    try:
        out_file.writelines(outlines);
    finally:
        out_file.close()


def check_input_validity(cmds):
    if len(cmds) != 2:
        return False
    return True

if __name__ == "__main__":
    if check_input_validity(sys.argv[1:]):
        analyze()
    else:
        print "Usage: python sentiment_analyzer.py IN_FILE OUT_FILE"