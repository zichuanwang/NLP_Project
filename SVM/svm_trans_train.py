import sys
import json
import re
from collections import Counter
from collections import OrderedDict
from random import random
tf = open('data.training.txt', 'r')
mf = open('data.training.svm.txt', 'w')
df = open('data.svmdict.txt', 'w')

wholeDict = {}
dataDict = {}

jsonDict = {}
jsonList = []

for line in tf:
	words = line.split()
	label = 1 

	if words[0] == 'NEU':
		label = 2
	elif words[0] == 'POS':
		label = 3
	else:
		label = 1

	mf.write(str(label) + ' ')

	dict = Counter()
	for i in xrange(1, len(words)):
		word = words[i]
		if word not in wholeDict:
			wholeDict[word] = len(wholeDict) + 1
		dict[wholeDict[word]] += 1

	sortedDict = OrderedDict(sorted(dict.items(), key=lambda t: t[0]))

	for key in sortedDict.keys():
		if key is 'EMO_HAPPY' or key is 'EMO_SAD':
			mf.write(str(key) + ':10 ');
		else:
			mf.write(str(key) + ':' + str(sortedDict[key]) + ' ');

	mf.write('\n')

df.write(json.dumps(wholeDict, indent=2, ensure_ascii=False, sort_keys=False))

tf.close()
mf.close()
df.close()