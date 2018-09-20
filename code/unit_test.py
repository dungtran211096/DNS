import unittest
from iplookup import IpLookUp
from readfile import ReadFile
from hash import CuckooHash
import ipaddress as ip

class TestIpLookUp(unittest.TestCase):
    def setUp(self):
        self.data = ReadFile("/media/dung/Dung Tran/GSLB/geoip_data.dat")
        self.big_hash = CuckooHash(1000)
        self.list = []

    def test_read_file(self):
        for i in self.data.read_file():
            self.big_hash[i[0]] = i[1]

    def test_full_hash(self):
        for i in self.big_hash.keys():
            self.assertEqual(self.big_hash[i], i)

    def test_ip(self):
        self.ip = "203.119.8.1/24"
        self.assertTrue(IpLookUp(self.ip).is_ip_valid(), self.ip)
        self.assertEqual(IpLookUp(self.ip).ip_range(), 'vdc-01')
        self.assertNotEqual(IpLookUp(self.ip).ip_range(), 'vdc-02')
        self.assertTrue(IpLookUp("111.111.111.11/22").ip_range())
        self.assertTrue(IpLookUp("117.70.0.0/15").ip_range())

    def test_distance(self):
        ip1 = "203.119.50.1/23"
        ip2 = "203.119.8.0/22"
        ip3 = "103.63.112.0/22"
        ip4 = "103.63.8.0/24"
        ip5 = "118.100.0.1/24"
        ip6 = "118.68.0.0/15"
        ip7 = "221.134.8.1/24"
        ip8 = "221.132.30.0/23"
        ip9 = "203.119.0.1/24"
        ip10 = "203.119.0.0/23"
        ip11 = "203.119.50/24"
        ip12 = "203.119.0.0/23"
        ip13= "192.168.0.0/26"  
        ip14 = "192.168.20.19/24"
        self.assertEqual(IpLookUp(ip1).ip_range(), IpLookUp(ip2).ip_range())
        self.assertEqual(IpLookUp(ip3).ip_range(), IpLookUp(ip4).ip_range())
        self.assertNotEqual(IpLookUp(ip5).ip_range(), IpLookUp(ip6).ip_range())
        self.assertEqual(IpLookUp(ip7).ip_range(), IpLookUp(ip8).ip_range())
        self.assertEqual(IpLookUp(ip9).ip_range(), IpLookUp(ip10).ip_range())
        self.assertEqual(IpLookUp(ip13).ip_range(), IpLookUp(ip14).ip_range())

    def test_longest_prefix(self):
        ip1 = "203.119.58.1/24"
        print("Longest_prefix: %s " % IpLookUp(ip1).ip_range())

if __name__ == '__main__':
    unittest.main()