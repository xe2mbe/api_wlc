# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:35:30 2020

@author: ss_ebueno
"""
#!/usr/bin/env python

from netmiko import ConnectHandler

netuser = "python"
netpass = "cisco123"
lifetime = 0
desc = "PythonAPI"
sendCommand = f"config netuser add {netuser} {netpass} wlan 4 userType guest lifetime {lifetime} description {desc}" 
print(sendCommand)

with ConnectHandler(ip = '192.168.252.2',
                        port = 22,
                        username = 'ebueno',
                        password = 'Tti0tGAXF*.',
                        device_type = 'cisco_wlc_ssh'
                    ) as ch: 

                        #print(ch.send_command("show ap summary"))
                        print(ch.send_command(sendCommand))