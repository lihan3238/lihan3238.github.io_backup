# -*- coding: utf-8 -*-
from scapy.all import *

# 禁用Scapy IPv6提示
conf.ipv6_enabled = False

def tcp_connect_scan(target_ip, target_port):
    print(f"\033[31m[tcp_connect_scan]\033[0m {target_port}...\n")
    response = sr1(IP(dst=target_ip)/TCP(dport=target_port, flags="S"), timeout=2)
    if response and response.haslayer(TCP):
        if response[TCP].flags == 0x12:
            send(IP(dst=target_ip)/TCP(dport=target_port, flags="R"))
            print(f"Port {target_port} is open\n")
        elif response[TCP].flags == 0x14:
            print(f"Port {target_port} is closed\n")
    else:
        print(f"Port {target_port} is filtered\n")

def tcp_stealth_scan(target_ip, target_port):
    print(f"\033[31m[tcp_stealth_scan]\033[0m {target_port}...\n")
    response = sr1(IP(dst=target_ip)/TCP(dport=target_port, flags="S"), timeout=2)
    if response and response.haslayer(TCP):
        if response[TCP].flags == 0x12:
            send(IP(dst=target_ip)/TCP(dport=target_port, flags="R"))
            print(f"Port {target_port} is open\n")
        elif response[TCP].flags == 0x14:
            print(f"Port {target_port} is closed\n")
    else:
        print(f"Port {target_port} is filtered\n")

def tcp_xmas_scan(target_ip, target_port):
    print(f"\033[31m[tcp_xmas_scan]\033[0m {target_port}...\n")
    response = sr1(IP(dst=target_ip)/TCP(dport=target_port, flags="FPU"), timeout=2)
    if response and response.haslayer(TCP):
        if response[TCP].flags == 0x14:
            print(f"Port {target_port} is closed\n")
    else:
        print(f"Port {target_port} is filtered or opened\n")

def tcp_fin_scan(target_ip, target_port):
    print(f"\033[31m[tcp_fin_scan]\033[0m {target_port}...\n")
    response = sr1(IP(dst=target_ip)/TCP(dport=target_port, flags="F"), timeout=2)
    if response and response.haslayer(TCP):
        if response[TCP].flags == 0x14:
            print(f"Port {target_port} is closed\n")
    else:
        print(f"Port {target_port} is filtered or opened\n")

def tcp_null_scan(target_ip, target_port):
    print(f"\033[31m[tcp_null_scan]\033[0m {target_port}...\n")
    response = sr1(IP(dst=target_ip)/TCP(dport=target_port, flags=""), timeout=2)
    if response and response.haslayer(TCP):
        if response[TCP].flags == 0x14:
            print(f"Port {target_port} is closed\n")
    else:
        print(f"Port {target_port} is filtered or opened\n")

def udp_scan(target_ip, target_port):
    print(f"\033[31m[udp_scan]\033[0m {target_port}...\n")
    
    # 发送一个零字节的UDP数据包到目标端口
    udp_packet = IP(dst=target_ip)/UDP(dport=target_port)
    response = sr1(udp_packet, timeout=2, verbose=0)
    
    if response is None:
        # 没有回应，通常认为端口是开放的
        print(f"Port {target_port} is open or filtered\n")
    else:
        if response.haslayer(ICMP):
            # 收到ICMP错误消息
            if int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [3, 13, 14]:
                print(f"Port {target_port} is closed\n")
        else:
            print(f"Port {target_port} is open or filtered\n")



# 输入目标IP地址
target_ip = input("请输入目标IP地址: ")

# 输入要扫描的端口列表，以逗号分隔
target_ports = input("请输入要扫描的端口列表 (例如:80,443,22): ")
target_ports = [int(port) for port in target_ports.split(',')]

# 选择扫描类型
print("请选择扫描类型:1. TCP Connect Scan|2. TCP Stealth Scan|3. TCP Xmas Scan|4. TCP Fin Scan|5. TCP Null Scan|6. UDP Scan")

scan_types = input("请输入要扫描的模式列表 (1,2,3,4,5,6): ")
scan_types = [int(scan_type) for scan_type in scan_types.split(',')]

for scan_type in scan_types:
    if scan_type == 1:
        for port in target_ports:
            tcp_connect_scan(target_ip, port)
    elif scan_type == 2:
        for port in target_ports:
            tcp_stealth_scan(target_ip, port)
    elif scan_type == 3:
        for port in target_ports:
            tcp_xmas_scan(target_ip, port)
    elif scan_type == 4:
        for port in target_ports:
            tcp_fin_scan(target_ip, port)
    elif scan_type == 5:
        for port in target_ports:
            tcp_null_scan(target_ip, port)
    elif scan_type == 6:
        for port in target_ports:
            udp_scan(target_ip, port)
    else:
        print("无效的扫描类型选择")