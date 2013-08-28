'''
Created on Aug 28, 2013

@author: george
'''


import socket
import thread
from optparse import OptionParser


class Scanner:
    def __init__(self, address, port=-1):
        self.host = address
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(0.1);
    def scanPorts(self):
        if self.port != -1:
           
            try:
                print "trying port %s on host %s" % (self.port, self.host)
                self.socket.connect((self.host, self.port))
                print "port is open"
            except Exception:
                print "Unable to connect to port"
        
        else:
            for i in range(1,65535):
                mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               # print "trying port ", i
                try:
                    mySocket.connect((self.host,i))
                    mySocket.close()
                    print "port %d is open" % i
                except Exception:
                    mySocket.close()
                    continue
   
            

if __name__ == "__main__":
    usage = "usage: %prog [options] address"
    parser = OptionParser(usage=usage)
    parser.add_option("-p", "--port", action="store", default="-1", type="int", dest="port", help="scan a spesific port")
    (options, args) = parser.parse_args()    
    scanner = Scanner(args[0], options.port)
    scanner.scanPorts()
