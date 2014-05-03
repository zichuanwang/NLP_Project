import sys
import json
import re
from collections import Counter
from collections import OrderedDict
tf = open('data.test.txt', 'r')
mf = open('data.test.svm.txt', 'w+')
df = open('data.svmdict.txt', 'r')
raw = unicode(df.read(), errors='replace')
wholeDict = json.loads(raw)

for line in tf:
	words = line.split()
	mf.write(str(0) + ' ')

	dict = Counter()
	for i in xrange(0, len(words)):
		word = words[i]
		if word in wholeDict:
			dict[wholeDict[word]] += 1

	sortedDict = OrderedDict(sorted(dict.items(), key=lambda t: t[0]))

	for key in sortedDict.keys():
		mf.write(str(key) + ':' + str(sortedDict[key]) + ' ');

	mf.write('\n')

tf.close()
mf.close()
df.close()