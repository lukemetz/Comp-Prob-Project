import pickle
import anydbm
from matplotlib import pyplot as pt
import time
import Cdf 
import myplot

def getChance(data):
  return [int(data[station]["bikes"]) for station in data]

def main():
  db = anydbm.open("bikes.db", 'r')
  sortedKeys = db.keys()
  sortedKeys.sort()
  oldTime = None;
  cumulative = {}

  count = 0;
  utilization = [];
  times = [];
  count = 0;
  initTime = int(sortedKeys[0])
  for timeKey in sortedKeys[0:len(sortedKeys):1]:
    count += 1
    print float(count)/len(sortedKeys)
    data = pickle.loads(db[timeKey]);
    util = getChance(data)
    utilization.extend(util);
    
    times.append((int(timeKey)-initTime)/1000.0/60.0/60.0/24);
  fig = pt.figure()
  cdf = Cdf.MakeCdfFromList(utilization);
  #cdf.Normalize()
  # pt.plot(times,utilization);
  # pt.xlabel("Time (days)")
  # pt.ylabel("Empty Docks")
  # pt.title("Utilization over Time")
  # pt.savefig("utilization.png")
  
  myplot.Cdf(cdf)
  pt.axis([0, 20, 0, 1]);
  pt.xlabel("Bikes Free") 
  pt.ylabel("Probability")
  pt.title("Probability of Free Bike")
  pt.savefig("cdfChance.png")
  pt.show()

if __name__=="__main__":
  main()
