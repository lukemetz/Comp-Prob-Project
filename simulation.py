
import random

def doTest():
  num_stations = 86

  min_bikes = 15
  bikes_per_day = 3250
  chance_per_min = bikes_per_day/float(24*60)/num_stations
  print chance_per_min

  stations= [];
  emptyWarnings = []
  fullWarnings = []
  for i in range(num_stations):
    stations.append(min_bikes/2+i%2) 
    emptyWarnings.append(0)
    fullWarnings.append(0)

  timeRange = int(19.3*60*25)
  #timeRange = 60*25*3
  for i in range(timeRange):
    for j in range(num_stations):
      pickup = random.random();
      if pickup < chance_per_min:
        if stations[j] > 0:
          stations[j] -= 1

      dropoff = random.random();
      if dropoff  < chance_per_min:
        if stations[j] <  min_bikes:
          stations[j] += 1

      if stations[j] <= 1:
        emptyWarnings[j] += 1
      if stations[j] >= min_bikes-1:
        fullWarnings[j] += 1

  fullWarnings.sort(reverse=True)
  emptyWarnings.sort(reverse=True)
  print fullWarnings
  print emptyWarnings
  return (fullWarnings[0] > .322* timeRange, fullWarnings[0] > .319*timeRange, fullWarnings[0] > .30*timeRange)


p1 = 0
p2 = 0
p3 = 0
for i in range(1000):
  print i
  ret = doTest()
  print ret
  p1 += ret[0]
  p2 += ret[1]
  p3 += ret[2]
  print "on i", i, p1, p2, p3
print p1, p2
