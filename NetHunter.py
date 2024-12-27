from scapy.all import ARP, Ether, srp

def scan(ip_range):
    
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    
    devices = []
    for sent, received in answered_list:
        devices.append({"ip": received.psrc, "mac": received.hwsrc})
    return devices

def display_results(devices):
    print("Dispositivos encontrados:")
    print("IP Address\t\tMAC Address")
    print("-" * 40)
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}")

if __name__ == "__main__":
    target_range = input("Ingresa el rango de IP (e.g., 192.168.1.0/24): ")
    devices = scan(target_range)
    display_results(devices)