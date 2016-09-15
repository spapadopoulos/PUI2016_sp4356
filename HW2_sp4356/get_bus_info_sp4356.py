import json
import urllib as ulr
import sys
import csv

key = sys.argv[1]
name = sys.argv[2]
output_file = sys.argv[3]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + name
response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

bus_json_path = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
bus_name = bus_json_path[0]['MonitoredVehicleJourney']['PublishedLineName']

with open(output_file,'wb') as csvfile: 
    bus_writer = csv.writer(csvfile)
    bus_writer.writerow(['Latitude', 'Longitude', 'Stop Name', 'Stop Status'])

    count = 0

    for i in bus_json_path:
        lat = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        long = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        count +=1

        if i['MonitoredVehicleJourney']['OnwardCalls'] == {}:
            stop = 'N/A'
            status = 'N/A'
        else:
            stop = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
            status = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
            count += 1
            bus_writer.writerow([lat, long, stop, status])

        print lat, long, stop, status

