import sys

resultFile = open('twitter_label.out', 'r')
sampleFile = open('data_twitter_tokenized.txt', 'r')
resultList = resultFile.readlines()
sampleList = []
for line in sampleFile.readlines():
	if line.strip():
		sampleList.append(line)

appearanceCount1 = 0.
correctCount1 = 0.
classifiedCount1 = 0.

for i in xrange(0, len(sampleList) - 1):
	result = resultList[i].rstrip().split()[0]
	sample = sampleList[i].rstrip().split()[0]
	if result == 'NEG':
		classifiedCount1 = classifiedCount1 + 1.
		if sample == 'NEG':
			correctCount1 = correctCount1 + 1.
	if sample == 'NEG':
		appearanceCount1 = appearanceCount1 + 1.

precision = correctCount1 / classifiedCount1
recall = correctCount1 / appearanceCount1
fscore = 2 * precision * recall / (precision + recall)

print 'NEG: '
print 'precision: ' + str(precision)
print 'recall: ' + str(recall)
print 'F-score: ' + str(fscore)

appearanceCount2 = 0.
correctCount2 = 0.
classifiedCount2 = 0.

for i in xrange(0, len(sampleList) - 1):
	result = resultList[i].rstrip().split()[0]
	sample = sampleList[i].rstrip().split()[0]
	if result == 'NEU':
		classifiedCount2 = classifiedCount2 + 1.
		if sample == 'NEU':
			correctCount2 = correctCount2 + 1.
	if sample == 'NEU':
		appearanceCount2 = appearanceCount2 + 1.

precision = correctCount2 / classifiedCount2
recall = correctCount2 / appearanceCount2
fscore = 2 * precision * recall / (precision + recall)

print 'NEU: '
print 'precision: ' + str(precision)
print 'recall: ' + str(recall)
print 'F-score: ' + str(fscore)

appearanceCount3 = 0.
correctCount3 = 0.
classifiedCount3 = 0.

for i in xrange(0, len(sampleList) - 1):
	result = resultList[i].rstrip().split()[0]
	sample = sampleList[i].rstrip().split()[0]
	if result == 'POS':
		classifiedCount3 = classifiedCount3 + 1.
		if sample == 'POS':
			correctCount3 = correctCount3 + 1.
	if sample == 'POS':
		appearanceCount3 = appearanceCount3 + 1.

precision = correctCount3 / classifiedCount3
recall = correctCount3 / appearanceCount3
fscore = 2 * precision * recall / (precision + recall)

print 'POS:'
print 'precision: ' + str(precision)
print 'recall: ' + str(recall)
print 'F-score: ' + str(fscore)

precision = (correctCount1 + correctCount2 + correctCount3) / (classifiedCount1 + classifiedCount2 + classifiedCount3)
recall = (correctCount1 + correctCount2 + correctCount3) / (appearanceCount1 + appearanceCount2 + appearanceCount3)
fscore = 2 * precision * recall / (precision + recall)

print 'Overall:'
print 'precision: ' + str(precision)
print 'recall: ' + str(recall)
print 'F-score: ' + str(fscore)
