import socket  # Import the socket module to create and manage network connections

def scan_port(host, port):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout for the connection attempt (1 second in this case)
        sock.settimeout(1)

        # Try to connect to the specified host and port
        result = sock.connect_ex((host, port))

        # If the connection was successful (port is open), result will be 0
        if result == 0:
            print(f"Port {port} is open")
        else:
            # If the connection was unsuccessful (port is closed), result will be an error code
            print(f"Port {port} is closed")

        # Close the socket
        sock.close()

    # Handle exceptions, e.g., if there's an error during the connection attempt
    except Exception as e:
        print(f"Error while scanning port {port}: {str(e)}")

if __name__ == "__main__":
    target_host = "127.0.0.1"  # Replace with the IP address or domain name you want to scan
    ports_to_scan = [21, 22, 80, 443, 3389]  # Add more ports to scan if needed

    # Iterate over the list of ports and scan each one on the target host
    for port in ports_to_scan:
        scan_port(target_host, port)
