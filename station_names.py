import pickle
import anydbm
import glob
import xml.etree.ElementTree as elementTree
def get_name(stationID):
  stationID = str(stationID)
  db = anydbm.open("stations.db")
  if stationID in db.keys():
    station = pickle.loads(db[stationID])
    return station['name']
  
  return "not found"

def make_station_db():
  db = anydbm.open("stations.db", 'c')
  paths = glob.glob("/home/luke/hubwayData/parsed/*.xml")
  paths.sort()
  tree = elementTree.parse(paths[-1])
  stations = tree.getroot()
  for station in stations:
    station_id = station.find('id').text
    station_lat = station.find('lat').text
    station_long = station.find('long').text
    station_name = station.find('name').text
    
    station_dict = {'lat':station_lat, 'long':station_long, 'name':station_name}
    db[station_id] = pickle.dumps(station_dict)

if __name__=="__main__":
  make_station_db()
