#### Description

Get uptime for Cisco IOS XE devices using NETCONF. Uses 
Cisco-IOS-XE-device-hardware-oper YANG module which is supported 
on IOS XE 16.8.1 and later. 

#### Usage

`./CiscoRouterUptimeNETCONF.py <input_file>`

Where input file is a text file consisting from the lines 
in the following format:

`<router IP address><NETCONF port><username><password>`

Example:

`10.1.1.1,830,myuser,mypass`  
`10.1.1.2,830,myuser,mypass`

#### Reqquirments

Package requires Python 3.3 and later.

#### Installation

Package is installed by running:

`python setup.py install`
   
Make sure that before running the script you have installed the 
following packages:
- libxml2-dev
- libxslt-dev
- python3-dev

Example: 
 
`sudo apt-get install libxml2-dev libxslt-dev python3-dev`


