#!/usr/bin/python2

# Script to test all 254 IP addresses on the 192.168.95.0/24 subnet with the ports offering telnet, SSH, smtp, http, imap, and https services

import socket
import os
import sys
def retbanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s=socket.socket()
        s.connect((ip, port))
        banner=s.recv(1024)
        return banner
    except:
        return
def checkvulns(banner, filename):
    f=open('filename', 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print '[+] Server is vulnerable: ' + banner.strip('\n')
def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print '[-] ' + filename + ' does not exist.'
            exit(0)
            if not os.access(filename, os.r_ok):
                print '[-] ' + filename + ' access denied.'
                exit(0)
        else:
            print '[-] usage: ' + str(sys.argv[0]) + ' < vuln filename>'
            exit(0)
            portlist=[21,22,25,80,110,443]
            for x in range(147, 150):
                ip='192.168.95.' + str(x)
                # print ip
                for port in portlist:
                    print 'checking ' + ip + '/' + str(port)
                    banner=retbanner(ip,port)
                    if banner:
                        print '[+] ' + ip + ': ' + banner
                        checkvulns(banner)
if __name__=='__main__':
    main()
