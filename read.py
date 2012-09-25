import anydbm
import pickle


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
db = anydbm.open("bikes.db", 'r')

sortedKeys = db.keys()
sortedKeys.sort()
deltas = {}
oldTime = None;
for time in sortedKeys[0:60:1]:
  if oldTime != None:
    data1 = pickle.loads(db[time])
    data2 = pickle.loads(db[oldTime])
    deltas[time] = dataDiff(data1, data2 )
  oldTime = time;
#print deltas

picked_up= 0
dropped_off = 0
for key in deltas.keys():
  stations = deltas[key].keys()
  for station in stations:
    
    bikes = deltas[key][station]
    print bikes
    if bikes > 0:
      picked_up+= int(bikes)
    else:
      dropped_off -= int(bikes)
print picked_up
print dropped_off
print int(sortedKeys[60]) - int(sortedKeys[0])
