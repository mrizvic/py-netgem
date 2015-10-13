# Netgem STB remote control over network

This is python class for manipulating with Netgem set-top-boxes over network using HTTP requests. Actions are triggered the same way as one would press buttons on physical remote control. Every button action can be triggered from physical remote control or via HTTP request.

# Usage

In order to do that you need to know LAN IP address of your Netgem STB. You can find it in diagnostics menu or by examining your DHCP server logs or by examining ARP table on your router and find device which mac address starts with 00:04:30. Im using ARP method since I know my box has been active recently.

```
lab$ arp -na
? (192.168.1.22) at 00:04:30:4e:fa:d3 [ether] on eth0
? (192.168.1.1) at 64:6e:ea:00:aa:ee [ether] on eth0
```

Example using python interpreter
```
lab$ python
Python 2.7.3 (default, Jun 22 2015, 19:33:41) 
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import netgem
>>> stbip='192.168.1.22'
>>> n=netgem.Netgem(ip=stbip)
>>> n.connect()
connecting...  success
>>> n.get_volume()
'<?xml version="1.0" encoding="utf-8"?>\n<response code="ok">96</response>'
>>> n.zap(239)
'<?xml version="1.0" encoding="utf-8"?>\n<response code="ok"/>'
>>> n.send_key('down')
'<?xml version="1.0" encoding="utf-8"?>\n<response code="ok"/>'
>>> n.send_key('down')
'<?xml version="1.0" encoding="utf-8"?>\n<response code="ok"/>'
>>> n.send_key('down')
'<?xml version="1.0" encoding="utf-8"?>\n<response code="ok"/>'
>>> n.send_key('down')
'<?xml version="1.0" encoding="utf-8"?>\n<response code="ok"/>'
>>> n.send_text('poletje v skoljki 2')
>>> 
```

In order to see short demo set environment variable then run `python netgem.py` and start enjoying hands-free STB manipulation.
```
lab$ export STB_IP=192.168.1.22
lab$ python netgem.py
connecting...  success
<?xml version="1.0" encoding="utf-8"?>
<response code="ok">96</response>
lab$ python zapchannels.py 
connecting...  success
zapping to channel 1
zapping to channel 2
zapping to channel 3
zapping to channel 4
zapping to channel 6
zapping to channel 7
zapping to channel 100
zapping to channel 102
zapping to channel 104
zapping to channel 106
zapping to channel 109
zapping to channel 110
zapping to channel 111
zapping to channel 201
zapping to channel 206
zapping to channel 208
zapping to channel 1
zapping to channel 2
zapping to channel 3
^CTraceback (most recent call last):
  File "zapchannels.py", line 22, in <module>
    main()
  File "zapchannels.py", line 19, in main
    time.sleep(5)
KeyboardInterrupt
```

# Documentation

Run `pydoc netgem` to see details.

# Installation

git clone https://github.com/mrizvic/py-netgem.git

# Prerequisites

This python class calls following imports
```
import urllib
import urllib2
import time
import zlib
import os
```
