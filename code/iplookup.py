import ipaddress
from Dung_Handlesubnet.hash import CuckooHash
from Dung_Handlesubnet.readfile import ReadFile

H = CuckooHash(200)

class IpLookUp(object):

    def __init__(self, address):
        self.address = address

    def is_ip_valid(self):
        """
        If address is a valid IP network, return it as an ipaddress object,
        otherwise, return None
        """

        try:
            return ipaddress.ip_address(self.address)
        except ValueError:
            return None

    def ip_range(self):
        """
        check ip in file, return if ip belong to the closest ip network
        :param list: list of ip network in file
        :return: data center

        """

        list = ReadFile().read_file()
        ip_addr = self.is_ip_valid()
        for add in list:
            H[add[0]] = add[1]
            net = ipaddress.ip_network(add[0])

            if ip_addr in net:
                return H[add[0]]




ip = "125.212.128.1"
#
print(IpLookUp(ip).ip_range())

