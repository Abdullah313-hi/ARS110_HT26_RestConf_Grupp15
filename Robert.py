import requests

headers = {
    "Accept": "application/yang-data+json",
    "Authorization": "Basic YWRtaW46TmV0d29yayEzMzc="
}

fel = 0

url1 = "https://11.11.11.1/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F0"

response1 = requests.get(url1, headers=headers, verify=False)

data1 = response1.json()

ip1 = data1["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"][0]["ip"]

if ip1 == "192.168.42.65":
    print("Overby G0/0/0 RÄTT")
else:
    print("Overby G0/0/0 FEL")
    fel += 1

url2 = "https://11.11.11.1/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F1"

response2 = requests.get(url2, headers=headers, verify=False)

data2 = response2.json()

ip2 = data2["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"][0]["ip"]

if ip2 == "192.168.42.1":
    print("Overby G0/0/1 RÄTT")
else:
    print("Overby G0/0/1 FEL")
    fel += 1

url3 = "https://11.11.11.2/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F0"

response3 = requests.get(url3, headers=headers, verify=False)

data3 = response3.json()

ip3 = data3["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"][0]["ip"]

if ip3 == "192.168.42.66":
    print("Trestad G0/0/0 RÄTT")
else:
    print("Trestad G0/0/0 FEL")
    fel += 1

url4 = "https://11.11.11.2/restconf/data/Cisco-IOS-XE-native:native/interface/Serial=0%2F1%2F1"

response4 = requests.get(url4, headers=headers, verify=False)

data4 = response4.json()

ip4 = data4["Cisco-IOS-XE-native:Serial"]["ip"]["address"]["primary"]["address"]

if ip4 == "192.168.42.69":
    print("Trestad Serial RÄTT")
else:
    print("Trestad Serial FEL")
    fel += 1

url5 = "https://11.11.11.3/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F1"

response5 = requests.get(url5, headers=headers, verify=False)

data5 = response5.json()

ip5 = data5["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"][0]["ip"]

if ip5 == "192.168.11.1":
    print("Torp G0/0/1 RÄTT")
else:
    print("Torp G0/0/1 FEL")
    fel += 1

url6 = "https://11.11.11.3/restconf/data/Cisco-IOS-XE-native:native/interface/Serial=0%2F1%2F1"

response6 = requests.get(url6, headers=headers, verify=False)

data6 = response6.json()

ip6 = data6["Cisco-IOS-XE-native:Serial"]["ip"]["address"]["primary"]["address"]

if ip6 == "192.168.42.70":
    print("Torp Serial RÄTT")
else:
    print("Torp Serial FEL")
    fel += 1

url7 = "https://11.11.11.1/restconf/data/Cisco-IOS-XE-native:native/router"

response7 = requests.get(url7, headers=headers, verify=False)

data7 = response7.json()

ospf1 = data7["Cisco-IOS-XE-native:router"]["Cisco-IOS-XE-ospf:router-ospf"]["ospf"]["process-id"][0]

if ospf1["router-id"] == "1.1.1.1":
    print("Overby OSPF RÄTT")
else:
    print("Overby OSPF FEL")
    fel += 1

url8 = "https://11.11.11.2/restconf/data/Cisco-IOS-XE-native:native/router"

response8 = requests.get(url8, headers=headers, verify=False)

data8 = response8.json()

ospf2 = data8["Cisco-IOS-XE-native:router"]["Cisco-IOS-XE-ospf:router-ospf"]["ospf"]["process-id"][0]

if ospf2["router-id"] == "2.2.2.2":
    print("Trestad OSPF RÄTT")
else:
    print("Trestad OSPF FEL")
    fel += 1

url9 = "https://11.11.11.2/restconf/data/ietf-routing:routing"

response9 = requests.get(url9, headers=headers, verify=False)

data9 = str(response9.json())

if "0.0.0.0/0" in data9 and "192.168.42.70" in data9:
    print("Trestad default route RÄTT")
else:
    print("Trestad default route FEL")
    fel += 1

url10 = "https://11.11.11.3/restconf/data/ietf-routing:routing"

response10 = requests.get(url10, headers=headers, verify=False)

data10 = str(response10.json())

if "192.168.42.0/26" in data10 and "192.168.42.69" in data10:
    print("Torp route 1 RÄTT")
else:
    print("Torp route 1 FEL")
    fel += 1

if "192.168.42.64/30" in data10 and "192.168.42.69" in data10:
    print("Torp route 2 RÄTT")
else:
    print("Torp route 2 FEL")
    fel += 1

url11 = "https://11.11.11.3/restconf/data/Cisco-IOS-XE-native:native/ip/access-list"

response11 = requests.get(url11, headers=headers, verify=False)

data11 = str(response11.json())

if "192.168.42.2" in data11 and "telnet" in data11:
    print("ACL RÄTT")
else:
    print("ACL FEL")
    fel += 1

if fel == 0:
    print("GODKÄND")
else:
    print("UNDERKÄND")
