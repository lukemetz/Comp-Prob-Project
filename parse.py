# Write the files to a db

import xml.etree.ElementTree as elementTree
import anydbm
import pickle
import glob
import os

def add_to_db(file_name, db):
  tree = elementTree.parse(file_name)
  stations = tree.getroot()
  last_update = stations.get("lastUpdate")

  stations_out = {}
  for station in stations:
    station_id = station.find('id').text
    station_bikes = station.find('nbBikes').text
    station_empty_docks = station.find('nbEmptyDocks').text
    station = {'bikes': station_bikes, 'empty_docks': station_empty_docks}
    stations_out[station_id] = station

  db[last_update] = pickle.dumps(stations_out)
def select_paths():
  paths = glob.glob("/home/luke/hubwayData/*.xml") 
  paths.sort()
  return paths[0:len(paths):1]

def main():

  db = anydbm.open("bikes.db", 'c')
  paths = select_paths()
  print("adding %d paths"%len(paths))
  count = 0
  for path in paths:
    count += 1
    print("Adding %d"%count)
    add_to_db(path, db);
    os.system("mv %s "%path + "/home/luke/hubwayData/parsed")
  db.close()

if __name__ == '__main__':
  main()
