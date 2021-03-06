#!/usr/bin/python
import os, sys
import socket
import struct
# import binascii
import subprocess
import re
import fcntl
import time
import signal, commands
# from threading import Thread
# import threading
from multiprocessing import Process
from socket import gethostname
#There is a really good chance this cannot be loaded on AIX and Solaris 
#But we are not using raw sockets
try:
    import ctypes
    class ifreq(ctypes.Structure):
        _fields_ = [("ifr_ifrn", ctypes.c_char * 16),
                    ("ifr_flags", ctypes.c_short)]
except (ImportError, NameError) as e:
    print "Meh"
#Taken from the C Header Files
ETH_P_ALL = 0x0003
IFF_PROMISC = 0x100
SIOCGIFFLAGS = 0x8913
SIOCSIFFLAGS = 0x8914


def get_networklist(osnameonly=None):
    """Get Operating system type so that we can choose the method for getting the LLDP data"""
    osname = subprocess.Popen("uname -s", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].strip()

    def get_linux_interfacenames():
        #interface_list = os.listdir("/sys/class/net/eth*")
        interface_list = []
        for interface in os.listdir("/sys/class/net"):
                if 'eth' in interface:
                        interface_list.append(interface)
        return interface_list

    def get_aix_interfacenames():
        output = subprocess.Popen("lsdev -l en\*", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        interface_list = re.findall(r"^(en\d*)\s+Available.*$", str(output), re.M)
        return interface_list

    def get_solaris_interfacenames():
        osrelease = subprocess.Popen("uname -r", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].strip()
        if osrelease == "5.10":
            output = subprocess.Popen("dladm show-dev -p", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
            interface_list = [line.split()[0] for line in output.rstrip().split('\n')]
        elif osrelease == "5.11":
            output = subprocess.Popen("dladm show-phys -p -o link", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
            interface_list = [line.split()[0] for line in output.rstrip().split('\n')]
        else:
            print "something went wrong here..."
        return interface_list


    if osnameonly is None:
        return {
            'Linux': get_linux_interfacenames,
            'AIX': get_aix_interfacenames,
            'SunOS': get_solaris_interfacenames,
        }[osname]()
    else:
        return osname
    # python case switch http://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python

# Enable promiscuous mode from http://stackoverflow.com/a/6072625
def promiscuous_mode(interface, sock, enable=False):
    ifr = ifreq()
    ifr.ifr_ifrn = interface
    fcntl.ioctl(sock.fileno(), SIOCGIFFLAGS, ifr)
    if enable:
        ifr.ifr_flags |= IFF_PROMISC
    else:
        ifr.ifr_flags &= ~IFF_PROMISC
    fcntl.ioctl(sock.fileno(), SIOCSIFFLAGS, ifr)

def evaluate_aix(interface, max_capture_time):
# figure out a way to track subprocess calls and
    # signal.signal(signal.SIGINT, exit_handler_aix)
    # signal.signal(signal.SIGALRM, exit_handler_aix)
    # signal.alarm(max_capture_time)
    # tcpdump -i en8 -s 1500 -c1 -w output_tcpdump.alex ether proto 0x88cc
    process = subprocess.Popen(['tcpdump', '-i', interface, '-s', '1500', '-c1', '-w', '/tmp/'+interface+'outfile', 'ether', 'proto', '0x88cc'])
    time.sleep(62)
    if process.poll() is None:
        process.terminate()
    time.sleep(3)
    if process.poll() is None:
        process.kill()

    with open("/tmp/"+interface+"outfile") as f:
        f.seek(40)
        data = f.read()
        data = data[14:]
        VLAN_ID, Switch_Name, Port_Description, Ethernet_Port_Id = parse_lldp_packet_frames(data)
    path = "/opt/sysdoc/lldp_data/"
    if not os.path.exists("/opt/sysdoc/lldp_data"):
        os.makedirs(path, mode=0755)

    interfacestring = interface[:2] + 't' + interface[2:]
    with open(path+interfacestring, 'w') as f: #TODO write mode
        context = {
            "vlanid": VLAN_ID,
            "ethernetportid": Ethernet_Port_Id,
            "portdescription": Port_Description,
            "switchname": Switch_Name,
            }
        template = """VLANID={vlanid}
ETHERNETPORTID={ethernetportid}
PORTDESCRIPTION={portdescription}
SWITCHNAME={switchname}"""

        f.write(template.format(**context))

def evaluate_solaris(interface, max_capture_time):
#snoop -o christian_ist_eine_gurke.out -s 1500 -c 1 -x 0 -d e1000g3 ethertype 0x88cc
    process = subprocess.Popen(['snoop', '-o', '/tmp/'+interface+'outfile', '-s', '1500', '-c', '1', '-x', '0', '-d', interface, 'ethertype', '0x88cc'])
    time.sleep(62)
    if process.poll() is None:
        process.terminate()
    time.sleep(3)
    if process.poll() is None:
        process.kill()

    with open("/tmp/"+interface+"outfile") as f:
        f.seek(40)
        data = f.read()
        data = data[14:]
        VLAN_ID, Switch_Name, Port_Description, Ethernet_Port_Id = parse_lldp_packet_frames(data)
    path = "/opt/sysdoc/lldp_data/"
    if not os.path.exists("/opt/sysdoc/lldp_data"):
        os.makedirs(path, mode=0755)

    with open(path+interface, 'w') as f: #TODO write mode
        context = {
            "vlanid": VLAN_ID,
            "ethernetportid": Ethernet_Port_Id,
            "portdescription": Port_Description,
            "switchname": Switch_Name,
            }
        template = """VLANID={vlanid}
ETHERNETPORTID={ethernetportid}
PORTDESCRIPTION={portdescription}
SWITCHNAME={switchname}"""

        f.write(template.format(**context))


def evaluate_linux(interface, max_capture_time):
    rawSocket = socket.socket(17, socket.SOCK_RAW, socket.htons(0x0003))
    rawSocket.bind((interface, ETH_P_ALL))
    #promiscuous mode below is True
    promiscuous_mode(interface, rawSocket, True)
    signal.signal(signal.SIGINT, exit_handler)
    signal.signal(signal.SIGALRM, exit_handler)
    signal.alarm(max_capture_time)
    while True:
        try:
            packet = rawSocket.recvfrom(65565)
            packet = packet[0]
            lldpPayload = packet[14:]
            ethernetHeaderTotal = packet[0:14]
            ethernetHeaderUnpacked = struct.unpack("!6s6s2s", ethernetHeaderTotal)
            ethernetHeaderProtocol = ethernetHeaderUnpacked[2]

            if ethernetHeaderProtocol != '\x88\xCC':
                continue

            VLAN_ID, Switch_Name, Port_Description, Ethernet_Port_Id = parse_lldp_packet_frames(lldpPayload)

            break
        except socket.error as msg:
            #print "Error occured with interface %s:\n%s" % (interface, msg)
                promiscuous_mode(interface, rawSocket, False)
    #get MAC address
    MAC=commands.getoutput("ifconfig " + interface + "|" + "grep " + interface).strip().split(' ')[-1]
    path = "/opt/sysdoc/lldp_data/"

    if not os.path.exists("/opt/sysdoc/lldp_data"):
        os.makedirs(path, mode=0755)
    #get the hostname of the server
    HOSTNAME=gethostname()
    with open(path+interface, 'w') as f: #TODO write mode
        context = {
            "hostname": HOSTNAME,
            "interface": interface,
            "MAC": MAC,
            "vlanid": VLAN_ID,
            "ethernetportid": Ethernet_Port_Id,
            "portdescription": Port_Description,
            "switchname": Switch_Name,
            }
        template = """HOSTNAME{hostname}
INTERFACE={interface}
MAC={MAC}
VLANID={vlanid}
ETHERNETPORTID={ethernetportid}
PORTDESCRIPTION={portdescription}
SWITCHNAME={switchname}
"""
        f.write(template.format(**context))
        print(HOSTNAME+';'+interface+';'+MAC+';'+Switch_Name+';'+Ethernet_Port_Id+';'+str(VLAN_ID))


def parse_lldp_packet_frames(lldpPayload):
    Switch_Name = None
    VLAN_ID = None
    Ethernet_Port_Id = None
    Port_Description = None

    while lldpPayload:
        tlv_header = struct.unpack("!H", lldpPayload[:2])[0]
        tlv_type = tlv_header >> 9
        tlv_len = (tlv_header & 0x01ff)
        lldpDU = lldpPayload[2:tlv_len + 2]
        if tlv_type == 127:
            tlv_oui = lldpDU[:3]
            tlv_subtype = lldpDU[3:4]
            tlv_datafield = lldpDU[4:tlv_len]
            if tlv_oui == "\x00\x80\xC2" and tlv_subtype == "\x01":
                VLAN_ID = struct.unpack("!H", tlv_datafield)[0]

        elif tlv_type == 0:
            #print "TLV Type is ZERO, Breaking the while loop"
            break
        else:
            tlv_subtype = struct.unpack("!B", lldpDU[0:1]) if tlv_type is 2 else ""
            startbyte = 1 if tlv_type is 2 else 0
            tlv_datafield = lldpDU[startbyte:tlv_len]


        if tlv_type == 4:
            Port_Description = tlv_datafield
        elif tlv_type == 2:
            Ethernet_Port_Id = tlv_datafield
        elif tlv_type == 5:
            Switch_Name = tlv_datafield
        else:
            pass

        lldpPayload = lldpPayload[2 + tlv_len:]


    return VLAN_ID, Switch_Name, Port_Description, Ethernet_Port_Id


def main():
    max_capture_time = 70
    networkname_list = get_networklist()
    os_name = get_networklist(osnameonly=True)
    evaluate_Function = {
        'Linux': evaluate_linux,
        'AIX': evaluate_aix,
        'SunOS': evaluate_solaris,
    }

    processes = [Process(target=evaluate_Function[os_name], args=(interface, max_capture_time)) for interface in networkname_list]
    for x in processes:
        x.start()

def exit_handler(signum, frame):
    """ Exit signal handler """

    rawSocket = frame.f_locals['rawSocket']
    interface = frame.f_locals['interface']
    promiscuous_mode(interface, rawSocket, False)
    #print("Abort, %s exit promiscuous mode." % interface)

    sys.exit(1)

def exit_handler_aix(signum, frame):
    #print "Aborting AIX"
    sys.exit(0)



if __name__ == '__main__':
    main()