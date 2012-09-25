import anydbm
import pickle

import operator

def checkForLowStation(data, amount, cumulative):
  for stationID in data:
    station = data[stationID]
    if stationID not in cumulative:
      cumulative[stationID] = {"bikes_warnings":0, "empty_warnings":0}
    if amount >= int(station["bikes"]):
      cumulative[stationID]["bikes_warnings"] += 1
    if amount >= int(station["empty_docks"]):
      cumulative[stationID]["empty_warnings"] += 1
  return cumulative

def printWarnings(cumulative):
  bikesWarnings = [0 for _ in range(300)] 
  emptyWarnings = [0 for _ in range(300)] 
  for station in cumulative:
    bikesWarnings[int(station)] = cumulative[station]["bikes_warnings"]
    emptyWarnings[int(station)] = cumulative[station]["empty_warnings"]
  
  oldBikeWarnings = bikesWarnings[:];
  oldEmpyWarnings = emptyWarnings[:];

  bikesWarnings.sort(reverse=True)
  emptyWarnings.sort(reverse=True)
  
  print oldBikeWarnings.index(bikesWarnings[0]), bikesWarnings[0]
  print emptyWarnings.index(emptyWarnings[0]), emptyWarnings[0]#[0:5]
  print "second worst"
  print oldBikeWarnings.index(bikesWarnings[1]), bikesWarnings[1]
  print emptyWarnings.index(emptyWarnings[1]), emptyWarnings[1]#[0:5]

def main():
  db = anydbm.open("bikes.db", 'r')
  sortedKeys = db.keys()
  sortedKeys.sort()
  oldTime = None;
  cumulative = {}
  for time in sortedKeys[0:len(sortedKeys):60]:
    data = pickle.loads(db[time])
    cumulative = checkForLowStation(data, 2, cumulative)
  printWarnings(cumulative)

if __name__=="__main__":
  main()
