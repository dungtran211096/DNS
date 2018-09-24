import ipaddress
import readfile
from hash import CuckooHash

H = CuckooHash(2000)

import timeit


def insert_to_hash():
    lists = ReadFile("/media/dung/Dung Tran/GSLB/geoip_data.dat").read_file()
    for i in lists:
        H[i[0]] = i[1]

class IpLookUp(object):
    def __init__(self, address):
        self.address = address

    def is_ip_valid(self):
        """
        If address is a valid IP network, return it as an ipaddress object,
        otherwise, return None
        """

        try:
            return ipaddress.ip_interface(self.address)
        except ValueError:
            return None

    def distance(self, ip1):
        list = []
        ip1 = self.is_ip_valid()
        for i in H.keys():
            x = abs(int(ip1) - int(ipaddress.ip_interface(i)))
            list.append(x)
        return list

    def ip_range(self):
        """
        From list keys in hash table return finding value-key pair
        :param ip_addr : ip looks up
        :return:
        """
        insert_to_hash()
        ip_addr = self.is_ip_valid()
        for i in H.keys():
            if ip_addr in ipaddress.ip_network(i, False):
                return i, H[i]
                pass
            else:
                m = min(self.distance(ip_addr))
                index = self.distance(ip_addr).index(m)
                return H[H.keys()[index]], H.keys()[index]
