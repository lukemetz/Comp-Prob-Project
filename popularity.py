import anydbm
import pickle
import math
import station_names

def dataDiff(data1, data2):
  bikeDelta = {}
  for key in data1.keys():
    if(key not in data1 or key not in data2):
      print "Oddness with", key
      continue
    delta = int(data1[key]["bikes"]) - int(data2[key]["bikes"])
    if (delta):
      bikeDelta[key] = delta;
  return bikeDelta

def popularStation(popular):
  maxv= 0;
  index = None
  for i in popular:
    if popular[i] > maxv:
      maxv = popular[i]
      index = i;
  return index

def main():
  db = anydbm.open("bikes.db", 'r')
  sortedKeys = db.keys()
  sortedKeys.sort()
  deltas = {}
  oldTime = None;
  for time in sortedKeys[0:60*24:1]:
    if oldTime != None:
      data1 = pickle.loads(db[time])
      data2 = pickle.loads(db[oldTime])
      deltas[time] = dataDiff(data1, data2 )
    oldTime = time;
  print deltas
 
  popularity = {}
  for key in deltas.keys():
    stations = deltas[key].keys()
    for station in stations:    
      if station not in popularity:
        popularity[station] = 0
      popularity[station] += abs(int(deltas[key][station]));
  
  for i in range(5):
    s1 = popularStation(popularity);
    print station_names.get_name(s1), popularity[s1];
    popularity[s1] = 0

if __name__=="__main__":
  main()
