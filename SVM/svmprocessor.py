import random
def main():
  f = open('data_tokenized/all.txt')
  testing = open('data.test.txt', 'w')
  training = open('data.training.txt', 'w')
  sample = open('data.sample.txt', 'w')
  for line in f:
    if random.random() > 0.8:
      print >>testing, line.rstrip()
      print >>sample, line.split()[0]
    else:
      print >>training, line.rstrip()
  f.close()
  testing.close()
  training.close()
  sample.close()
  
if __name__ == '__main__':
  main()