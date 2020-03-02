from senticnet5 import word



def score(s):
  bad = []
  good = []
  total=0
  sum=0
  arr=[]
  for i in s.split():
    i=i.split(",")
    i=i[0].split("!")
    i=i[0].split(".")
    i=i[0].split("?")
    arr.append(i[0])

  for v, i in enumerate(arr):
    
    
    if scoreOne(i) >  .3:
      good.append(i)
      total+=1
      sum+=scoreOne(i)
    elif scoreOne(i) < -.3:
      bad.append(i)
      total+=1
      sum+=scoreOne(i)
    try: 
      
      if scoreTwo(i,arr[v+1]) >  .3:
        good.append(i+"_"+arr[v])
        total+=1
        sum+= scoreTwo(i,arr[v+1])
        
      elif scoreTwo(i,arr[v+1]) < -.3:
        
        bad.append(i+"_"+arr[v+1])
        total+=1
        sum+= scoreTwo(i,arr[v+1])
        
    except:
      pass
    try:
      if scoreThree(i,arr[v+1], arr[v+2]) >  .3:
        good.append(i+"_"+arr[v+1]+"_"+arr[v+2])
        total+=1
        sum+= scoreThree(i,arr[v+1], arr[v+2])
      elif  scoreThree(i,arr[v+1], arr[v+2]) < -.3:
        bad.append(i+"_"+arr[v+1]+"_"+arr[v+2])
        total+=1
        sum+= scoreThree(i,arr[v+1], arr[v+2])
    except:
      pass
    try:
      if scoreFour(i,arr[v+1], arr[v+2], arr[v+3]) >  .3:
        good.append(i+"_"+arr[v+1]+"_"+arr[v+2]+"_"+arr[v+3])
        total+=1
        sum+= scoreFour(i,arr[v+1], arr[v+2], arr[v+3])
      elif  scoreFour(i,arr[v+1], arr[v+2], arr[v+3]) < -.3:
        bad.append(i+"_"+arr[v+1]+"_"+arr[v+2]+"_"+arr[v+3])
        total+=1
        sum+= scoreFour(i,arr[v+1], arr[v+2], arr[v+3])
    except:
      pass
   
  try:
    
    avg=sum/total
  except:
    avg=0
  return [avg,good, bad]

def scoreOne(x):
  x=x.lower()

  try:

    if abs(float(word(x).polarity_value()))>.3:
      return float(word(x).polarity_value())
    return 0
  except:
    return 0

def scoreTwo(x,y):
  x=x.lower()+"_"+y.lower()
  try:

    if abs(float(word(x).polarity_value()))>.3:
      return float(word(x).polarity_value())
    return 0
  except:
    return 0


def scoreThree(x,y,z):
  x=x.lower()+"_"+y.lower()+"_"+z.lower()
  try:

    if abs(float(word(x).polarity_value()))>.3:
      return float(word(x).polarity_value())
    return 0
  except:
    return 0

def scoreFour(x,y,z,a):
  x=x.lower()+"_"+y.lower()+"_"+z.lower()+"_"+a.lower()
  try:

    if abs(float(word(x).polarity_value()))>.3:
      return float(word(x).polarity_value())
    return 0
  except:
    return 0
