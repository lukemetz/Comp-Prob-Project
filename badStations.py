import anydbm
import pickle
import station_names
import operator
import time

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
  
  bikesWarningsIndex = [i[0] for i in sorted(enumerate(bikesWarnings), reverse=True, key=lambda x:x[1])]
  emptyWarningsIndex = [i[0] for i in sorted(enumerate(emptyWarnings), reverse=True, key=lambda x:x[1])]
  for k in bikesWarningsIndex:
    print bikesWarnings[k],
  print "d"
  for i in range(4):
    indexBikes = bikesWarningsIndex[i]
    indexEmpty = emptyWarningsIndex[i]
     
    print "Waring on bikes", i, indexBikes, bikesWarnings[indexBikes], station_names.get_name(indexBikes)
    print "Warning on empty", i, indexEmpty, emptyWarnings[indexEmpty], station_names.get_name(indexEmpty)

def main():
  db = anydbm.open("bikes.db", 'r')
  sortedKeys = db.keys()
  sortedKeys.sort()
  oldTime = None;
  cumulative = {}

  print time.ctime(int(sortedKeys[0]))
  print time.ctime(int(sortedKeys[len(sortedKeys)-1]))
  count = 0;
  for timeKey in sortedKeys[0:len(sortedKeys):1]:
    count += 1
    print float(count)/len(sortedKeys)
    data = pickle.loads(db[timeKey])
    cumulative = checkForLowStation(data, 1, cumulative)
  printWarnings(cumulative)

if __name__=="__main__":
  main()
