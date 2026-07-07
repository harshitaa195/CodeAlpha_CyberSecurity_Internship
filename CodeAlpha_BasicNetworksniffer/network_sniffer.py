import socket
import threading
from scapy.all import sniff
from scapy.layers.inet import IP

def asd(qwe):
    if qwe.haslayer(IP):
        print("Source IP :", qwe[IP].src)
        print("Destination IP :", qwe[IP].dst)
        print("Protocol :", qwe[IP].proto)

sniff(prn=asd, count=20)




def asd(qwe):
    try:
        xyz = qwe.recv(1024)
        print("Data Received:")
        print(xyz.decode(errors="ignore"))
    except:
        pass

def zxc():
    abc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    abc.bind(("0.0.0.0", 9999))
    abc.listen(5)

    print("Listening on Port 9999...")

    while True:
        qwe, ert = abc.accept()
        print("Connection From:", ert)

        tyu = threading.Thread(target=asd, args=(qwe,))
        tyu.start()

zxc()