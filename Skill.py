import requests

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
    "Authorization": "Basic YWRtaW46TmV0d29yayEzMzc="
}


url1 = "https://11.11.11.1/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F0"

payload1 = {
    "ietf-interfaces:interface": {
        "name": "GigabitEthernet0/0/0",
        "description": "till Trestad",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "192.168.42.65",
                    "netmask": "255.255.255.252"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

response1 = requests.put(url1, headers=headers, json=payload1, verify=False)

print(response1.text)


url2 = "https://11.11.11.1/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F1"

payload2 = {
    "ietf-interfaces:interface": {
        "name": "GigabitEthernet0/0/1",
        "description": "till HostBk",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "192.168.42.1",
                    "netmask": "255.255.255.192"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

response2 = requests.put(url2, headers=headers, json=payload2, verify=False)

print(response2.text)

url3 = "https://11.11.11.2/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F0"

payload3 = {
    "ietf-interfaces:interface": {
        "name": "GigabitEthernet0/0/0",
        "description": "till Overby",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "192.168.42.66",
                    "netmask": "255.255.255.252"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

response3 = requests.put(url3, headers=headers, json=payload3, verify=False)

print(response3.text)

url4 = "https://11.11.11.2/restconf/data/Cisco-IOS-XE-native:native/interface/Serial=0%2F1%2F1"

payload4 = {
    "Cisco-IOS-XE-native:Serial": {
        "name": "0/1/1",
        "description": "till Torp",
        "ip": {
            "address": {
                "primary": {
                    "address": "192.168.42.69",
                    "mask": "255.255.255.252"
                }
            }
        }
    }
}

response4 = requests.put(url4, headers=headers, json=payload4, verify=False)

print(response4.text)

url5 = "https://11.11.11.3/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F1"

payload5 = {
    "ietf-interfaces:interface": {
        "name": "GigabitEthernet0/0/1",
        "description": "till HostMc",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "192.168.11.1",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

response5 = requests.put(url5, headers=headers, json=payload5, verify=False)

print(response5.text)


url6 = "https://11.11.11.3/restconf/data/Cisco-IOS-XE-native:native/interface/Serial=0%2F1%2F1"

payload6 = {
    "Cisco-IOS-XE-native:Serial": {
        "name": "0/1/1",
        "description": "till TRESTAD",
        "ip": {
            "address": {
                "primary": {
                    "address": "192.168.42.70",
                    "mask": "255.255.255.252"
                }
            }
        }
    }
}

response6 = requests.put(url6, headers=headers, json=payload6, verify=False)

print(response6.text)

url7 = "https://11.11.11.3/restconf/data/Cisco-IOS-XE-native:native/ip/access-list"

payload7 = {
    "Cisco-IOS-XE-native:access-list": {
        "Cisco-IOS-XE-acl:extended": [
            {
                "name": "BLOCK-TELNET",
                "access-list-seq-rule": [
                    {
                        "sequence": "10",
                        "ace-rule": {
                            "action": "deny",
                            "protocol": "tcp",
                            "ipv4-address": "192.168.42.2",
                            "mask": "0.0.0.0",
                            "dst-any": [None],
                            "dst-eq": "telnet"
                        }
                    },
                    {
                        "sequence": "20",
                        "ace-rule": {
                            "action": "permit",
                            "protocol": "ip",
                            "any": [None],
                            "dst-any": [None]
                        }
                    }
                ]
            }
        ]
    }
}

response7 = requests.patch(url7, headers=headers, json=payload7, verify=False)

print(response7.text)

url8 = "https://11.11.11.1/restconf/data/Cisco-IOS-XE-native:native/router"

payload8 = {
    "Cisco-IOS-XE-native:router": {
        "Cisco-IOS-XE-ospf:router-ospf": {
            "ospf": {
                "process-id": [
                    {
                        "id": 1,
                        "router-id": "1.1.1.1",
                        "network": [
                            {
                                "ip": "192.168.42.0",
                                "wildcard": "0.0.0.63",
                                "area": 0
                            },
                            {
                                "ip": "192.168.42.64",
                                "wildcard": "0.0.0.3",
                                "area": 0
                            }
                        ],
                        "passive-interface": {
                            "interface": [
                                "GigabitEthernet0/0/1"
                            ]
                        }
                    }
                ]
            }
        }
    }
}

response8 = requests.patch(url8, headers=headers, json=payload8, verify=False)

print(response8.text)

url9 = "https://11.11.11.2/restconf/data/Cisco-IOS-XE-native:native/router"

payload9 = {
    "Cisco-IOS-XE-native:router": {
        "Cisco-IOS-XE-ospf:router-ospf": {
            "ospf": {
                "process-id": [
                    {
                        "id": 1,
                        "router-id": "2.2.2.2",
                        "default-information": {
                        "originate":{}
                        },
                        "network": [
                            {
                                "ip": "192.168.42.64",
                                "wildcard": "0.0.0.3",
                                "area": 0
                            }
                        ]
                    }
                ]
            }
        }
    }
}

response9 = requests.patch(url9, headers=headers, json=payload9, verify=False)

print(response9.text)



url10 = "https://11.11.11.2/restconf/data/ietf-routing:routing"

payload10 = {
    "ietf-routing:routing": {
        "routing-instance": [
            {
                "name": "default",
                "routing-protocols": {
                    "routing-protocol": [
                        {
                            "type": "ietf-routing:static",
                            "name": "1",
                            "static-routes": {
                                "ietf-ipv4-unicast-routing:ipv4": {
                                    "route": [
                                        {
                                            "destination-prefix": "0.0.0.0/0",
                                            "next-hop": {
                                                "next-hop-address": "192.168.42.70"
                                            }
                                        }
                                    ]
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

response10 = requests.patch(url10, headers=headers, json=payload10, verify=False)

print(response10.text)



url11 = "https://11.11.11.3/restconf/data/ietf-routing:routing"

payload11 = {
    "ietf-routing:routing": {
        "routing-instance": [
            {
                "name": "default",
                "routing-protocols": {
                    "routing-protocol": [
                        {
                            "type": "ietf-routing:static",
                            "name": "1",
                            "static-routes": {
                                "ietf-ipv4-unicast-routing:ipv4": {
                                    "route": [
                                        {
                                            "destination-prefix": "192.168.42.64/30",
                                            "next-hop": {
                                                "next-hop-address": "192.168.42.69"
                                            }
                                        },
                                        {
                                            "destination-prefix": "192.168.42.0/26",
                                            "next-hop": {
                                                "next-hop-address": "192.168.42.69"
                                            }
                                        }
                                    ]
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

response11 = requests.patch(url11, headers=headers, json=payload11, verify=False)

print(response11.text)

url12 = "https://11.11.11.1/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=0%2F0%2F0"

payload12 = {
    "Cisco-IOS-XE-native:GigabitEthernet": {
        "name": "0/0/0",
        "ip": {
            "Cisco-IOS-XE-ospf:router-ospf": {
                "ospf": {
                    "authentication": {
                        "clear-text": [None]
                    },
                    "authentication-key": {
                        "auth-type": 0,
                        "auth-key": "cisco"
                    }
                }
            }
        }
    }
}

response12 = requests.patch(url12, headers=headers, json=payload12, verify=False)

print(response12.text)


url13 = "https://11.11.11.2/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=0%2F0%2F0"

payload13 = {
    "Cisco-IOS-XE-native:GigabitEthernet": {
        "name": "0/0/0",
        "ip": {
            "Cisco-IOS-XE-ospf:router-ospf": {
                "ospf": {
                    "authentication": {
                        "clear-text": [None]
                    },
                    "authentication-key": {
                        "auth-type": 0,
                        "auth-key": "cisco"
                    }
                }
            }
        }
    }
}

response13 = requests.patch(url13, headers=headers, json=payload13, verify=False)

print(response13.text)

url14 = "https://11.11.11.1/restconf/data/Cisco-IOS-XE-native:native/enable"

payload14 = {
    "Cisco-IOS-XE-native:enable": {
        "secret": {
            "type": "0",
            "secret": "Network!337"
        }
    }
}

response14 = requests.patch(url14, headers=headers, json=payload14, verify=False)

print(response14.text)

url15 = "https://11.11.11.1/restconf/data/Cisco-IOS-XE-native:native/line"

payload15 = {
    "Cisco-IOS-XE-native:line": {
        "console": [
            {
                "first": "0",
                "login": {
                    "local": [None]
                }
            }
        ]
    }
}

response15 = requests.patch(url15, headers=headers, json=payload15, verify=False)

print(response15.text)

url16 = "https://11.11.11.2/restconf/data/Cisco-IOS-XE-native:native/enable"

payload16 = {
    "Cisco-IOS-XE-native:enable": {
        "secret": {
            "type": "0",
            "secret": "Network!337"
        }
    }
}

response16 = requests.patch(url16, headers=headers, json=payload16,verify=False)

print(response16.text)

url17 = "https://11.11.11.2/restconf/data/Cisco-IOS-XE-native:native/line"

payload17 = {
    "Cisco-IOS-XE-native:line": {
        "console": [
            {
                "first": "0",
                "login": {
                    "local": [None]
                }
            }
        ]
    }
}

response17 = requests.patch(url17, headers=headers, json=payload17, verify=False)

print(response17.text)

url18 = "https://11.11.11.3/restconf/data/Cisco-IOS-XE-native:native/enable"

payload18 = {
    "Cisco-IOS-XE-native:enable": {
        "secret": {
            "type": "0",
            "secret": "Network!337"
        }
    }
}

response18 = requests.patch(url18, headers=headers, json=payload18, verify=False)

print(response18.text)

url19 = "https://11.11.11.3/restconf/data/Cisco-IOS-XE-native:native/line"

payload19 = {
    "Cisco-IOS-XE-native:line": {
        "console": [
            {
                "first": "0",
                "login": {
                    "local": [None]
                }
            }
        ]
    }
}

response19 = requests.patch(url19, headers=headers, json=payload19, verify=False)

print(response19.text)

url20 = "https://11.11.11.3/restconf/data/Cisco-IOS-XE-native:native/line"

payload20 = {
    "Cisco-IOS-XE-native:line": {
        "vty": [
            {
                "first": 0,
                "last": 4,
                "access-class": {
                    "access-list": [
                        {
                            "direction": "in",
                            "access-list": "BLOCK-TELNET"
                        }
                    ]
                }
            }
        ]
    }
}

response20 = requests.patch(url20, headers=headers, json=payload20, verify=False)

print(response20.text)
