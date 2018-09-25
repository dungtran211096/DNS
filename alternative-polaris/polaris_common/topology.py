import ipaddress
from .hash import CuckooHash

H = CuckooHash(20000)


def insert_to_hash(topology_map):
    for i in topology_map:
        H[i[0]] = i[1]


def is_ip_valid(address):
    """
    If address is a valid IP network, return it as an ipaddress object,
    otherwise, return None
    """

    try:
        return ipaddress.ip_interface(address)
    except ValueError:
        return None

def distance(ip1):
        list = []
        
        for i in H.keys():
            x = abs(int(is_ip_valid(ip1)) - int(is_ip_valid(i)))
            list.append(x)
        return list

def ip_range(ip_addr, topology_map):
    """
    From list keys in hash table return finding value-key pair
    :param ip_addr : ip looks up
    :return:
    """
    
    insert_to_hash(topology_map)
   
    for i in H.keys():
        if is_ip_valid(ip_addr) in ipaddress.ip_network(i, False):
            return H[i]
        else:
            m = min(distance(is_ip_valid(ip_addr)))
            index = distance(is_ip_valid(ip_addr)).index(m)
            return H[H.keys()[index]]
