# Port Scanner

This is a basic example of a TCP port scanner using Python. Additionally, detect port scanning activities using a simple technique called "TCP SYN Stealth Scan detection."


<h2>Detect TCP SYN Stealth Scan:</h2>

TCP SYN Stealth Scan is a common type of port scan that attempts to determine which ports are open on a target system by sending SYN packets without completing the TCP handshake. We can detect this type of scan by analyzing incoming packets with the tcp.flags field set to SYN and not ACK (acknowledgment). In a real-world scenario, you would use an Intrusion Detection System (IDS) or network monitoring tool, but here's a simple example using Scapy (a Python library for packet manipulation) to demonstrate the concept.

The code sets up a basic TCP port scanner that attempts to connect to a list of specified ports on a given host. If the connection is successful, it considers the port as "open"; otherwise, it assumes the port is "closed." The scanner iterates through the list of ports and performs the scan for each one.

The socket module provides a convenient way to work with sockets, which are endpoints for network communication. The socket.AF_INET argument indicates that we are using the Internet Address Family (IPv4). The socket.SOCK_STREAM argument specifies that we want to create a TCP socket.

The sock.settimeout(1) line sets a timeout of 1 second for the connection attempt. If the connection is not established within this time, the connection attempt will be terminated.

In the main part of the code, you can set the target_host variable to the IP address or domain name of the system you want to scan. The ports_to_scan list contains the port numbers that the scanner will attempt to connect to.

The for loop iterates through each port in the ports_to_scan list and calls the scan_port() function for each one. Inside the scan_port() function, the code tries to connect to the specified port using the sock.connect_ex() method.

If the connection attempt is successful (indicated by a return value of 0), the scanner prints a message indicating that the port is open. Otherwise, it prints a message stating that the port is closed or that an error occurred during the connection attempt.

That's the basic logic behind the TCP Port Scanner in the provided code. Remember to use it responsibly and only on systems where you have proper authorization. Unauthorized scanning of networks or systems is illegal and unethical.
