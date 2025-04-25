import socket

# Function to scan a specific range of ports on a target IP
def scan_ports(target_ip, start_port, end_port):
    print(f"\nScanning {target_ip} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # Short timeout to speed up scanning

        result = s.connect_ex((target_ip, port))  # Try to connect

        if result == 0:
            print(f"Port {port} is OPEN ✅")
        else:
            print(f"Port {port} is CLOSED ❌")

        s.close()

# Ask the user for IP and port range
if __name__ == "__main__":
    target = input("Enter target IP address: ")
    start = int(input("Enter start port (e.g., 20): "))
    end = int(input("Enter end port (e.g., 80): "))

    scan_ports(target, start, end)
