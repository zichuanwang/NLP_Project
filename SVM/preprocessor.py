import nltk, re, pprint
from subprocess import Popen, PIPE, STDOUT
slangTable = {}
emoticonTable = {}

def createSlangTable():
  f = open('dict/SlangLookupTable.txt')
  for line in f:
    array = line.rstrip().split(' ', 1)
    str = array[1].replace('\xa0', ' ')
    str = str.replace('\x92', '\'')
    slangTable[array[0]] = str

def createEmoticonTable():
  f = open('dict/EmoticonLookupTable.txt')
  for line in f:
    array = line.rstrip().rsplit(' ', 2)
    intVale = array[1]    
    value = 'EMO_HAPPY' if intVale > 0 else 'EMO_SAD'
    emoticonTable[array[0]] = value

def tokenize(fname):
  nf = open(fname + '_tokenized.txt', 'w')
  p = Popen(['java', '-cp', 'corenlp.jar', 
    'edu.stanford.nlp.process.PTBTokenizer', fname + '_new.txt', '-preserveLines'], stdout=PIPE)
  while True:
    line = p.stdout.readline()
    if line == '':
      break
    nf.write(line)
  nf.close()

def format(fname):
  f = open(fname + '.txt')
  nf = open(fname + '_new.txt', 'w')
  firstLine = True
  for line in f:
    if firstLine:
      firstLine = False
      continue
    scores = line.split('\t', 2)
    tag = ''
    if len(scores) <= 1:
      print scores
      continue
    if scores[0] is scores[1]:
      tag = 'NEU'
    elif scores[0] > scores[1]:
      tag = 'POS'
    else:
      tag = 'NEG'

    line = ' '.join(re.sub("(@[A-Za-z0-9]+)|#|(?:http://|www.)[^\"\' ]+", " ", line).split())
    words = [w.lower() for w in line.split()]
    for i in range(len(words)):
      if words[i] in slangTable:
        words[i] = slangTable[words[i]]
      if words[i] in emoticonTable:
        words[i] = emoticonTable[words[i]]
        
    nf.write(tag + ' ' + ' '.join(words[2:]) + '\n')

def main():
  createEmoticonTable()
  createSlangTable()
  fileNames = ['data_bbc', 'data_digg', 'data_myspace', 'data_rw', 'data_twitter', 'data_YouTube']
  for fileName in fileNames:
    format('data_raw/' + fileName)
    tokenize('data_raw/' + fileName)

if __name__ == '__main__':
  main()
