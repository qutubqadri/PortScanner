import socket

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout for the connection attempt
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        sock.close()
    except Exception as e:
        print(f"Error while scanning port {port}: {str(e)}")

if __name__ == "__main__":
    target_host = "127.0.0.1"  # Replace with the IP address or domain name you want to scan
    ports_to_scan = [21, 22, 80, 443, 3389]  # Add more ports to scan if needed

    for port in ports_to_scan:
        scan_port(target_host, port)
