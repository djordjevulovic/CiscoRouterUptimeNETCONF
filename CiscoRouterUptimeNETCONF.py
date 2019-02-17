from lxml import etree
from ncclient import manager
from io import BytesIO
import dateutil.parser
import sys
import datetime

def NETCONF_IOS_XE_get_uptime(router,port,username,password):

    filter = """
    <filter>
       <device-hardware-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-device-hardware-oper">
       </device-hardware-data>
    </filter>
    """

    try:
        m = manager.connect(host=router, port=port, username=username, password=password, hostkey_verify=False)

        xml_response_string = m.get(filter=filter).data_xml

    except Exception as e:
        print ("Could not read config for router {}: error '{}'".format(router,e))
        return None

    current_time = None
    boot_time = None

    for action, elem in etree.iterparse(BytesIO(bytes(xml_response_string, 'utf-8'))):
        if elem.tag == '{http://cisco.com/ns/yang/Cisco-IOS-XE-device-hardware-oper}current-time':
            current_time = dateutil.parser.parse(elem.text).timestamp()
        elif elem.tag == '{http://cisco.com/ns/yang/Cisco-IOS-XE-device-hardware-oper}boot-time':
            boot_time = dateutil.parser.parse(elem.text).timestamp()

    if current_time == None or boot_time == None:
        print ("Could not read uptime objects for router {}".format(router))
        return None

    return current_time - boot_time

print ("CiscoRouterUptimeNETCONF by Djordje Vulovic (dvulovic@cisco.com)")
print ("----------------------------------------------------------------")

if len(sys.argv) != 2:
    print ("Usage: CiscoRouterUptimeNETCONF <file>")
    print ("File consists of lines <mgmt ip>,<NETCONF port>,<username>,<password>")
    exit (code=0)

try:

    with open (sys.argv[1], "r") as myfile:

        for line in myfile:

            fields=line.rstrip().split(',')

            if len(fields) == 4:
                uptime = NETCONF_IOS_XE_get_uptime(fields[0],fields[1],fields[2],fields[3])
                if uptime:
                    print ("Router {} has uptime of {} seconds ({})".format(fields[0],uptime,str(datetime.timedelta(seconds=uptime))))
            else:
                print ("Cannot parse line '{}', skipping".format (line))
except IOError as e:
    print ("I/O error({0}): {1}".format(e.errno, e.strerror))


