import ipaddress
from readfile import ReadFile
from hash import CuckooHash

H = CuckooHash(20000)


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

    def insert_to_hash(self):
        lists = ReadFile("/media/dung/Dung Tran/GSLB/geoip_data.dat").read_file()

        for i in lists:
            H[i[0]] = i[1]

    def ip_range(self):
        """
        From list keys in hash table return finding value-key pair
        :return:
        """

        self.insert_to_hash()
        ip_addr = self.is_ip_valid()

        for i in H.keys():
            # if ip_addr in ipaddress.ip_network(i):
            #     return i, H[i]
            if i == "203.119.8.0/22":
                return H[i]

ip = '203.119.8.1/24'


print(IpLookUp(ip).ip_range())
# print(H.keys())
