from senticnet5 import word

def score(s):
  bad = []
  good = []
  total=0
  sum=0
  for i in s.split():
    i=i.split(",")
    i=i[0].split("!")
    i=i[0].split(".")
    i=i[0].split("?")

    if scoreOne(i[0]) >  .3:
      good.append(i[0])
    elif scoreOne(i[0]) < -.3:
      bad.append(i[0])
    if scoreOne(i[0])!=0:
      total+=1
      print(scoreOne(i[0]))
      sum+=scoreOne(i[0])
  return [sum/total,good, bad]

def scoreOne(x):
  x=x.lower()

  try:

    if abs(float(word(x).polarity_value()))>.3:
      return float(word(x).polarity_value())
    return 0
  except:
    return 0

def scoreTwo(x,y):
  x=x+"_"+y
  try:
    return float(word(x).pleasant())
  except:
    return -2

def scoreThree(x,y,z):
  x=x+"_"+y+"_"+z
  try:
    return float(word(x).pleasant())
  except:
    return -2

if __name__ == '__main__':
  print(score(input()))

