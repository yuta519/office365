import urllib.request
import json
import make_random_uuid
import sys


def get_o365_data():
	uuid = make_random_uuid.create_uuid4()
	# For the latest version of the Office 365 URLs and IP address ranges
	url       = 'https://endpoints.office.com/endpoints/worldwide?clientrequestid='+str(uuid)
	request   = urllib.request.Request(url)
	with urllib.request.urlopen(request) as response:
		if response.getcode() == 200:		
			response_body = response.read().decode("utf-8")
			result_json   = json.loads(response_body)
		else:
			sys.exit()
	return result_json

def main():
	o365_data = get_o365_data()
	for data in o365_data:
		service_name = data['serviceAreaDisplayName'] if 'serviceAreaDisplayName' in data else 'No Service Name'
		urls         = data['urls'] if 'urls' in data else []
		tcp_ports    = data['tcpPorts'] if 'tcpPorts' in  data else []
		ips          = data['ips'] if 'ips' in data else []
		print('==============================================')
		print(service_name)
		print(urls)
		print(tcp_ports)
		print(ips)
		print('==============================================')

#############################
# execution
#############################
if __name__ == "__main__":
    main()