import ipaddress
from Dung_Handlesubnet.hashing import CuckooMap
from Dung_Handlesubnet.vega_geoip_data import GEOIP_CIDRS


H = CuckooMap()

class IpLookUp():


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
        - Finding ip_range which include ip_input
        - fragment ip_input to take the first octet of ip address
        - if the first octet is similar to tag in Geoip file, check ip in list cidrs
        :param ip_addr : ip address input
        :param ipaddr : ip address input is fragmented into different octets
        :param add : item in list of cidrs
        :return: name of data center
        """
        ip_addr = self.is_ip_valid()
        ipaddr = self.address.split('.')

        if ip_addr is None:
            return "ip doesn't have a valid ip configuration"

        for geoip in GEOIP_CIDRS:
            H[int(geoip['tag'])] = geoip['cidrs']
        try:
            for add in H[int(ipaddr[0])]:
                if ip_addr in ipaddress.ip_network(add[0]):
                    return add[1]
            else:
                return "Ip does not belong to any datatacenter"
        except ValueError:
            return None

ip = '45.124.88.3'


print(IpLookUp(ip).ip_range())


