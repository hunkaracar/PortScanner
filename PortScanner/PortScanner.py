#!/bin/python3

import socket
import sys
import pyfiglet
from datetime import datetime
import requests
import time




class PortScanner:

    def initliaze(self):

        result_show = pyfiglet.figlet_format("PORT SCANNER")
        print(result_show)


    def Pinging(self):

        print("Example Url=>https://www.example.com")
        url = input("Enter the web site url ==>> ")
        response = requests.get(url)

        if response.status_code == 200:
            print(f"Ping to {url} $successful$")

        else:
            print(f"Ping to {url} #failed#. Status Code: {response.status_code}")


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        url_new = input("Enter the web site url(exam=>example.com) => ")

        ipaddress = socket.getaddrinfo(url_new,4040,proto=socket.IPPROTO_TCP)

        print("/*/" * 20)

        print("Ip Address web sites => {}".format(ipaddress[0][4][0]))
        print("Port Used => {}".format(ipaddress[0][4][1]))





    def portScanner(self):

        if len(sys.argv) == 2:

            # translate hostname to IPv4
            target = socket.gethostbyname(sys.argv[1])

        else:

            print("Sytax: python PortScanner.py <ip> ")




        # Add Banner

        print("-" * 40)
        print("Scanning Target: " + target)
        print("Scanning started at: " + str(datetime.now()))
        print("-" * 40)

        try:

            # will scan ports between1to1500
            for port in range(1, 2001):

                """
                socket.AF_INET => IPv4 protocols for TCP and UDP
                socket.SOCK_STREAM => TCP connection type
                """
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)

                # returns an error indicator
                # s.connect_ex => used to connect to the server.Returns 0(zero) if successfully connected
                result = s.connect_ex((target,port))
                if result == 0:
                    print("Discovery {} Port is open".format(port))
                s.close()


        except KeyboardInterrupt:
            print("\n Exiting Program !!!!")
            sys.exit()

        except socket.gaierror:
            #usually caused by incorrect hostname or ip address specified
            print("\n Hostname Could Not Be Resolved !!!!")
            sys.exit()

        except socket.error:
            # caused by server-side error
            print("\n Server not Responding !!!")
            sys.exit()


if __name__ == '__main__':

    portscanner = PortScanner()
    portscanner.initliaze()


    print("""
    [1].Pinging
    [2].Port Scanner
    [3].Show Options
    [4].More İnformation(Socket Programming)
    [5].Exit
    """)

    while 1==1:

        chose = int(input("Please select the option you want to choose(Exam => 1) ==>> "))

        if chose == 1:
            portscanner.Pinging()
            continue

        try:
            if chose == 2:
                portscanner.portScanner()
                continue

        except UnboundLocalError:
            print("""
            
            Select this option from normal terminal => python PortScanner.py <targetsiteip>
            You can use other options to use this option and to ping the address of the target site and find out its IP^^
            Then choose 2 of the options and wait for the port scan^^
            """)

        if chose == 3:
            print("""
               [1].Pinging
               [2].Port Scanner
               [3].Show Options
               [4].More İnformation(Socket Programming)
               [5].Exit
               """)
            continue

        if chose == 4:
            print("Redirecting to page....")
            time.sleep(3)
            r = requests.get('https://docs.python.org/3/library/socket.html')
            print(r.url)


        if chose == 5:
            print("Exiting....")
            time.sleep(2)
            break






