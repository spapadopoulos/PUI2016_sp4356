import json
import urllib as ulr
import sys

key = sys.argv[1]
name = sys.argv[2]

#key = raw_input('Enter your key: ')
#name = raw_input('Enter bus name: ')



url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + name
response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

#type(data)
#data.keys()
#data['Siri'].keys()
#data['Siri']['ServiceDelivery'].keys()

bus_json_path = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
bus_name = bus_json_path[0]['MonitoredVehicleJourney']['PublishedLineName']
print 'Bus line: ', bus_name

count = 0
for i in bus_json_path:
    count +=1
print 'Number of active buses: ', count

counter = 0
for i in bus_json_path:
    lat = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    long = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print 'Bus', counter, 'is at latitude', lat, 'and logitude', long
    counter +=1

