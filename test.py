a = open('twitter.out', 'r')
b = open('data_twitter_tokenized.txt', 'r')
als = a.readlines()
bls = b.readlines()
print len(als)
count = 0
for i in range(0, len(als)):
    al = float(als[i].split()[0])
    br = bls[i].split()[0]
    if not al: continue
    ar = 'NEU'
    if al > 0.33:
        ar = 'POS'
    elif al < -0.33:
        ar = 'NEG'
    if ar != br:
        count += 1
        print i, count, ar, br, al

a.close()
b.close()